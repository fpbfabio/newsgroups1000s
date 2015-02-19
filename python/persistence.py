#!/usr/bin/env python3


from const import *
from utils import Utils
from document import Document
from newsgroups import Newsgroups


class Persistence:

    @staticmethod
    def document_to_solr_xml(document, path):
        with open(path, WRITE_MODE) as archive:
            archive.write(XML_HEADER)
            archive.write(SOLR_XML_ADD_OPEN_TAG + EOL)
            archive.write(TAB_SPACE + SOLR_XML_DOCUMENT_OPEN_TAG + EOL)
            for inner_list in document.content_list:
                field_name = inner_list[DOCUMENT_FIELD_NAME_INDEX]
                field_value = inner_list[DOCUMENT_FIELD_VALUE_INDEX]
                field_value = Utils.string_replace(CDATA_CLOSE_TAG, "]]" + CDATA_CLOSE_TAG + CDATA_OPEN_TAG + ">", field_value)
                field_open_tag = Utils.string_replace(REPLACE_MASK, field_name, SOLR_XML_FIELD_OPEN_TAG)
                archive.write(2 * TAB_SPACE + field_open_tag + CDATA_OPEN_TAG + field_value + CDATA_CLOSE_TAG + SOLR_XML_FIELD_CLOSE_TAG + EOL)
            archive.write(TAB_SPACE + SOLR_XML_DOCUMENT_CLOSE_TAG + EOL)
            archive.write(SOLR_XML_ADD_CLOSE_TAG)

    @staticmethod
    def get_document_from_file(path):
        if (Utils.is_backup_file(path)):
            return None
        file_name = Utils.extract_file_name(path)
        parent_folder = Utils.extract_file_parent_folder(path)
        document = Document(parent_folder + "_" + file_name)
        document.add_field(Newsgroups.TEXT_FIELD_NAME, EMPTY_STRING)
        try:
            with open(path, READ_MODE) as archive:
                for line in archive:
                    line = line.translate(CONTROL_CHARS_TO_IGNORE)
                    separator_index = Utils.string_find(Newsgroups.FIELD_SEPARATOR, line)
                    line_has_separator = separator_index is not None
                    if (not line_has_separator):
                        document.append_field(Newsgroups.TEXT_FIELD_NAME, line)
                        continue
                    field_name = line[0:separator_index]
                    field_value = line[separator_index + 1:].rstrip(EOL).strip()
                    field_name_is_valid = Newsgroups.validate_field_name(field_name)
                    field_name_is_new = not document.has_field(field_name)
                    is_line_field = field_name == Newsgroups.LINE_FIELD_NAME
                    is_not_integer = not Utils.is_integer(field_value)
                    is_invalid_line_field = is_line_field and is_not_integer
                    if (field_name_is_valid and field_name_is_new and not is_invalid_line_field):
                        document.add_field(field_name, field_value)
                    else:
                        document.append_field(Newsgroups.TEXT_FIELD_NAME, line)
        except UnicodeDecodeError:
            error_document = Utils.string_replace(REPLACE_MASK, str(path), DECODE_ERROR_LOG)
            print(error_document)
            return None
        return document