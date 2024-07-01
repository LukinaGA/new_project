from src.widget import mask_account_card, get_data
import pytest


@pytest.mark.parametrize("card_or_account_info, expected", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"), ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card(card_or_account_info, expected):
    assert mask_account_card(card_or_account_info) == expected


def test_get_data():
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"