from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    '''Возвращает маску счёта или карты, исходя из полученных данных'''
    digits = card_or_account_info.split()[-1]

    if card_or_account_info.lower().startswith("счет"):

        return get_mask_account(digits)

    return get_mask_card_number(digits)
