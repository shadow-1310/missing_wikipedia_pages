#!/bin/bash

for file in $(ls extracted/); do
	source="extracted/$file"
	basename=$(basename "$file" .xml)
	echo " Processing file $file"
	destination="redirect/$basename.txt"
	#echo "To destination $destination"
	cat $source | grep '<redirect title' | grep -o '"\([^"]*\)"' | sed 's/"//g' > $destination
done
