import os
import tempfile
import unittest

from pdfmatch import add_file_to_hash, validate_hash_file


class TestFileHashing(unittest.TestCase):
    """
    Unit tests for file hashing and comparison functions.
    Tests include identical files, different files, and error handling.
    """

    def setUp(self):
        """
        Set up temporary files for testing.
        Create two identical files and one different.
        """
        self.temp1 = tempfile.NamedTemporaryFile(delete=False)
        self.temp2 = tempfile.NamedTemporaryFile(delete=False)
        self.temp3 = tempfile.NamedTemporaryFile(delete=False)
        self.temp1.write(b"Howdy mister!")
        self.temp2.write(b"Howdy mister!")
        self.temp3.write(b"How's it goin?")
        self.temp1.close()
        self.temp2.close()
        self.temp3.close()

    def tearDown(self):
        """
        Clean up temporary files after testing.
        """
        os.unlink(self.temp1.name)
        os.unlink(self.temp2.name)
        os.unlink(self.temp3.name)

    def test_hash_identical_files(self):
        """
        Test that the hash values of two identical files are equal.
        """
        hash1 = add_file_to_hash(self.temp1.name, 1024)
        hash2 = add_file_to_hash(self.temp2.name, 1024)
        self.assertEqual(hash1, hash2)

    def test_hash_different_files(self):
        """
        Test that the hash values of two different files are not equal.
        """
        hash1 = add_file_to_hash(self.temp1.name, 1024)
        hash3 = add_file_to_hash(self.temp3.name, 1024)
        self.assertNotEqual(hash1, hash3)

    def test_validate_hash_file_identical(self):
        """
        Test that validate_hash_file returns True for identical files.
        """
        self.assertTrue(validate_hash_file(self.temp1.name, self.temp2.name))

    def test_validate_hash_file_different(self):
        """
        Test that validate_hash_file returns False for different files.
        """
        self.assertFalse(validate_hash_file(self.temp1.name, self.temp3.name))

    def test_missing_file_raises(self):
        """
        Test that add_file_to_hash raises a ValueError for a missing file.
        """
        with self.assertRaises(ValueError):
            add_file_to_hash("nonexistent.txt", 1024)


if __name__ == "__main__":
    unittest.main()
