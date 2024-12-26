import unittest
from unittest.mock import patch
from io import StringIO
import sys
from lab_2 import students, add_student, delete_student, update_student, print_all_students

class TestStudentList(unittest.TestCase):
    def setUp(self):
        students.clear()

    @patch('builtins.input', side_effect=["John", "123456789", "CS-101"])
    def test_add_student(self, mock_input):
        add_student()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['name'], "John")
        self.assertEqual(students[0]['phone'], "123456789")
        self.assertEqual(students[0]['group'], "CS-101")

    @patch('builtins.input', return_value="Jane")
    def test_delete_student(self, mock_input):
        students.append({"name": "Jane", "phone": "987654321", "group": "CS-102"})
        delete_student()
        self.assertEqual(len(students), 0)

    @patch('builtins.input', side_effect=["Ivan","Ivan", "444999666", "CS-104"])
    def test_update_student(self, mock_input):
        students.append({"name": "Alice", "phone": "111222333", "group": "CS-103"})
        update_student()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['name'], "Alice")
        self.assertEqual(students[0]['phone'], "444555666")
        self.assertEqual(students[0]['group'], "CS-104")

    def test_print_all_students(self):
        students.append({"name": "Michael", "phone": "321321321", "group": "CS-204"})
        captured_output = StringIO()
        original_stdout = sys.stdout  
        sys.stdout = captured_output  
        try:
            print_all_students()
        finally:
            sys.stdout = original_stdout  
        self.assertIn("Michael", captured_output.getvalue())

if __name__== '__main__':
    unittest.main()