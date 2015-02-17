#!/usr/bin/env python3


import sys

sys.path.insert(0, "../python/")

from persistence import Persistence
from message import Message


class PersistenceTest:

    @staticmethod
    def message_to_solr_xml_test():
        file_name = "test_files/message_list_to_solr_xml_test.xml"
        message = Message("message_list_to_solr_xml_test")
        message.add_field("year", "2015")
        message.add_field("month", "2")
        message.add_field("day", "15")
        message.add_field("<>&'\"", "<>&'\"")
        Persistence.message_to_solr_xml(message, file_name)
        print("PersistenceTest.message_to_solr_xml_test() ----- Warning: need to read file: " + file_name )

    @staticmethod
    def get_message_from_file_test():
        file_name = "test_files/49960"
        message = Persistence.get_message_from_file(file_name);
        with open("test_files/get_message_from_file_test.txt", "w") as archive:
            for item in message.content_list:
                archive.write("\n\n--------" + item[0] + "--------\n\n" + item[1])
        print("PersistenceTest.get_message_from_file_test() ----- Warning: need to read file: " + "test/get_message_from_file_test.txt")
        return message


if __name__ == "__main__":
    PersistenceTest.message_to_solr_xml_test()
    PersistenceTest.get_message_from_file_test()