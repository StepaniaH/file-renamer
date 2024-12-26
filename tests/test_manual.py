import os
import shutil
import sys
from pathlib import Path

project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from src.file_renamer.core.renamer import FileRenamer


def setup_test_files():
    test_folder = Path(__file__).parent / "test_folder"
    test_folder.mkdir(exist_ok=True)

    structure = {
        "": [
            "image1.jpg",
            "video1.mp4",
        ],
        "subdir1": [
            "image2.png",
            "video2.avi",
        ],
        "subdir2": [
            "image3.jpg",
            "video3.mp4",
        ],
    }

    for dir_name, files in structure.items():
        current_dir = test_folder
        if dir_name:
            current_dir = test_folder / dir_name
            current_dir.mkdir(exist_ok=True)

        for filename in files:
            file_path = current_dir / filename
            if not file_path.exists():
                with open(file_path, "w") as f:
                    f.write(f"content for {filename}")


def cleanup_test_files():
    test_folder = Path(__file__).parent / "test_folder"
    if test_folder.exists():
        shutil.rmtree(test_folder)
        print("Test files cleaned up.")


def show_directory_structure(directory):
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, "").count(os.sep)
        indent = " " * 4 * level
        print(f"{indent}{os.path.basename(root) or 'test_folder'}/")
        for f in sorted(files):
            print(f"{indent}    {f}")


def main():
    try:
        setup_test_files()
        test_folder = str(Path(__file__).parent / "test_folder")
        renamer = FileRenamer(test_folder)

        print("\n=== Current Directory Structure ===")
        show_directory_structure(test_folder)

        recursive = (
            input("\nDo you want to process subdirectories? (yes/no): ").lower()
            == "yes"
        )

        for file_type in ["all", "video", "image"]:
            print(f"\n=== Testing {file_type.upper()} files ===")
            print(f"=== Dry Run Mode {'(Recursive)' if recursive else ''} ===")
            renamer.rename_files(file_type=file_type, dry_run=True, recursive=recursive)

        file_type = input("\nChoose file type to rename (all/video/image): ").lower()
        if file_type in ["all", "video", "image"]:
            response = input(
                "Do you want to proceed with the actual renaming? (yes/no): "
            )

            if response.lower() == "yes":
                print(
                    f"\n=== Performing Actual Rename for {file_type.upper()} files ==="
                )
                renamer.rename_files(
                    file_type=file_type, dry_run=False, recursive=recursive
                )

                print("\n=== Final Directory Structure ===")
                show_directory_structure(test_folder)
        else:
            print("Invalid file type selected.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

    finally:
        cleanup = input("\nDo you want to clean up test files? (yes/no): ")
        if cleanup.lower() == "yes":
            cleanup_test_files()


if __name__ == "__main__":
    main()
