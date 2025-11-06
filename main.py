from src.masks import get_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state

input_needed_function = input("Введите номер нужной функции, 1, 2 и т д -> ")
# Функция 1
if input_needed_function == "1":
    input_number_card = input("Введите номер карты ->")
    masked_card = get_card_number(input_number_card)
    print(f"введенный номер карты {input_number_card}")
    print(f"замаскированный номер карты {masked_card}")

# Функция 2
elif input_needed_function == "2":
    input_number_account: str = input("Введите номер счета ->")
    masked_account: str = get_mask_account(input_number_account)
    print(f"введенный номер карты {input_number_account}")
    print(f"замаскированный номер карты {masked_account}")

# Функция 3
elif input_needed_function == "3":
    input_type_number_account: str = "Введите тип карты и номер или слово счет и номер ->"
    masked_account_card: str = mask_account_card(input_type_number_account)
    print(f"Замаскированный аккаунт пользователя {masked_account_card}")

# Функция 4
elif input_needed_function == "4":
    input_datime: str = input("Введите дату -> ")
    date_correct: str = get_date(input_datime)
    print(date_correct)

# Функция 5
elif input_needed_function == "5":
    dictionaries = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    filter_data = filter_by_state(dictionaries)
    print(f"Результат фильтра {filter_data}")

else:
    print("функция не выбрана")
