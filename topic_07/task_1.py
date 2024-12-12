class Person:
    def __init__(self, name, age):
        """Ініціалізація атрибутів об'єкта."""
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(f"Ім'я: {person.name}, Вік: {person.age}")



class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        """Повертає текстове представлення об'єкта для користувача."""
        return f"Книга: '{self.title}' Автор: {self.author}"

book = Book("1984", "George Orwell")
print(book) 



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        """Повертає офіційне представлення об'єкта."""
        return f"Point(x={self.x}, y={self.y})"

point = Point(2, 3)
print(repr(point))  


class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __eq__(self, other):
        """Перевіряє рівність об'єктів."""
        return self.model == other.model and self.year == other.year


car1 = Car("Tesla", 2020)
car2 = Car("Tesla", 2020)
car3 = Car("BMW", 2019)

print(car1 == car2)  
print(car1 == car3)  



class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Додає два об'єкти класу Vector."""
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  
print(v3)  
