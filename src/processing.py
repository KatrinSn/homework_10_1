from mypy.types import AnyType


def filter_by_state(
    bank_operations: list[dict], state: str = "EXECUTED"
) -> list[dict]:
    """Функция, которая обрабатывает список словарей банковских операций и фильтрует список по наличию ключа(статусу)
    state = 'EXECUTED' принимает список словарей, и через перебор каждого словаря в списке проверяет соответствие
    пары ключ - значение по ключу state, если значение по ключу соответствует заданному параметру, то данный словарь
    остается в списке для возврата списка. В результате возвращает список операций только со статусом EXECUTED"""

    return [
        bank_operation
        for bank_operation in bank_operations
        if bank_operation["state"] == state
    ]
bank_operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(filter_by_state(bank_operations))


def sort_by_date(
    operations: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, которая сортирует список словарей по ключу date по убыванию, функция принимает список словарей,
    и сортирует универсальным методом по убыванию через анонимную функцию, где аргумент для сортировки использует x,
    где x это значение по ключу date"""
    return sorted(operations, key=lambda x: x["date"], reverse=reverse)

operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(sort_by_date(operations))