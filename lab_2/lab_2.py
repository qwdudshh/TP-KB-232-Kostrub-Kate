import csv
import sys

directory = []  

def load_from_csv(filename):
    global directory
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            directory = [row for row in reader]
            print(f"Завантажено {len(directory)} записів.")
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
    except Exception as e:
        print(f"Помилка при завантаженні даних: {e}")

def save_to_csv(filename):
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "group"])
            writer.writeheader()
            writer.writerows(directory)
            print(f"Дані успішно збережено у файл {filename}.")
    except Exception as e:
        print(f"Помилка при збереженні даних: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть ім'я файлу для завантаження даних.")
    else:
        load_from_csv(sys.argv[1])

    save_to_csv("students.csv")
