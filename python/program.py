import os
import sys
from threading import Thread
from persistence import Persistence


def execute_conversion(path, output_folder_path):
	for subdir, dir, file_list in os.walk(path):
		for file in file_list:
			document = Persistence.get_document_from_file(path + os.path.sep + str(file))
			Persistence.document_to_solr_xml(document, output_folder_path + document.identifier + ".xml")


input_root_dir = sys.argv[1]
output_root_dir = sys.argv[2]
is_the_same_root_dir = True
thread_list = []
thread_count = 0
for subdir, dir, file in os.walk(input_root_dir):
	if(not is_the_same_root_dir):
		thread_count += 1
		print(str(thread_count))
		thread = Thread(target=execute_conversion(str(subdir), output_root_dir))
		thread.start()
	else:
		is_the_same_root_dir = False
for thread in thread_list:
	thread.join()