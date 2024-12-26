from typing import List
from student import Student
import csv

class StudentList:
    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, student: Student):
        self.students.append(student)
        self.students.sort(key=lambda s: s.name)
        print("Student has been added.")

    def delete_student(self, name: str):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print("Student has been deleted.")
                return
        print("Student not found.")

    def update_student(self, name: str, new_name: str = None, new_phone: str = None, new_group: str = None):
        for student in self.students:
            if student.name == name:
                if new_name:
                    student.name = new_name
                if new_phone:
                    student.phone = new_phone
                if new_group:
                    student.group = new_group
                self.students.sort(key=lambda s: s.name)
                print("Student information has been updated.")
                return
        print("Student not found.")

    def print_all_students(self):
        if not self.students:
            print("The list of students is empty.")
            return
        for student in self.students:
            print(student)

    def import_students(self, file_name: str):
        try:
            with open(file_name, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(name=row.get("name"), phone=row.get("phone"), group=row.get("group"))
                    self.add_student(student)
            print("Students imported successfully.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Starting with an empty list.")
        except csv.Error as e:
            print(f"CSV error: {e}")
        except Exception as e:
            print(f"Error importing students: {e}")

    def save_students(self, file_name: str):
        try:
            with open(file_name, mode="w", encoding="utf-8", newline="") as file:
                fieldnames = ["name", "phone", "group"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student in self.students:
                    writer.writerow({"name": student.name, "phone": student.phone, "group": student.group})
            print(f"Students saved to '{file_name}'.")
        except Exception as e:
            print(f"Error saving students: {e}")
