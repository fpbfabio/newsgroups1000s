#!/usr/bin/env python3


#---------Class implementation section---------#


class Message:

    def __init__(self, identifier):
        self.identifier = identifier
        self.content = ""

    @staticmethod
    def from_file(file_name):
        with open(file_name) as archive:
            message = Message(file_name)
            for line in archive:
                message.content = message.content + line
        return message


#---------Unit testing section---------#


class MessageTest:

    @staticmethod
    def from_file_test():
        file_name = "49960"
        message = Message.from_file(file_name);
        for k in message.__dict__:
            print("--------" + k + "--------\n\n" + message.__dict__[k])


if __name__ == "__main__":
    MessageTest.from_file_test()
