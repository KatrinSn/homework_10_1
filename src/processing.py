from mypy.types import AnyType


def filter_by_state(
    bank_operations: list[dict], state: str = "EXECUTED"
) -> list[dict]:
    """Функция, которая обрабатывает список словарей и фильтрует список по наличию ключа state = 'EXECUTED'
    принимает список словарей, и через перебор каждого словаря в списке проверяет соответствие пары ключ - значение
    по ключу state, если значение по ключу соответствует заданному параметру, то данный словарь остается в списке для
    возврата списка"""

    return [
        bank_operation
        for bank_operation in bank_operations
        if bank_operation["state"] == state
    ]


def sort_by_date(
    operations: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, которая сортирует список словарей по ключу date по убыванию, функция принимает список словарей,
    и сортирует универсальным методом по убыванию через анонимную функцию, где аргумент для сортировки использует x,
    где x это значение по ключу date"""
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)
