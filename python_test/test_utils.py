#!/usr/bin/env python3


import sys

sys.path.insert(0, "../python/")

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


if __name__ == "__main__":
    UtilsTest.string_find_test()
    UtilsTest.string_replace_test()
    UtilsTest.extract_dir_test()