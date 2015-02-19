#!/usr/bin/env python3


import sys
from document import Document
from persistence import Persistence
from const import XML_FILE_EXTENSION


document = Persistence.get_document_from_file(sys.argv[1])
if (document is not None):
    Persistence.document_to_solr_xml(document, sys.argv[2] + document.identifier + XML_FILE_EXTENSION)
