#!/usr/bin/env python3


from const import *


class Newsgroups:

    FIELD_SEPARATOR = ":"
    SCHEMA_STATIC_FIELD_NAMES = ("Path", "From", "Newsgroups", "Subject", "Message-ID", "Date", "Organization", "Lines", "Sender", "References", "Xref", "Article-I.D.", "Expires", "Followup-To", "Keywords", "Distribution", "Approved", "Supersedes", "Originator", "Content-Type", "X-Newsreader", "Summary")
    SCHEMA_DYNAMIC_FIELD_NAMES = ("Reply-To", "Posting-Host", "Posting-User")
    TEXT_FIELD_NAME = "text"
    LINE_FIELD_NAME = "Lines"

    @staticmethod
    def validate_field_name(string):
        has_no_blank_space = not (BLANK_SPACE in string)
        is_static_field = string in Newsgroups.SCHEMA_STATIC_FIELD_NAMES
        is_dynamic_field = False
        for item in Newsgroups.SCHEMA_DYNAMIC_FIELD_NAMES:
            if item in string:
                is_dynamic_field = True
        return has_no_blank_space and (is_static_field or is_dynamic_field)

