import csv
from sys import argv

DEFAULT_FILE = "students.csv"
students = []

def print_all_students():
    if not students:
        print("The list of students is empty.")
        return
    for student in students:
        print(f"Name: {student['name']}, Phone: {student['phone']}, Group: {student['group']}")

def add_student():
    name = input("Enter student name: ") 
    phone = input("Enter student phone: ") 
    group = input("Enter student group: ")
    new_student = {"name": name, "phone": phone, "group": group}

    insert_position = 0
    for student in students:
        if name > student["name"]:
            insert_position += 1
        else:
            break

    students.insert(insert_position, new_student)
    print("Student has been added.")

def delete_student():
    name = input("Enter the name of the student to delete: ")
    for i, student in enumerate(students):
        if student["name"] == name:
            del students[i]
            print("Student has been deleted.")
            return
    print("Student not found.")

def update_student():
    name = input("Enter the name of the student to update: ")
    for i, student in enumerate(students):
        if student["name"] == name:
            print(f"Current Info - Name: {student['name']}, Phone: {student['phone']}, Group: {student['group']}")

            student["name"] = input("Enter new name (or press Enter to keep current): ") or student["name"]
            student["phone"] = input("Enter new phone (or press Enter to keep current): ") or student["phone"]
            student["group"] = input("Enter new group (or press Enter to keep current): ") or student["group"]
           
            students.sort(key=lambda x: x["name"])
            print("Student information has been updated.")
            return
    print("Student not found.")

def import_students(file_name):
    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            if not rows:
                print(f"The file '{file_name}' is empty.")
                return

            for row in rows:
                students.append({
                    "name": row.get("name"),
                    "phone": row.get("phone"),
                    "group": row.get("group"),
                })
        
        students.sort(key=lambda x: x["name"])
        print("Students imported successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found. Starting with an empty list.")
    except csv.Error as e:
        print(f"CSV error: {e}")
    except Exception as e:
        print(f"Error importing students: {e}")

def save_students(file_name):
    try:
        with open(file_name, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["name", "phone", "group"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
        print(f"Students saved to '{file_name}'.")
    except Exception as e:
        print(f"Error saving students: {e}")

def main():
    file_name = argv[1] if len(argv) > 1 else DEFAULT_FILE
    print(f"Using file: {file_name}")
    import_students(file_name)

    while True:
        action = input("Choose action [C - Create, U - Update, D - Delete, P - Print, E - Exit]: ").strip().upper()
        match action:
            case "C":
                add_student()
            case "U":
                update_student()
            case "D":
                delete_student()
            case "P":
                print_all_students()
            case "E":
                save_students(file_name)
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
