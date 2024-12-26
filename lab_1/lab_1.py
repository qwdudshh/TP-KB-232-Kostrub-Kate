
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

list = [
    {"name":"Bob", "phone":"0631234567", "email":"bob@gmail.com", "group":"1"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@gmail.com", "group":"2"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon@gmail.com", "group":"1"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak@gmail.com", "group":"1"}
]

def printAllList():
    for elem in list:
        strForPrint = f"Student name is {elem['name']}, Phone is {elem['phone']}, Email is {elem['email']}, Group is {elem['group']}"
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "email": email, "group": group}

    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print(f"Deleted position {deletePosition}")
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    student = next((item for item in list if item["name"] == name), None)
    
    if student:
        print(f"Updating information for {name}:")
        student["phone"] = input(f"Enter new phone (current: {student['phone']}): ") or student["phone"]
        student["email"] = input(f"Enter new email (current: {student['email']}): ") or student["email"]
        student["group"] = input(f"Enter new group (current: {student['group']}): ") or student["group"]
        print(f"Information for {name} has been updated.")
    else:
        print(f"Student {name} not found.")

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  E exit ]: ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exiting program.")
                break
            case _:
                print("Wrong choice")

main()
