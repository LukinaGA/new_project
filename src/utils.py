import json
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
    filename="..\\logs\\utils.log",
    encoding="utf-8",
    filemode="w",
)
logger = logging.getLogger("utils")


def get_transactions_info(path_json_file):
    """Возвращает список словарей с данными о финансовых транзакциях из файла json"""
    logger.info(f"Попытка открытия файла {os.path.basename(path_json_file)}")
    try:
        with open(path_json_file, encoding="utf-8") as file:
            transactions = json.load(file)
    except (TypeError, FileNotFoundError, ValueError):
        logger.warning("Ошибка чтения файла")
        return []
    else:
        logger.info("Успешное открытие файла")
        return transactions
