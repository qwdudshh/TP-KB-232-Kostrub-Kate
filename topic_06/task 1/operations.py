import logging

def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            logging.info(f"Введено число: {number}")
            return number
        except ValueError:
            logging.warning("Невірний ввід. Введіть число.")
            print("Будь ласка, введіть число.")

def get_operation():
    while True:
        operation = input("Введіть операцію (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            logging.info(f"Вибрано операцію: {operation}")
            return operation
        else:
            logging.warning(f"Невірна операція: {operation}")
            print("Невірна операція. Спробуйте ще раз.")

