def filter_by_currency(transactions_list: list[dict], currency: str):
    """Возвращать список с операциями по заданной валюте"""
    if transactions_list:
        try:
            filtered_transactions = [transaction for transaction in transactions_list if
                                     transaction["operationAmount"]["currency"]["code"] == currency]
        except KeyError:
            filtered_transactions = [transaction for transaction in transactions_list if
                                     transaction.get("currency_code") == currency]

        return filtered_transactions

    else:
        return []


def transaction_descriptions(transactions: list[dict]):
    """Возвращает описание операций по очереди"""
    if transactions:
        for transaction in transactions:
            yield transaction["description"]

    else:
        return []


def card_number_generator(start: int = 1, stop: int = 9999999999999999):
    """Генерирует номер карты в заданном диапазоне в формате ХХХХ ХХХХ ХХХХ ХХХХ"""
    for i in range(start, stop + 1):

        if len(str(i)) < 16:
            i = "0" * (16 - len(str(i))) + str(i)

        yield f"{str(i)[:4]} {str(i)[4:8]} {str(i)[8:12]} {str(i)[-4:]}"
