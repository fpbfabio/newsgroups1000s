#newsgroups1000s

A program that transforms the 20000 newsgroups corpora available on the web into xml files compatible with Apache Solr. It is useful mainly to data science researchers


##Requirements

* python3 command line tool set up
* Tested only on linux, uses bash files

##How to use

```
./program.sh <path-to-newsgroups-root-folder> <path-destination-folder>
```

###Detailed steps
1. Download the 20000 newsgroups data set available on the web
2. Clone this repository to a folder in your computer
3. Run the bash file program.sh passing two parameters the path to the 20000 newsgroups files root folder and the path to the xml files destination folder (as in the above example code)
4. Set up a core in Solr with the schema.xml file present in this repository
5. Post the xml files to that core
6. Start making searches!

##Important information

The messages saying "XXXX could not be decoded" are normal and expected, some files in the newsgroups collection have codification issues and cannot be read using the python file handling functions. You should end up with 19926 generated xml files

In the schema.xml file implemented there is only one field with indexed=true, that is the field "everything" which receives the commonly most relevant fields of each document through copyField. So make sure to specify the "everything" field when submiting queries to Solr when using the schema.xml file provided in this repository. Also, you may choose to customize this file.

The program takes around 30 minutes to complete (tested in a i5 ssd machine)
