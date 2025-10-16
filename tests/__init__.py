from masks import get_card_number, get_mask_account
from widget import mask_account_card, get_date

input_number_card = "4563975548726482"
masked_card = get_card_number(input_number_card)
print(f"введенный номер карты {input_number_card}")
print(f"замаскированный номер карты {masked_card}")

input_number_account = "25864741254787155555"
masked_account = get_mask_account(input_number_account)
print(f"введенный номер карты {input_number_account}")
print(f"замаскированный номер карты {masked_account}")

input_type_number_account = "Maestro 1596837868705199"
masked_account_card = mask_account_card(input_type_number_account)
print(f"Замаскированный аккаунт пользователя {masked_account_card}")

input_datime = "2024-03-11T02:26:18.671407"
date_correct = get_date(input_datime)
print(date_correct)

