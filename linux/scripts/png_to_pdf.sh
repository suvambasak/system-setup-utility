
# Install img2pdf
# pip install img2pdf



#!/bin/bash

# Check if the directory argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

# Assign the directory argument to a variable
directory="$1"

# Change to the specified directory
cd "$directory" || { echo "Directory not found: $directory"; exit 1; }

# Loop through all PNG files in the directory and convert them to PDF
for img in *.png; do
    base_name="${img%.png}"
    img2pdf "$img" -o "$base_name.pdf"
    echo "> $img to $base_name.pdf"
    rm "$img"
done

echo "Conversion complete."
