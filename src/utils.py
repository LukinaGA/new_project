import json


def get_transactions_info(path_json_file):
    """Возвращает список словарей с данными о финансовых транзакциях из файла json"""
    try:
        with open(path_json_file, encoding="utf-8") as file:
            transactions = json.load(file)
    except TypeError:
        return []
    except FileNotFoundError:
        return []
    except ValueError:
        return []
    else:
        return transactions
