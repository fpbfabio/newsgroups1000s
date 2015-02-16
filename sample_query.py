from urllib.request import urlopen
import json
connection = urlopen("http://localhost:8983/solr/select?q=video&wt=json")
str_connection = connection.readall().decode("utf-8");
response = json.loads(str_connection)
print (response["response"]["numFound"], "documents founded")
for document in response["response"]["docs"]:
	print(" Name = " + str(document["name"]))
