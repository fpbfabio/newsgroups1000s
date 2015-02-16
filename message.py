#!/usr/bin/env python3


class Message:

    def __init__(self, identifier):
        self.content_list = [["id", identifier]]

    @property
    def identifier(self):
        return self.content_list[0][1]

    @identifier.setter
    def identifier(self, identifier):
        self.content_list[0][1] = identifier

    def add_field(self, field, value):
        self.content_list.append([field, value])

    def field(self, field):
        for item in self.content_list:
            if (item[0] == field):
                return item[1]
        return None

    def set_field(self, field, value):
        for item in self.content_list:
            if (item[0] == field):
                item[1] = value

    def append_field(self, field, value):
        for item in self.content_list:
            if (item[0] == field):
                item[1] += value