class Student:
    def __init__(self, name: str, phone: str, group: str):
        self.name = name
        self.phone = phone
        self.group = group

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Group: {self.group}"