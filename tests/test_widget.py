import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize("card_or_account_info, expected",
                         [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                          ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                          ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card(card_or_account_info, expected):
    assert mask_account_card(card_or_account_info) == expected


def test_get_data():
    assert get_data("2024-03-11T02:26:18.671407") == "11.03.2024"
