#newsgroups1000s

A program that transforms the 20000 newsgroups corpora available on the web into xml files compatible with Apache Solr. It is useful mainly to data science researchers


##Requirements

*python3 command line tool set up
*tested only on linux, uses bash files

##How to use

1. Download the 20000 newsgroups data set available on the web
2. Clone this repository to a folder in your computer
3. Run the bash file program.sh passing two parameters the path to the 20000 newsgroups files root folder and the path to the xml files destination folder
4. Set up a core in Solr with the schema.xml file present in this repository