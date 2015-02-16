#!/usr/bin/env python3


import sys
from utils import Utils
from message import Message

message = Utils.get_message_from_file(sys.argv[1])
Utils.message_to_solr_xml(message, sys.argv[2] + message.identifier + ".xml")
