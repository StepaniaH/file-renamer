import os
from typing import Dict, Optional, List
from ..utils.file_utils import FileTypes

class FileRenamer:
    def __init__(self, directory: str):
        self.directory = os.path.expanduser(directory)
        self.error_files: Dict[str, str] = {}
        self.file_types = FileTypes()

    def rename_files(self, file_type: str = 'all', dry_run: bool = False) -> None:
        """
            Rename files
            Args:
                file_type: File type ('all', 'video', 'image')
                dry_run: Confirm whether it is preview mode
        """
        folder_name = os.path.basename(self.directory)
        files_to_rename = self._get_files_to_rename(file_type)
        
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

    def _get_files_to_rename(self, file_type: str) -> List[str]:
        """
            Get the list of the files which need to be rename
            Args:
                file_type: File type filter
            Returns:
                List of eligible files
        """
        supported_extensions = self.file_types.get_supported_extensions(file_type)

        return [
            f for f in os.listdir(self.directory)
            if (os.path.isfile(os.path.join(self.directory, f)) and
                f.lower().endswith(supported_extensions))
        ]

    def _perform_rename(self, old_path: str, new_path: str) -> None:
        """
            Perform rename operation
        """
        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {os.path.basename(old_path)} -> {os.path.basename(new_path)}")
        except OSError as e:
            self.error_files[old_path] = f"Rename failed: {str(e)}"
