def filter_by_state(transaction_info: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает список транзакций, отфильтрованных по статусу"""

    return [transaction for transaction in transaction_info if transaction["state"] == state]

