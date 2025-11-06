
def filter_by_state(
    bank_operations: list[dict[str, str | object]], state: str = "EXECUTED"
) -> list[dict[str, str | object]]:
    """Функция, которая обрабатывает список словарей и фильтрует список по наличию ключа state = 'EXECUTED'"""

    return [
        bank_operation
        for bank_operation in bank_operations
        if bank_operation["state"] == state
    ]
