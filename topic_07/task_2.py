class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"


students = [
    Student("Anna", 21),
    Student("Bohdan", 19),
    Student("Iryna", 22),
    Student("Oleksii", 20),
    Student("Kateryna", 23),
    Student("Dmytro", 18),
    Student("Sofiia", 21),
    Student("Viktor", 25),
    Student("Maksym", 20),
    Student("Olha", 22),
    Student("Andrii", 19),
    Student("Yuliia", 24)
]

sort_criteria = input("Введіть критерій сортування (n - за ім'ям, a - за віком): ").strip().lower()

if sort_criteria == 'n':
    sorted_students = sorted(students, key=lambda student: student.name)
    print("\nСортування за іменем:")
elif sort_criteria == 'a':
    sorted_students = sorted(students, key=lambda student: student.age)
    print("\nСортування за віком:")
else:
    print("Неправильний критерій сортування. Використовується сортування за замовчуванням (за іменем).")
    sorted_students = sorted(students, key=lambda student: student.name)

for student in sorted_students:
    print(student)
