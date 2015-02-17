#!/bin/sh

DIR="$( cd "$( dirname "$0" )" && pwd )"
for folder in $1/*
do
    for file in $folder/*
    do
        python3 $DIR/../python/generate_sorl_xml.py "$file" "$2"
    done
done
