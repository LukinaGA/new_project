import re
from collections import Counter, defaultdict


def search_dy_description(transactions_list: list[dict], search_word: str) -> list:
    """Возвращает список транзакций с заданным описанием"""
    found_transactions = []

    for transcription in transactions_list:
        if re.search(search_word, transcription["description"], flags=re.IGNORECASE):
            found_transactions.append(transcription)

    return found_transactions


def filter_by_categories(transactions_list: list[dict], categories_list: list[str]) -> dict:
    """Возвращает словарь с названием категорий и количеством транзакций в этих категориях"""
    filtered_transactions = defaultdict(int)
    counter = Counter([transaction["description"].lower() for transaction in transactions_list])

    for transaction in transactions_list:
        description = transaction.get("description").lower()
        if description in categories_list:
            filtered_transactions[description] = counter[description]

    return filtered_transactions
