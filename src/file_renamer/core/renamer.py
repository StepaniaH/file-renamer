import os
from typing import Dict, Optional

class FileRenamer:
    def __init__(self, directory: str):
        self.directory = os.path.expanduser(directory)
        self.error_files: Dict[str, str] = {}

    def rename_files(self, dry_run:bool = False) -> None:
        """
            The basic rename function: only rename the files as the format "<directory name>-num"
        """
        folder_name = os.path.basename(self.directory)
        files_to_rename = self._get_files_to_rename()
        
        if files_to_rename:
            count = 1
            total_files = len(files_to_rename)
            num_digits = len(str(total_files))

            for filename in sorted(files_to_rename):
                file_path = os.path.join(self.directory, filename)
                new_name = f"{folder_name}-{count:0{num_digits}d}{os.path.splitext(filename)[1].lower()}"
                new_path = os.path.join(self.directory, new_name)

                if dry_run:
                    print(f"Would rename: {filename} -> {new_name}")
                else:
                    self._perform_rename(file_path, new_path)
                count += 1

    def _get_files_to_rename(self) -> list:
        """
            Get the list of the files which need to be rename
        """
        return [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f))]

    def _perform_rename(self, old_path: str, new_path: str) -> None:
        """
            Perform rename operation
        """
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {os.path.basename(old_path)} -> {os.path.basename(new_path)}")
        except OSError as e:
            self.error_files[old_path] = f"Rename failed: {str(e)}"
