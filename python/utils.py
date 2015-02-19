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
    def extract_file_parent_folder(path):
        name = path
        for i in range(len(path) - 1, -1, -1):
            if (path[i] == LINUX_PATH_SEPARATOR):
                most_right_slash_index = i
                break
        second_most_right_slash_index = -1
        for i in range(most_right_slash_index - 1, -1, -1):
            if (path[i] == LINUX_PATH_SEPARATOR):
                second_most_right_slash_index = i
                break
        parent_folder_name = path[second_most_right_slash_index + 1:most_right_slash_index]
        return parent_folder_name

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
    def extract_file_extension(path):
        separator_index = None
        file_extension = None
        for i in range(len(path) - 1, -1, -1):
            if (path[i] == LINUX_PATH_SEPARATOR):
                break
            if (path[i] == FILE_EXTENSION_SEPARATOR):
                separator_index = i
        if (separator_index is not None):
            file_extension = path[separator_index:]
        return file_extension

    @staticmethod
    def is_backup_file(path):
        file_name = Utils.extract_file_name(path)
        file_extension = Utils.extract_file_extension(path)
        if (file_extension is not None):
            last_char_index = len(file_extension) - 1
            return file_extension[last_char_index] == BACKUP_SYMBOL
        last_char_index = len(file_name) - 1
        return file_name[last_char_index] == BACKUP_SYMBOL

    @staticmethod
    def is_integer(s):
        try:
            int(s)
            return True
        except ValueError:
            return False