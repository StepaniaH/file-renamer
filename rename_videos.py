import os
import sys
import datetime
import re

class RenameFilesAsDate:
    def __init__(self, root_directory):
        self.root_directory = os.path.expanduser(root_directory)
        self.error_files = {}

    def rename_files(self):
        current_date = datetime.datetime.now().strftime("%m%d")
        self._process_directory(self.root_directory, current_date)

        if self.error_files:
            print("The following files could not be renamed:")
            for original_path in self.error_files:
                print(original_path)

    def _process_directory(self, directory, current_date):
        folder_name = os.path.basename(directory)
        video_extensions = ('.mp4', '.avi', '.mov')

        count = 1

        for entry in os.listdir(directory):
            entry_path = os.path.join(directory, entry)

            if os.path.isfile(entry_path):
                if entry.lower().endswith(video_extensions):
                    base_name = os.path.splitext(entry)[0]
                    new_name = f"{folder_name}-{current_date}-{count:02d}{os.path.splitext(entry)[1]}"
                    new_path = os.path.join(directory, new_name)

                    os.rename(entry_path, new_path)
                    count += 1
                else:
                    self.error_files[entry_path] = "File is not a video"

            elif os.path.isdir(entry_path):
                self._process_directory(entry_path, current_date)

def main():
    if len(sys.argv) != 2:
        print("Usage: python rename_files.py <directory>")
        sys.exit(1)

    root_directory = sys.argv[1]

    renamer = RenameFilesAsDate(root_directory)
    renamer.rename_files()

if __name__ == '__main__':
    main()
