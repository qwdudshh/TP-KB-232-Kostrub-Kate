from student import Student
from student_list import StudentList
import sys

DEFAULT_FILE = "students.csv"

def main():
    student_list = StudentList()
    file_name = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FILE

    print(f"Using file: {file_name}")
    student_list.import_students(file_name)

    while True:
        action = input("Choose action [C - Create, U - Update, D - Delete, P - Print, S - Save, E - Exit]: ").strip().upper()
        if action == "C":
            name = input("Enter student name: ")
            phone = input("Enter student phone: ")
            group = input("Enter student group: ")
            student = Student(name=name, phone=phone, group=group)
            student_list.add_student(student)
        elif action == "U":
            name = input("Enter the name of the student to update: ")
            new_name = input("Enter new name (or press Enter to keep current): ")
            new_phone = input("Enter new phone (or press Enter to keep current): ")
            new_group = input("Enter new group (or press Enter to keep current): ")
            student_list.update_student(name, new_name=new_name, new_phone=new_phone, new_group=new_group)
        elif action == "D":
            name = input("Enter the name of the student to delete: ")
            student_list.delete_student(name)
        elif action == "P":
            student_list.print_all_students()
        elif action == "S":
            student_list.save_students(file_name)
        elif action == "E":
            student_list.save_students(file_name)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
