from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"

    assert get_mask_card_number("abcdefghijklmnop") == "Некорректный формат номера карты"

    assert get_mask_card_number("132427638298376") == "Некорректный формат номера карты"

    assert get_mask_card_number("") == "Некорректный формат номера карты"


def test_get_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"

    assert get_mask_account("asdfghjkldqwertyuiop") == "Некорректный формат номера счёта"

    assert get_mask_account("1234567891234567891") == "Некорректный формат номера счёта"

    assert get_mask_account("") == "Некорректный формат номера счёта"
