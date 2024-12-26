import argparse

from ..core.renamer import FileRenamer


def create_parser() -> argparse.ArgumentParser:
    """
    Create a command line argument parser
    """
    parser = argparse.ArgumentParser(description="Rename files based on folder name")
    parser.add_argument("directory", help="Directory containing files to rename")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without actually renaming",
    )
    return parser


def main() -> None:
    """
    Command line entry function
    """
    parser = create_parser()
    args = parser.parse_args()

    renamer = FileRenamer(args.directory)
    renamer.rename_files(args.dry_run)


if __name__ == "__main__":
    main()
