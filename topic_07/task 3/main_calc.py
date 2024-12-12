import logging
from calc import calculator
from operations import get_number, get_operation

logging.basicConfig(
    filename="calc.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    print("Ласкаво просимо до калькулятора!")
    calc = calculator()

    calc.result = get_number("Введіть початкове число: ")

    while True:
        operation = get_operation()
        number = get_number("Введіть число: ")

        try:
            result = calc.calculate(operation, number)
            print(f"\nПоточний результат: {result}")
        except ValueError as e:
            logging.error(f"Помилка: {e}")
            print(f"Помилка: {e}")

        again = input("Бажаєте продовжити? (так/ні): ").strip().lower()
        if again != "так":
            print("Дякуємо за використання калькулятора!")
            logging.info("Користувач завершив роботу калькулятора.")
            break

if __name__ == "__main__":
    main()
