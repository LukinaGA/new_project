import os

import requests
from dotenv import load_dotenv


def get_transaction_amount_rub(transaction):
    """Возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":

        return float(transaction["operationAmount"]["amount"])

    load_dotenv()
    api_key = os.getenv("API_KEY")

    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {
        "amount": transaction["operationAmount"]["amount"],
        "from": transaction["operationAmount"]["currency"]["code"],
        "to": "RUB",
    }

    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers, params=payload)
    result = response.json()

    return float(result["result"])
