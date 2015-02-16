#!/usr/bin/env python3


from utils import Utils
from message import Message


class UtilsTest:

    @staticmethod
    def string_find_test():
        test_string = "abcd"
        if (Utils.string_find(test_string[0], test_string) != 0
            or Utils.string_find(test_string[len(test_string) - 1], test_string) != len(test_string) - 1
            or Utils.string_find("z", test_string) is not None):
            print("-----ERROR-----Utils.string_find")

    @staticmethod
    def string_replace_test():
        string = "Teste1 Teste2 Teste3"
        string = Utils.string_replace("Teste2", "Teste4", string)
        string = Utils.string_replace("Teste1", "Teste5", string)
        if (string != "Teste5 Teste4 Teste3"):
            print (string)
            print("-----ERROR-----Utils.string_replace")

    @staticmethod
    def extract_dir_test():
        test_list = ["/abc/def/ghi/jkl.txt", "/abc/def/ghi/jkl", "jkl.txt", "jkl"]
        for item in test_list:
            if (Utils.extract_file_name(item) != "jkl"):
                print("-----ERROR-----Utils.extract_dir------" + Utils.extract_file_name(item))

    @staticmethod
    def message_to_solr_xml_test():
        file_name = "test/nested_list_to_solr_xml_test.xml"
        message = Message(file_name)
        message.add_field("year", "2015")
        message.add_field("month", "2")
        message.add_field("day", "15")
        message.add_field("<>&'\"", "<>&'\"")
        Utils.message_to_solr_xml(message, file_name)
        print("Warning: need to read file: " + file_name )

    @staticmethod
    def get_message_from_file_test():
        file_name = "test/49960"
        message = Utils.get_message_from_file(file_name);
        with open("test/get_message_from_file_test.txt", "w") as archive:
            for item in message.content_list:
                archive.write("\n\n--------" + item[0] + "--------\n\n" + item[1])
        print("Warning: need to read file: " + "test/get_message_from_file_test.txt")
        #for item in message.content_list:
        #    print("--------" + item[0] + "--------\n\n" + item[1])
        return message


if __name__ == "__main__":
    UtilsTest.string_find_test()
    UtilsTest.string_replace_test()
    UtilsTest.extract_dir_test()
    UtilsTest.message_to_solr_xml_test()
    UtilsTest.get_message_from_file_test()