"""
Module Description:

This module contains unit tests for the generate_tree_structure.py script.
It provides tests to ensure that the generate_tree_structure function works
correctly under various conditions.

Usage:

To run the tests, use the following command:
    pytest test_generate_tree_structure.py

Test cases include:
- Verifying the generated tree structure for a directory with files and subdirectories.
- Verifying the generated tree structure for an empty directory.
- Additional edge cases to ensure robustness.

Author: jeffhong824 (tchung)
Version: 1.0.0
Date: 2024-05-21
"""


import os
import pytest
from generate_tree_structure import generate_tree_structure


@pytest.fixture
def setup_test_directory(tmp_path):
    """
    Setup a temporary directory for testing.

    Args:
        tmp_path: A pytest fixture that provides a temporary directory unique to the test invocation.

    Returns:
        The path to the temporary directory.
    """
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    (test_dir / "file1.txt").write_text("This is a test file.")
    (test_dir / "subdir").mkdir()
    (test_dir / "subdir" / "file2.txt").write_text("This is another test file.")
    return test_dir


def test_generate_tree_structure(setup_test_directory, tmp_path):
    """
    Test generate_tree_structure function.

    Args:
        setup_test_directory: The temporary directory for testing.
        tmp_path: A pytest fixture that provides a temporary directory unique to the test invocation.
    """
    output_file = tmp_path / "structure.md"
    generate_tree_structure(start_path=str(
        setup_test_directory), output_file=str(output_file))

    with open(output_file, 'r', encoding='utf-8') as f:
        output = f.read()

    expected_output = """
.
├── file1.txt
└── subdir
    └── file2.txt
"""
    assert expected_output.strip() in output.strip()


def test_generate_tree_structure_with_empty_directory(tmp_path):
    """
    Test generate_tree_structure function with an empty directory.

    Args:
        tmp_path: A pytest fixture that provides a temporary directory unique to the test invocation.
    """
    empty_dir = tmp_path / "empty_dir"
    empty_dir.mkdir()
    output_file = tmp_path / "structure.md"
    generate_tree_structure(start_path=str(empty_dir),
                            output_file=str(output_file))

    with open(output_file, 'r', encoding='utf-8') as f:
        output = f.read()

    expected_output = """
.
"""
    assert expected_output.strip() in output.strip()
