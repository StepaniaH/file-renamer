import os
import sys
from pathlib import Path

project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.file_renamer.core.renamer import FileRenamer

def setup_test_files():
    test_folder = Path(__file__).parent / "test_folder"
    test_folder.mkdir(exist_ok=True)
    
    test_files = {
        "image1.jpg": "image content",
        "image2.png": "image content",
        "video1.mp4": "video content",
        "video2.avi": "video content",
        "document.txt": "text content"
    }
    
    for filename, content in test_files.items():
        file_path = test_folder / filename
        if not file_path.exists():
            with open(file_path, "w") as f:
                f.write(content)

def main():
    setup_test_files()
    test_folder = str(Path(__file__).parent / "test_folder")
    renamer = FileRenamer(test_folder)
    
    for file_type in ['all', 'video', 'image']:
        print(f"\n=== Testing {file_type.upper()} files ===")
        print(f"=== Dry Run Mode ===")
        renamer.rename_files(file_type=file_type, dry_run=True)
    
    file_type = input("\nChoose file type to rename (all/video/image): ").lower()
    if file_type in ['all', 'video', 'image']:
        response = input("Do you want to proceed with the actual renaming? (yes/no): ")
        
        if response.lower() == 'yes':
            print(f"\n=== Performing Actual Rename for {file_type.upper()} files ===")
            renamer.rename_files(file_type=file_type, dry_run=False)
            
            print("\n=== Final Directory Contents ===")
            for file in os.listdir(test_folder):
                print(file)
    else:
        print("Invalid file type selected.")

if __name__ == "__main__":
    main()
