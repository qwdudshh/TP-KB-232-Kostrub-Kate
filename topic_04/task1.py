def values():
    while True:
        try:
            a = int(input("Введіть a: "))
            b = int(input("Введіть b: "))
            return a, b
        except ValueError:
            print("Помилка: введіть числові значення для a і b.")

def get_operation():
    op = input("Оберіть бажану операцію (+, -, *, /) або введіть 'exit' для виходу: ")
    return op

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multipl(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Помилка: ділення на нуль!"

while True:
    a, b = values()  
    operation = get_operation()
    
    if operation.lower() == "exit":
        print("Вихід з програми.")
        break

    match operation:
        case "+":
            result = add(a, b)
        case "-":
            result = minus(a, b)
        case "*":
            result = multipl(a, b)
        case "/":
            result = division(a, b)
        case _:
            result = "Невідома операція!"
    
    print("Результат:", result)
