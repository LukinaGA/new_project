from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """Возвращает маску счёта или карты, исходя из полученных данных"""
    if card_or_account_info:
        card_or_acc_info_list = card_or_account_info.split()
        words = card_or_acc_info_list[:-1]
        digits = card_or_acc_info_list[-1]

        if card_or_account_info.lower().startswith("счет"):

            return f"{" ".join(words)} {get_mask_account(digits)}"

        return f"{" ".join(words)} {get_mask_card_number(digits)}"

    return ""


def get_date(date_info: str) -> str:
    """Возвращает дату в формате ДД.ММ.ГГГГ"""

    return f"{date_info[8:10]}.{date_info[5:7]}.{date_info[:4]}"
