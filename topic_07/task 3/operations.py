def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Будь ласка, введіть число.")

def get_operation():
    while True:
        operation = input("Введіть операцію (+, -, *, /): ")
        if operation in ['+', '-', '*', '/', '^', '!-']:
            return operation
        else:
            print("Невірна операція. Спробуйте ще раз.")
