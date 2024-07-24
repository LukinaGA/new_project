import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
    filename="..\\logs\\masks.log",
    encoding="utf-8",
    filemode="w",
)
logger = logging.getLogger("masks")


def get_mask_card_number(card_number: str) -> str:
    """Возвращает маску номера карты в формате XXXX XX** **** XXXX"""
    logger.info(f"Проверка формата номера карты: {card_number}")
    if len(card_number) == 16 and card_number.isdigit():
        logger.info("Успешная маскировка номера карты")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    logger.warning("Некорректный формат номера карты")
    return "Некорректный формат номера карты"


def get_mask_account(account_number: str) -> str:
    """Возвращает маску номера счета в формате **XXXX"""
    logger.info(f"Проверка формата номера счёта: {account_number}")
    if len(account_number) == 20 and account_number.isdigit():
        logger.info("Успешная маскировка номера счёта")
        return f"**{account_number[-4:]}"

    logger.warning("Некорректный формат номера счёта")
    return "Некорректный формат номера счёта"
