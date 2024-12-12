import logging
from operations import get_number, get_operation
from functions import sum, sub, mult, div

logging.basicConfig(
    filename="calc.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def calculation(a):
    while True:
        b = get_number("Введіть друге число: ")
        act = get_operation()

        try:
            match act:
                case "+":
                    a = sum(a, b)
                case "-":
                    a = sub(a, b)
                case "*":
                    a = mult(a, b)
                case "/":
                    a = div(a, b)
        except ValueError as e:
            logging.error(f"Помилка: {e}")
            print(f"Помилка: {e}")
            continue

        print(f"\nПоточний результат = {a}")
        logging.info(f"Поточний результат = {a}")

        again = input("Бажаєте продовжити? (так/ні): ").lower()
        if again != "так":
            logging.info("Завершення роботи калькулятора.")
            print("Дякуємо за використання калькулятора!")
            break

a = get_number("Введіть перше число: ")
calculation(a)
