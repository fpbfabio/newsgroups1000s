#!/usr/bin/env python3


from const import *
from utils import Utils
from message import Message


class Persistence:

    @staticmethod
    def message_to_solr_xml(message, path):
        with open(path, WRITE_MODE) as archive:
            archive.write(XML_HEADER)
            archive.write(SOLR_XML_ADD_OPEN_TAG + EOL)
            archive.write(TAB_SPACE + SOLR_XML_DOCUMENT_OPEN_TAG + EOL)
            for inner_list in message.content_list:
                field_name = inner_list[MESSAGE_FIELD_NAME_INDEX]
                field_value = inner_list[MESSAGE_FIELD_VALUE_INDEX]                    
                field_open_tag = Utils.string_replace(REPLACE_MASK, field_name, SOLR_XML_FIELD_OPEN_TAG)
                archive.write(2 * TAB_SPACE + field_open_tag + CDATA_OPEN_TAG + field_value + CDATA_CLOSE_TAG + SOLR_XML_FIELD_CLOSE_TAG + EOL)
            archive.write(TAB_SPACE + SOLR_XML_DOCUMENT_CLOSE_TAG + EOL)
            archive.write(SOLR_XML_ADD_CLOSE_TAG)

    @staticmethod
    def get_message_from_file(path):
        if (Utils.is_backup_file(path)):
            return None
        try:
            with open(path, READ_MODE) as archive:
                file_name = Utils.extract_file_name(path)
                message = Message(file_name)
                message.add_field(MESSAGE_TEXT_FIELD_NAME, EMPTY_STRING)
                for line in archive:
                    separator_index = Utils.string_find(NEWSGROUPS_CORPORA_FIELD_SEPARATOR, line)
                    if (separator_index is not None and BLANK_SPACE not in line[0:separator_index]):
                        match_dynamic_field = False
                        for string in SOLR_SCHEMA_DYNAMIC_FIELDS:
                            if (string in line[0:separator_index]):
                                match_dynamic_field = True
                        if (line[0:separator_index] in SOLR_SCHEMA_FIELD_NAMES or match_dynamic_field):
                            field_name = line[0:separator_index]
                            field_value = line[separator_index + 1:].lstrip().rstrip(EOL)
                            message.add_field(field_name, field_value)
                    else:
                        message.append_field(MESSAGE_TEXT_FIELD_NAME, line)
        except UnicodeDecodeError:
            error_message = Utils.string_replace(REPLACE_MASK, str(path), DECODE_ERROR_LOG)
            print(error_message)
            return None
        return message
