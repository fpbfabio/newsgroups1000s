#!/usr/bin/env python3


from const import TAB_SPACE, WRITE
from message import Message


class Utils:

    @staticmethod
    def string_find(to_find, target):
        result = str(target).find(to_find)
        if (result != -1):
            return result
        return None

    @staticmethod
    def string_replace(to_find, replace, target):
        index = Utils.string_find(to_find, target)
        if (index is None):
            return target
        to_find_length = len(to_find)
        beginning = ""
        end = ""
        if (index > 0):
            beginning = target[0:index]
        if (index + to_find_length < len(target)):
            end = target[index + to_find_length:]
        new_string = beginning + replace + end
        return new_string

    @staticmethod
    def extract_file_name(path):
        name = path
        for i in range(len(path) - 1, -1, -1):
            if (path[i] == "/"):
                most_right_slash_index = i
                name = path[most_right_slash_index + 1:]
                break
        if ("." in name):
            dot_index = Utils.string_find(".", name)
            name = name[0:dot_index]
        return name

    @staticmethod
    def message_to_solr_xml(message, path):
        with open(path, WRITE) as archive:
            archive.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n\n")
            archive.write("<add>\n")
            archive.write(TAB_SPACE + "<doc>\n")
            for element in message.content_list:
                field = element[0]
                value = element[1]
                for tup in [("&", "&amp;"), ("<", "&lt;"), (">", "&gt;"), ("'", "&apos;"), ("\"", "&quot;")]:
                    field = Utils.string_replace(tup[0], tup[1], field)
                    value = Utils.string_replace(tup[0], tup[1], value)
                archive.write(2 * TAB_SPACE + "<field name=\"" + field + "\">" + value + "</field>\n")
            archive.write(TAB_SPACE + "</doc>\n")
            archive.write("</add>")

    @staticmethod
    def get_message_from_file(path):
        with open(path) as archive:
            file_name = Utils.extract_file_name(path)
            message = Message(file_name)
            can_add_new_list = True
            size = 0
            for line in archive:
                colon_index = Utils.string_find(":", line)
                if (can_add_new_list and (colon_index is not None) and (" " not in line[0:colon_index])):
                    field = line[0:colon_index]
                    value = line[colon_index + 1:].lstrip().rstrip("\n")
                    message.add_field(field, value)
                else:
                    if (can_add_new_list):
                        message.add_field("text", "")
                        size = len(message.content_list)
                    can_add_new_list = False
                    message.append_field("text", line)
        return message