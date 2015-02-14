#!/usr/bin/env python3


#---------Class implementation---------#


class Utils:

    @staticmethod
    def string_find(char, string):
        length = len(string);
        for i in range(0, length):
            if (string[i] == char):
                return i
        return None


#---------Unit test class---------#


class UtilsTest:

    @staticmethod
    def string_find_test():
        test_string = "abcd"
        if (Utils.string_find(test_string[0], test_string) == 0
            and Utils.string_find(test_string[len(test_string) - 1], test_string) == len(test_string) - 1
            and Utils.string_find("z", test_string) is None):
            print("Utils.string_find works!")
            return
        print("-----ERROR-----Utils.string_find")


#---------Unit test execution---------#


if __name__ == "__main__":
    UtilsTest.string_find_test()

