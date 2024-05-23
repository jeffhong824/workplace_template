"""
Module Description:

This module, `generate_tree_structure`, generates the tree structure of a specified directory
and outputs it to a specified file. It is designed to provide a visual representation of the 
directory hierarchy, making it easier to understand the organization of files and folders.

Features:
- Recursively traverse the directory to build the tree structure.
- Customize the output file name and location.
- Default to the current directory and 'structure.md' if no arguments are provided.

Usage:
To generate the tree structure of the current directory and output it to 'structure.md':
    python generate_tree_structure.py

To generate the tree structure of a specified directory and output it to 'structure.md' in the same directory:
    python generate_tree_structure.py path/to/your/folder

To generate the tree structure of a specified directory and output it to a specified file:
    python generate_tree_structure.py path/to/your/folder --output_file path/to/output/file.md

Arguments:
- `start_path` (str): The starting directory path to generate the tree structure. Defaults to the current directory.
- `output_file` (str): The output file path. Defaults to 'structure.md' in the input directory.

Example:
    python generate_tree_structure.py /home/user/project --output_file /home/user/project_structure.md

Author: jeffhong824 (tchung)
Version: 1.0.0
Date: 2024-05-21
"""


import os
import argparse
from typing import Any

def generate_tree_structure(start_path: str = '.', output_file: str = 'structure.md') -> None:
    """
    Generate the tree structure of the specified directory and output to the specified file.

    Args:
        start_path (str): The starting directory path to generate the tree structure. Defaults to the current directory.
        output_file (str): The output file path. Defaults to 'structure.md'.
    """
    def tree(dir_path: str, prefix: str = '') -> None:
        """
        Recursively generate the tree structure of the directory.

        Args:
            dir_path (str): The current directory path being processed.
            prefix (str): The prefix used to control indentation and lines in the tree structure.
        """
        contents = os.listdir(dir_path)
        pointers = ['├── '] * (len(contents) - 1) + ['└── ']
        for pointer, path in zip(pointers, contents):
            full_path = os.path.join(dir_path, path)
            print(prefix + pointer + path)
            if os.path.isdir(full_path):
                extension = '│   ' if pointer == '├── ' else '    '
                tree(full_path, prefix + extension)

    with open(output_file, 'w', encoding='utf-8') as f:
        import sys
        sys.stdout = f
        print(".")
        tree(start_path)

def parse_args() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Generate the tree structure of the specified directory and output to the specified file.")
    parser.add_argument(
        'input_folder',
        type=str,
        nargs='?',
        default=None,
        help="The starting directory path to generate the tree structure. Defaults to the current directory."
    )
    parser.add_argument(
        '--output_file',
        type=str,
        default=None,
        help="The output file path. Defaults to 'structure.md' in the input directory."
    )
    return parser.parse_args()

def main() -> None:
    """
    Main function to handle input and generate the tree structure.
    """
    args = parse_args()

    if args.input_folder is None:
        print("Choose an option to generate the tree structure:")
        print("1. Generate the tree structure of the current directory and output to structure.md in the current directory.")
        print("2. Generate the tree structure of the specified directory and output to structure.md in the specified directory.")
        print("3. Generate the tree structure of the specified directory and output to the specified file.")

        choice = input("Enter the number of your choice: ").strip()

        if choice == '1':
            generate_tree_structure()
        elif choice == '2':
            folder = input("Enter the path to the directory: ").strip()
            generate_tree_structure(start_path=folder, output_file=os.path.join(folder, 'structure.md'))
        elif choice == '3':
            folder = input("Enter the path to the directory: ").strip()
            output_file = input("Enter the path to the output file: ").strip()
            generate_tree_structure(start_path=folder, output_file=output_file)
        else:
            print("Invalid choice. Exiting.")
    else:
        input_folder = args.input_folder
        output_file = args.output_file or os.path.join(input_folder, 'structure.md')
        generate_tree_structure(start_path=input_folder, output_file=output_file)

if __name__ == "__main__":
    main()
