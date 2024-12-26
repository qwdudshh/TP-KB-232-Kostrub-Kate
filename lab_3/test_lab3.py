import unittest
from student import Student
from student_list import StudentList
import os
import csv

class TestStudentList(unittest.TestCase):

    def setUp(self):
        self.student_list = StudentList()
        self.test_file = "test_students.csv"

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_student(self):
        student = Student(name="John Doe", phone="123456789", group="A")
        self.student_list.add_student(student)
        self.assertEqual(len(self.student_list.students), 1)
        self.assertEqual(self.student_list.students[0].name, "John Doe")

    def test_delete_student(self):
        student = Student(name="John Doe", phone="123456789", group="A")
        self.student_list.add_student(student)
        self.student_list.delete_student("John Doe")
        self.assertEqual(len(self.student_list.students), 0)

    def test_update_student(self):
        student = Student(name="John Doe", phone="123456789", group="A")
        self.student_list.add_student(student)
        self.student_list.update_student("John Doe", new_name="Jane Doe", new_phone="987654321", new_group="B")
        updated_student = self.student_list.students[0]
        self.assertEqual(updated_student.name, "Jane Doe")
        self.assertEqual(updated_student.phone, "987654321")
        self.assertEqual(updated_student.group, "B")

    def test_import_students(self):
        with open(self.test_file, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "phone", "group"])
            writer.writerow(["John Doe", "123456789", "A"])
            writer.writerow(["Jane Smith", "987654321", "B"])

        self.student_list.import_students(self.test_file)
        self.assertEqual(len(self.student_list.students), 2)
        self.assertEqual(self.student_list.students[0].name, "Jane Smith")
        self.assertEqual(self.student_list.students[1].name, "John Doe")

    def test_save_students(self):
        student1 = Student(name="John Doe", phone="123456789", group="A")
        student2 = Student(name="Jane Smith", phone="987654321", group="B")
        self.student_list.add_student(student1)
        self.student_list.add_student(student2)

        self.student_list.save_students(self.test_file)

        with open(self.test_file, "r", encoding="utf-8") as file:
            content = file.readlines()
        self.assertEqual(len(content), 3)  # Header + 2 students
        self.assertIn("John Doe,123456789,A\n", content[1:])
        self.assertIn("Jane Smith,987654321,B\n", content[1:])

if __name__ == "__main__":
    unittest.main()
