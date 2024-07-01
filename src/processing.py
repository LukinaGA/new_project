def filter_by_state(transaction_info: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует транзакции по статусу"""

    return [transaction for transaction in transaction_info if transaction["state"] == state]


def sort_by_date(transaction_info: list[dict], is_decreasing: bool = True) -> list[dict]:
    """Сортирует список транзакций по дате"""
    if len(transaction_info) == 1:

        return transaction_info

    return sorted(
        transaction_info, key=lambda transaction: transaction["date"][:10].replace("-", ""), reverse=is_decreasing
    )
