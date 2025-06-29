"""
This module provides functions for generating and comparing SHA-1 hashes of files.
"""

import hashlib
from typing import Optional


def add_file_to_hash(file_name: str, chunk_size: int = 1024) -> str:
    """
    Generates a SHA-1 hash for a file by reading it in fixed-size chunks.

    Args:
        file_name: Path to the file to be hashed.
        chunk_size: Number of bytes to read per chunk.

    Returns:
        Hexadecimal SHA-1 digest string.

    Raises:
        ValueError: If file cannot be read.
    """
    hash_obj = hashlib.sha1()
    try:
        with open(file_name, "rb") as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        raise ValueError(f"Unable to read file '{file_name}': {e}") from e


def validate_hash_file(file_one: str, file_two: str, chunk_size: int = 1024) -> bool:
    """
    Compares SHA-1 hashes of two files.

    Args:
        file_one: Path to first file.
        file_two: Path to second file.
        chunk_size: Number of bytes to read per chunk.

    Returns:
        True if the files are identical (hashes match), False otherwise.
    """
    file_one_hash = add_file_to_hash(file_one, chunk_size)
    file_two_hash = add_file_to_hash(file_two, chunk_size)
    return file_one_hash == file_two_hash


def main(
    file_one: Optional[str] = "file1.txt",
    file_two: Optional[str] = "file2.txt",
    chunk_size: int = 1024,
):
    """
    Main entry point for script execution.
    Compares hashes of two files and prints the result.
    """
    try:
        match = validate_hash_file(file_one, file_two, chunk_size)
        if match:
            print("The files are identical (matching hashes).")
        else:
            print("The files are different (hashes are not matching).")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
