#!/usr/bin/env python3


from const import *


class Utils:

    @staticmethod
    def string_find(to_find_string, target_string):
        result = str(target_string).find(to_find_string)
        if (result != -1):
            return result
        return None

    @staticmethod
    def string_replace(to_find_string, replace_string, target_string):
        index = Utils.string_find(to_find_string, target_string)
        if (index is None):
            return target_string
        to_find_string_length = len(to_find_string)
        beginning = EMPTY_STRING
        end = EMPTY_STRING
        if (index > 0):
            beginning = target_string[0:index]
        if (index + to_find_string_length < len(target_string)):
            end = target_string[index + to_find_string_length:]
        new_string = beginning + replace_string + end
        return new_string

    @staticmethod
    def extract_file_name(path):
        name = path
        for i in range(len(path) - 1, -1, -1):
            if (path[i] == LINUX_PATH_SEPARATOR):
                most_right_slash_index = i
                name = path[most_right_slash_index + 1:]
                break
        if (FILE_EXTENSION_SEPARATOR in name):
            dot_index = Utils.string_find(FILE_EXTENSION_SEPARATOR, name)
            name = name[0:dot_index]
        return name

    @staticmethod
    def is_backup_file(path):
        if (BACKUP_SYMBOL in path):
            return True
        return False
