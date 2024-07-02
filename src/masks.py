def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску номера карты в формате XXXX XX** **** XXXX"""
    if len(card_number) == 16 and card_number.isdigit():

        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return "Некорректный формат номера карты"


def get_mask_account(account_number: str) -> str:
    """Возвращает маску номера счета в формате **XXXX"""
    if len(account_number) == 20 and account_number.isdigit():

        return f"**{account_number[-4:]}"

    return "Некорректный формат номера счёта"
