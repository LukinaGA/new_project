import json
# import logging
import os

import pandas as pd

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
#     filename="..\\logs\\utils.log",
#     encoding="utf-8",
#     filemode="w",
# )
# logger = logging.getLogger("utils")


def get_transactions_info(path_json_file):
    """Возвращает список словарей с данными о финансовых транзакциях из файла json"""
    # logger.info(f"Попытка открытия файла {os.path.basename(path_json_file)}")
    try:
        with open(path_json_file, encoding="utf-8") as file:
            transactions = json.load(file)
    except (TypeError, FileNotFoundError, ValueError):
        # logger.warning("Ошибка чтения файла")
        return []
    else:
        # logger.info("Успешное открытие файла")
        return transactions


def read_csv_file(file_path):
    """Считывает файлы CSV-формата"""
    try:
        csv_file_data = pd.read_csv(file_path, delimiter=";")

    except Exception:
        return "Не удалось считать файл"

    return csv_file_data.to_dict("records")


def read_excel_file(file_path):
    """Считывает файлы XLSX-фомата"""
    try:
        xlsx_file_data = pd.read_excel(file_path)

    except Exception:
        return "Не удалось считать файл"

    return xlsx_file_data.to_dict("records")
