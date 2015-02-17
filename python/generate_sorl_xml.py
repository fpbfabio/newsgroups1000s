#!/usr/bin/env python3


import sys
from message import Message
from persistence import Persistence
from const import XML_FILE_EXTENSION


message = Persistence.get_message_from_file(sys.argv[1])
if (message is not None):
    Persistence.message_to_solr_xml(message, sys.argv[2] + message.identifier + XML_FILE_EXTENSION)
