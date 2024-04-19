#!/bin/bash

for file in $(ls redirect/); do
	source="redirect/$file"
	basename=$(basename "$file" .txt)
	echo " Processing file for duplicates $file"
	destination="unique_redirects/$basename.txt"
	cat $source | sort | uniq > $destination
done
