from src.masks import get_mask_account, get_card_number


def mask_account_card(card_type_number: str) -> str:
    """Функция, которая умеет обрабатывать информацию о картах и о счетах"""
    card_info = card_type_number.rsplit(" ", 1)
    if "Cчет" in card_type_number:
        return f"{card_info[0]}{get_mask_account(card_info[1])}"
    else:
        return f"{card_info[0]}{get_card_number(card_info[1])}"


def get_date(date_incorrect: str) -> str:
    """Функция, которая умеет выдавать дату в формате ДД.ММ.ГГГГ"""

    date_correct = f"{date_incorrect[8:10]}.{date_incorrect[5:7]}.{date_incorrect[0:4]}"

    return date_correct
