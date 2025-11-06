def filter_by_state(
    bank_operations: list[dict[str, str | object]], state: str = "EXECUTED"
) -> list[dict[str, str | object]]:
    """Функция, которая обрабатывает список словарей и фильтрует список по наличию ключа state = 'EXECUTED'"""

    return [
        bank_operation
        for bank_operation in bank_operations
        if bank_operation["state"] == state
    ]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, которая сортирует список словарей по ключу date по убыванию"""
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
