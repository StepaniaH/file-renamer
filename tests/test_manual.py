import os
import sys
from pathlib import Path

project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.file_renamer.core.renamer import FileRenamer

def setup_test_files():
    """
        Create test directory and diles
    """
    test_folder = Path(__file__).parent / "test_folder"
    test_folder.mkdir(exist_ok=True)
    
    test_files = ["test1.txt", "test2.txt", "test3.txt"]
    for file in test_files:
        file_path = test_folder / file
        if not file_path.exists():
            with open(file_path, "w") as f:
                f.write("test content")

def main():
    setup_test_files()
    
    test_folder = str(Path(__file__).parent / "test_folder")
    renamer = FileRenamer(test_folder)
    
    print("\n=== Dry Run Mode ===")
    renamer.rename_files(dry_run=True)
    
    response = input("\nDo you want to proceed with the actual renaming? (yes/no): ")
    
    if response.lower() == 'yes':
        print("\n=== Performing Actual Rename ===")
        renamer.rename_files(dry_run=False)
        
        print("\n=== Final Directory Contents ===")
        for file in os.listdir(test_folder):
            print(file)

if __name__ == "__main__":
    main()
