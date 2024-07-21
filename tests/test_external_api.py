import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_transaction_amount_rub

load_dotenv()
api_key = os.getenv("API_KEY")


@patch("requests.get")
def test_get_transaction_amount_rub(mock_get, transaction_info_for_external_api):
    mock_get.return_value.json.return_value = {"result": 3}
    assert get_transaction_amount_rub(transaction_info_for_external_api) == 3
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": api_key},
        params={"amount": "31957.58", "from": "EUR", "to": "RUB"},
    )


def test_get_transaction_amount_rub_rub():
    assert (
        get_transaction_amount_rub(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 31957.58
    )
