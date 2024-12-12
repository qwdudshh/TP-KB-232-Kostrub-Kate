students = [
    {"name": "Alice", "mark": 85},
    {"name": "Bob", "mark": 90},
    {"name": "Charlie", "mark": 78},
    {"name": "David", "mark": 92}
]

def print_students(students):
    for student in students:
        print(f"{student['name']} - {student['mark']}")

def sort_by_name(students):
    return sorted(students, key=lambda x: x["name"])

def sort_by_mark(students):
    return sorted(students, key=lambda x: x["mark"], reverse=True)

while True:
    sortingMethod = input("Select sorting method: Enter 'n - name' or 'm - mark' or 'p - print unsorted' or Enter 'exit' to stop program: ").lower()

    if sortingMethod == 'n':
        sorted_students = sort_by_name(students)
        print("Sorted by name:")
        print_students(sorted_students)

    elif sortingMethod == 'm':
        sorted_students = sort_by_mark(students)
        print("Sorted by mark:")
        print_students(sorted_students)

    elif sortingMethod == 'p':
        print("Unsorted list:")
        print_students(students)

    elif sortingMethod == 'exit':
        print("Exiting program.")
        break

    else:
        print("Invalid input. Please try again.")