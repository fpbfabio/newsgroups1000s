#!/usr/bin/env python3


from const import *
from newsgroups import Newsgroups

class Document:

    def __init__(self, identifier):
        self.content_list = [[DOCUMENT_IDENTIFIER_FIELD_NAME, identifier]]

    @property
    def identifier(self):
        return self.field(DOCUMENT_IDENTIFIER_FIELD_NAME)

    @identifier.setter
    def identifier(self, identifier):
        self.set_field(DOCUMENT_IDENTIFIER_FIELD_NAME, identifier)

    def add_field(self, field_name, field_value):
        self.content_list.append([field_name, field_value])

    def field(self, field_name):
        for inner_list in self.content_list:
            if (inner_list[DOCUMENT_FIELD_NAME_INDEX] == field_name):
                return inner_list[DOCUMENT_FIELD_VALUE_INDEX]
        return None

    def set_field(self, field, value):
        for inner_list in self.content_list:
            if (inner_list[DOCUMENT_FIELD_NAME_INDEX] == field):
                inner_list[DOCUMENT_FIELD_VALUE_INDEX] = value

    def append_field(self, field_name, field_value):
        for inner_list in self.content_list:
            if (inner_list[DOCUMENT_FIELD_NAME_INDEX] == field_name):
                inner_list[DOCUMENT_FIELD_VALUE_INDEX] += field_value

    def has_field(self, field_name):
        for inner_list in self.content_list:
            if (inner_list[DOCUMENT_FIELD_NAME_INDEX] == field_name):
                return True
        return False