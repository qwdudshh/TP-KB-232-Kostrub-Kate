import unittest
import csv
import tempfile
import os
from lab_2 import load_from_csv, save_to_csv, directory

class TestStudentDirectory(unittest.TestCase):

    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False, mode='w', newline='', encoding='utf-8')
        self.test_filename = self.test_file.name
        self.test_file.close()

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_load_from_csv(self):
        data = [
            {"name": "John", "phone": "1234567890", "email": "john@example.com", "group": "556"},
            {"name": "Jane", "phone": "9876543210", "email": "jane@example.com", "group": "456"}
        ]
        
        with open(self.test_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "group"])
            writer.writeheader()
            writer.writerows(data)

        load_from_csv(self.test_filename)
        self.assertEqual(len(directory), 2)
        self.assertEqual(directory[0]["name"], "John Doe")

    def test_save_to_csv(self):
        directory.append({"name": "Charlie", "phone": "5555555555", "email": "charlie@example.com", "group": "758"})
        save_to_csv(self.test_filename)

        with open(self.test_filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["name"], "Charlie Brown")

if __name__ == "__main__":
    unittest.main()
