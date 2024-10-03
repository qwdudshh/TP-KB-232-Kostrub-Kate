def input_values():
    a = int(input("Введіть а: "))
    b = int(input("Введіть b: "))
    c = int(input("Введіть c: "))
    return a, b, c

def disc(a, b, c):
    result = (b*b - 4*a*c)
    return result

value1, value2, value3 = input_values()
result = disc(value1, value2, value3)

print("Результат =", result)


