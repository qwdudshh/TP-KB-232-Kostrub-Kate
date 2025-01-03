def values():
    a = int(input("Введіть a: "))
    b = int(input("Введіть b: "))
    return a, b

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
    if b != 0:
        return a / b
    else:
        return "Ділення на нуль!"

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
