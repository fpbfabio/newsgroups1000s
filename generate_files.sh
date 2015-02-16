#!/bin/sh
for file in $1/*
do
    for subfile in $file/*
    do
        python3 generate_sorl_xml.py "$subfile" "$2"
    done
done
