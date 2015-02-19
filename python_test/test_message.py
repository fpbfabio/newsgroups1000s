#!/usr/bin/env python3

import sys

sys.path.insert(0, "../python/")

from message import Message


class MessageTest:

    @staticmethod
    def add_field_test():
        message = Message("1234")
        message.add_field("Test", "Testing")
        field_name = message.content_list[len(message.content_list) - 1][0]
        field_value = message.content_list[len(message.content_list) - 1][1]
        if (field_name != "Test" or field_value != "Testing"):
            print("-----ERROR-----Message.add_field_test")

    @staticmethod
    def field_test():
        message = Message("1234")
        message.add_field("Test", "Testing")
        if (message.field("Test") != "Testing"):
            print("-----ERROR-----Message.field_test")

    @staticmethod
    def set_field_test():
        message = Message("1234")
        message.add_field("Test", "Testing")
        message.set_field("Test", "abcd")
        if (message.field("Test") != "abcd"):
            print("-----ERROR-----Message.set_field_test")

    @staticmethod
    def append_field():
        message = Message("1234")
        message.add_field("Test", "abcd")
        message.append_field("Test", "efgh")
        if (message.field("Test") != "abcdefgh"):
            print("-----ERROR-----Message.append_field_test")

    @staticmethod
    def has_field_test():
        message = Message("1234")
        message.add_field("Test", "abcd")
        if (not message.has_field("Test")):
            print("-----ERROR-----Message.has_field_test")


MessageTest.add_field_test()
MessageTest.field_test()
MessageTest.set_field_test()
MessageTest.append_field()
MessageTest.has_field_test()