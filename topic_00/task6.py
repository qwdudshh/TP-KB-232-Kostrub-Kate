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

def input_values():
    a = int(input("Введіть a: "))
    b = int(input("Введіть b: "))
    return a, b

def input_op():
    op = input("Оберіть бажану операцію (+, -, *, /): ")
    return op

def operations(a, b, op):
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = minus(a, b)
    elif op == "*":
        result = multipl(a, b)
    elif op == "/":
        result = division(a, b)
    else:
        result = "Помилка введення"
    
    print("Результат:", result)


a, b = input_values()    
operation = input_op()  
operations(a, b, operation) 
