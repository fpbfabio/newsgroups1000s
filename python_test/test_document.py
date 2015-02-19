#!/usr/bin/env python3

import sys

sys.path.insert(0, "../python/")

from document import Document


class DocumentTest:

    @staticmethod
    def add_field_test():
        document = Document("1234")
        document.add_field("Test", "Testing")
        field_name = document.content_list[len(document.content_list) - 1][0]
        field_value = document.content_list[len(document.content_list) - 1][1]
        if (field_name != "Test" or field_value != "Testing"):
            print("-----ERROR-----Document.add_field_test")

    @staticmethod
    def field_test():
        document = Document("1234")
        document.add_field("Test", "Testing")
        if (document.field("Test") != "Testing"):
            print("-----ERROR-----Document.field_test")

    @staticmethod
    def set_field_test():
        document = Document("1234")
        document.add_field("Test", "Testing")
        document.set_field("Test", "abcd")
        if (document.field("Test") != "abcd"):
            print("-----ERROR-----Document.set_field_test")

    @staticmethod
    def append_field():
        document = Document("1234")
        document.add_field("Test", "abcd")
        document.append_field("Test", "efgh")
        if (document.field("Test") != "abcdefgh"):
            print("-----ERROR-----Document.append_field_test")

    @staticmethod
    def has_field_test():
        document = Document("1234")
        document.add_field("Test", "abcd")
        if (not document.has_field("Test")):
            print("-----ERROR-----Document.has_field_test")


DocumentTest.add_field_test()
DocumentTest.field_test()
DocumentTest.set_field_test()
DocumentTest.append_field()
DocumentTest.has_field_test()