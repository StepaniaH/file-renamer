# Recursive Media File Renamer

A Python script for recursively renaming video and image files within directories using a consistent date-based pattern.

## Features

- Recursively processes all subdirectories
- Renames files to `foldername-MMDD-NN` format
- Supports common video formats (.mp4, .avi, .mov, .mkv, .wmv)
- Supports common image formats (.jpg, .jpeg, .png, .gif)
- Maintains existing renamed files (won't rename twice)
- Provides dry-run mode for preview
- Allows filtering by file type

## Usage

Basic usage:
```bash
python rename_files.py <directory>
```

Additional options:
```bash
# Only rename video files
python rename_files.py <directory> --type video

# Only rename image files
python rename_files.py <directory> --type image

# Preview changes without renaming
python rename_files.py <directory> --dry-run
```

## File Naming Pattern

Files are renamed to: `<folder_name>-<current_date>-<number>`

For example:
- If the folder name is "Videos"
- Current date is December 16
- It's the first file

The result will be: `Videos-1216-01.mp4`

## Error Handling

- The script will skip already renamed files
- A summary of files that could not be renamed will be displayed at the end
- File name conflicts are automatically resolved by continuing the sequence number

## Requirements

- Python 3.x
- No additional dependencies required

# Others

This README is worte by `anthropic/claude-3.5-sonnet`.
