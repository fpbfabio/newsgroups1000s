#!/usr/bin/env python3

REPLACE_MASK = "@MASK"
BLANK_SPACE = " "
FILE_EXTENSION_SEPARATOR = "."
TAB_SPACE = 4 * BLANK_SPACE
WRITE_MODE = "w"
READ_MODE = "r"
EOL = "\n"
XML_HEADER = "<?xml version=\"1.0\" encoding=\"utf-8\"?>" + 2 * EOL
XML_FILE_EXTENSION = FILE_EXTENSION_SEPARATOR + "xml"
NEWSGROUPS_CORPORA_FIELD_SEPARATOR = ":"
SOLR_XML_ADD_OPEN_TAG = "<add>"
SOLR_XML_ADD_CLOSE_TAG = "</add>"
SOLR_XML_DOCUMENT_OPEN_TAG = "<doc>"
SOLR_XML_DOCUMENT_CLOSE_TAG = "</doc>"
SOLR_XML_FIELD_OPEN_TAG = "<field name=\"" + REPLACE_MASK + "\">"
SOLR_XML_FIELD_CLOSE_TAG = "</field>"
MESSAGE_FIELD_NAME_INDEX = 0
MESSAGE_FIELD_VALUE_INDEX = 1
XML_CHARS_TO_ESCAPE_LIST = ["&", "<", ">", "'", "\""]
XML_ESCAPE_DICTIONARY = {"&":"&amp;", "<":"&lt;", ">":"&gt;", "'":"&apos;", "\"":"&quot;"}
SOLR_SCHEMA_STATIC_FIELD_NAMES = ("Path", "From", "Newsgroups", "Subject", "Message-ID", "Date", "Organization", "Lines", "Sender", "References", "Xref", "Article-I.D.", "Expires", "Followup-To", "Keywords", "Distribution", "Approved", "Supersedes", "Originator", "Content-Type", "X-Newsreader", "Summary")
SOLR_SCHEMA_DYNAMIC_FIELDS = ("Reply-To", "Posting-Host", "Posting-User")
MESSAGE_TEXT_FIELD_NAME = "text"
MESSAGE_LINE_FIELD_NAME = "Lines"
MESSAGE_IDENTIFIER_FIELD_NAME = "id"
DECODE_ERROR_LOG = REPLACE_MASK + " could not be decoded"
EMPTY_STRING = ""
BACKUP_SYMBOL = "~"
LINUX_PATH_SEPARATOR = "/"
CDATA_OPEN_TAG = "<![CDATA["
CDATA_CLOSE_TAG = "]]>"
NEWSGROUPS_CORPORA_FIELD_NAME_LIST = ["Path", "From", "Newsgroups", "Subject", "Message-ID", "Date", "Lines", "Organization"]

CONTROL_CHARS_TO_IGNORE = {}
for i in range(1, 10):
    CONTROL_CHARS_TO_IGNORE[i] = None
for i in range(11, 32):
    CONTROL_CHARS_TO_IGNORE[i] = None
