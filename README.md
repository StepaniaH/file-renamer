# Simple Recursive Video File Renamer

This is a simple Python script for recursively renaming video files within a directory.

## Usage

Run the script using the following command: `python rename_videos.py <target_root_directory>`

Then, the video files will be renamed to the format: `<folder_name>-<current_date (MMDD)>-<incremental_number>`

Finally, the script will output a summary of files that could not be renamed.

For example, if the folder name is `MyVideos`, the current date is February 1, 2024, and it’s the first video file, the new name will be: `MyVideos-0201-01.mp4`

