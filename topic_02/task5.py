import math

def input_values():
    a = int(input("Введіть a: "))
    b = int(input("Введіть b: "))
    c = int(input("Введіть c: "))
    return a, b, c

def disc(a, b, c):
    result = b * b - 4 * a * c
    return result

def find_num(a, b, c, result):
    if result > 0:
        num1 = (-b + math.sqrt(result)) / (2 * a)
        num2 = (-b - math.sqrt(result)) / (2 * a)
        print("Рівняння має два корені:", num1, num2)
    elif result == 0:
        num3 = -b / (2 * a)
        print("Рівняння має один корінь:", num3)
    else:
        print("Рівняння не має коренів")

value1, value2, value3 = input_values()
result = disc(value1, value2, value3)
print("Результат =", result)

find_num(value1, value2, value3, result)
