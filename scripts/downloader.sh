#!/bin/bash

# Check if the argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <urls_file>"
    exit 1
fi

# Assign the provided argument to the variable
urls_file="$1"

# Check if the file exists
if [ ! -f "$urls_file" ]; then
    echo "Error: File $urls_file not found."
    exit 1
fi

# Loop through each URL in the file
while IFS= read -r url; do
    echo "Downloading $url..."
    wget "$url"
    if [ $? -eq 0 ]; then
        echo "Download of $url successful."
    else
        echo "Failed to download $url."
    fi
done < "$urls_file"
