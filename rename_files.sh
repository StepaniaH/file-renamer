#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory="$1"

# Change to the specified directory
cd "$directory" || exit 1

# Prompt for the rename format
read -p "Enter the rename format: " rename_prefix

# Initialize the counter variable
counter=1

# Iterate through the .mp4 files in the directory
for file in *.mp4; do
    # Check if the file exists (to handle the case when no .mp4 files are found)
    if [ -e "$file" ]; then
        # Generate the new file name
        new_file_name=$(printf "${rename_prefix}-%02d.mp4" $counter)
        
        # Rename the file
        mv "$file" "$new_file_name"
        
        # Increment the counter
        ((counter++))
    fi
done

# Print a success message
echo "Renamed files successfully."
