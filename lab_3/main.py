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
        action = input("\nChoose action [C - Create, U - Update, D - Delete, P - Print, S - Save, E - Exit]: ").strip().upper()
        
        if action == "C":
            print("Add New Student")
            name = input("Enter student name: ").strip()
            phone = input("Enter student phone: ").strip()
            group = input("Enter student group: ").strip()
            student = Student(name=name, phone=phone, group=group)
            student_list.add_student(student)
            print("Student added successfully.")
        
        elif action == "U":
            print(" Update Student Information")
            name = input("Enter the name of the student to update: ").strip()
            student = student_list.find_student(name)
            if student:
                print(f"Found student: {student}")
                new_name = input("Enter new name (or press Enter to keep current): ").strip()
                new_phone = input("Enter new phone (or press Enter to keep current): ").strip()
                new_group = input("Enter new group (or press Enter to keep current): ").strip()
                success = student_list.update_student(name, new_name=new_name, new_phone=new_phone, new_group=new_group)
                if success:
                    print("Student updated successfully.")
                else:
                    print("Failed to update student.")
            else:
                print("Student not found.")
        
        elif action == "D":
            print("Delete Student")
            name = input("Enter the name of the student to delete: ").strip()
            success = student_list.delete_student(name)
            if success:
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        
        elif action == "P":
            print("List of Students:")
            student_list.print_all_students()
        
        elif action == "S":
            student_list.save_students(file_name)
            print("Students saved successfully.")
        
        elif action == "E":
            student_list.save_students(file_name)
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
