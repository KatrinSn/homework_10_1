from masks import get_card_number, get_mask_account

input_number_card = input("Введите номер карты ->")
masked_card = get_card_number(input_number_card)
print(f"введенный номер карты {input_number_card}")
print(f"замаскированный номер карты {masked_card}")

input_number_account = input("Введите номер счета ->")
masked_account = get_mask_account(input_number_account)
print(f"введенный номер карты {input_number_account}")
print(f"замаскированный номер карты {masked_account}")
