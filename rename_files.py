import os
import re
import sys

if len(sys.argv)!= 2:
    print("Usage: python rename_files.py <directory>")
    sys.exit(1)

directory = sys.argv[1]

# Set the folder path to the current working directory
folder_path = directory 

# Set the regular expression pattern to match any.mp4 file
pattern = r'^.*\.mp4$'

# Set the rename format
rename_prefix = input("Enter the rename format: ")
rename_format = f'{rename_prefix}-{{:02d}}.mp4'

# Initialize the counter variable
counter = 1

# Iterate through the files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file matches the pattern
    if re.match(pattern, file_name):
        # Rename the file using the rename format
        new_file_name = rename_format.format(counter)
        # Rename the file
        os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
        # Increment the counter
        counter += 1

# Print a success message
print("Renamed files successfully.")

