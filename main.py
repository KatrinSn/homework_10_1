from src.masks import get_card_number, get_mask_account
from src.widget import mask_account_card, get_date

input_number_card = input("Введите номер карты ->")
masked_card = get_card_number(input_number_card)
print(f"введенный номер карты {input_number_card}")
print(f"замаскированный номер карты {masked_card}")

input_number_account = input("Введите номер счета ->")
masked_account = get_mask_account(input_number_account)
print(f"введенный номер карты {input_number_account}")
print(f"замаскированный номер карты {masked_account}")

input_type_number_account = "Введите тип карты и номер или слово счет и номер ->"
masked_account_card = mask_account_card(input_type_number_account)
print(f"Замаскированный аккаунт пользователя {masked_account_card}")

input_datime = input("Введите дату -> ")
date_correct = get_date(input_datime)
print(date_correct)
