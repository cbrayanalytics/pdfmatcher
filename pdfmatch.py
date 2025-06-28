"""
module docstring here
"""

import hashlib


def add_file_to_hash(file_name, chunk_size):
    """
    hash out file by reading chunk_size at a time.
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


def validate_hash_file(file_one, file_two):
    """
    Validate hexdigest objects to confirm if they are same or not
    """

    file_one_hash = add_file_to_hash(file_one, 1024)
    file_two_hash = add_file_to_hash(file_two, 1024)

    print(f"File one: {file_one_hash},\n File two: {file_two_hash}")

    if file_one_hash == file_two_hash:
        print("The files are identical (matching hashes).")
        return
    print("The files are different (hashes are not matching).")


def main():
    """
    Run validate_hash_file
    """
    validate_hash_file("file1.txt", "file2.txt")


if __name__ == "__main__":
    main()
