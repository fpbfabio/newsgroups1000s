#!/usr/bin/env python3


import sys

sys.path.insert(0, "../python/")

from newsgroups import Newsgroups
from const import *

class NewsgroupsTest:

    @staticmethod
    def validate_field_name_test():
        for item in Newsgroups.SCHEMA_STATIC_FIELD_NAMES:
            if (not Newsgroups.validate_field_name(item)):
                print("-----ERROR-----Newsgroups.validate_field_name")
        for item in Newsgroups.SCHEMA_STATIC_FIELD_NAMES:
            if (Newsgroups.validate_field_name(item + BLANK_SPACE)):
                print("-----ERROR-----Newsgroups.validate_field_name")
        for item in Newsgroups.SCHEMA_DYNAMIC_FIELD_NAMES:
            if (not Newsgroups.validate_field_name("XX" + item + "XXXX")):
                print("-----ERROR-----Newsgroups.validate_field_name")


NewsgroupsTest.validate_field_name_test()