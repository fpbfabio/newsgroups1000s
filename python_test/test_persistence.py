#!/usr/bin/env python3


import sys

sys.path.insert(0, "../python/")

from persistence import Persistence
from document import Document


class PersistenceTest:

    @staticmethod
    def document_to_solr_xml_test():
        file_name = "test_files/document_list_to_solr_xml_test.xml"
        document = Document("document_list_to_solr_xml_test")
        document.add_field("year", "2015")
        document.add_field("month", "2")
        document.add_field("day", "15")
        document.add_field("<>&'\"", "<>&'\"")
        Persistence.document_to_solr_xml(document, file_name)
        print("PersistenceTest.document_to_solr_xml_test() ----- Warning: need to read file: " + file_name )

    @staticmethod
    def get_document_from_file_test():
        file_name = "test_files/49960"
        document = Persistence.get_document_from_file(file_name);
        with open("test_files/get_document_from_file_test.txt", "w") as archive:
            for item in document.content_list:
                archive.write("\n\n--------" + item[0] + "--------\n\n" + item[1])
        print("PersistenceTest.get_document_from_file_test() ----- Warning: need to read file: " + "test_files/get_document_from_file_test.txt")
        return document


PersistenceTest.document_to_solr_xml_test()
PersistenceTest.get_document_from_file_test()