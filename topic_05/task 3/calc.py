from operations import get_number, get_operation
from functions import sum, sub, mult, div

def calculator():
    a = get_number("Введіть перше число: ")

    while True:
        operation = get_operation()

        b = get_number("Введіть друге число: ")

        try:
            match operation:
                case "+":
                    a = sum(a, b)
                case "-":
                    a = sub(a, b)
                case "*":
                    a = mult(a, b)
                case "/":
                    a = div(a, b)
        except ValueError as e:
            print(f"Помилка: {e}")
            continue

        print(f"Результат: {a}")

        again = input("Бажаєте продовжити? (так/ні): ").lower()
        if again != "так":
            break

calculator()
