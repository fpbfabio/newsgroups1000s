#!/usr/bin/env python3


import sys

sys.path.insert(0, "../python/")

from utils import Utils
from document import Document
from const import *


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
    def extract_file_name_test():
        test_list = ["/abc/def/ghi/jkl.txt", "/abc/def/ghi/jkl", "jkl.txt", "jkl"]
        for item in test_list:
            if (Utils.extract_file_name(item) != "jkl"):
                print("-----ERROR-----Utils.extract_dir------" + Utils.extract_file_name(item))

    @staticmethod
    def extract_file_parent_folder():
        test_list = ["/abc/def/ghi/jkl.txt", "ghi/jkl"]
        for item in test_list:
            if (Utils.extract_file_parent_folder(item) != "ghi"):
                print("-----ERROR-----Utils.extract_dir------" + Utils.extract_file_name(item))

    @staticmethod
    def extract_file_extension_test():
        test_dictionary = {"/abc~/def/ghi/jkl.txt":".txt", "/abc/def/ghi~/jkl":None, "jkl.txt~":".txt~", "jkl~":None, "/abc/def/ghi~/jkl~":None}
        for key in test_dictionary:
            if (Utils.extract_file_extension(key) != test_dictionary[key]):
                print("-----ERROR-----Utils.extract_file_extension----" + key)

    @staticmethod
    def is_backup_file_test():
        test_dictionary = {"/abc~/def/ghi/jkl.txt":False, "/abc/def/ghi~/jkl":False, "jkl.txt~":True, "jkl~":True, "/abc/def/ghi~/jkl~":True}
        for key in test_dictionary:
            if (Utils.is_backup_file(key) != test_dictionary[key]):
                print("-----ERROR-----Utils.is_backup_file----" + key)

    @staticmethod
    def is_interger_test():
        test_dictionary = {"1":True, " 1":True, "1 ":True, "a1":False, "1 1":False}
        for key in test_dictionary:
            if (Utils.is_integer(key) != test_dictionary[key]):
                print("-----ERROR-----Utils.is_integer_test----" + "'" + key + "'")


UtilsTest.string_find_test()
UtilsTest.string_replace_test()
UtilsTest.extract_file_name_test()
UtilsTest.extract_file_parent_folder()
UtilsTest.extract_file_extension_test()
UtilsTest.is_backup_file_test()
UtilsTest.is_interger_test()