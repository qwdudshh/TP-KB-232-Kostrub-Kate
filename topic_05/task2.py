import requests

def get_exchange_rates():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json"
    response = requests.get(url)
    if response.status_code == 200:
        rates = response.json()
        return {rate['cc']: rate['rate'] for rate in rates}
    else:
        print("Не вдалося отримати дані про курси валют.")
        return {}

def convert_currency(amount, currency, rates):
    if currency in rates:
        return amount * rates[currency]
    else:
        print(f"Валюта {currency} недоступна для конвертації.")
        return None

def main():
    rates = get_exchange_rates()
    if not rates:
        return

    currency = input("Введіть код валюти (EUR, USD, PLN): ").upper()
    try:
        amount = float(input(f"Введіть кількість {currency}: "))
    except ValueError:
        print("Будь ласка, введіть числове значення.")
        return

    result = convert_currency(amount, currency, rates)
    if result is not None:
        print(f"{amount} {currency} = {result:.2f} UAH")

if __name__ == "__main__":
    main()
