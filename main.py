import requests
import os
import argparse
from requests import HTTPError
from dotenv import load_dotenv


def get_course(base, target, amount, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base}"
    response = requests.get(url)
    response.raise_for_status()
    currency = response.json()["conversion_rates"]
    target_rate = float(currency[target])
    converted_amount = amount * target_rate
    return converted_amount


def main():
    load_dotenv()
    api_key = os.getenv("TOKEN")
    parser = argparse.ArgumentParser(description="Конвертер валют")
    parser.add_argument("-b", "--base", help="Введите код базовой валюты (например RUB)", required=True)
    parser.add_argument("-t", "--target", help="Введите код целевой валюты (например EUR)", required=True)
    parser.add_argument("-a", "--amount", help="Введите сумму", required=True)
    args = parser.parse_args()
    base = args.base.upper()
    target = args.target.upper()
    amount = int(args.amount)
    try:
        print(f"Конвертированая сумма: {get_course(base, target, amount, api_key)} {target}")
    except HTTPError:
        print("Неверный курс валют или API ключ")


if __name__ == "__main__":
    main()