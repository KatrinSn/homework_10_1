def get_card_number(card_number: str) -> str:
    """
    Функция маскировки номера банковской карты:
    :param card_number: принимает номер карты в виде строки
    :return: возвращает замаскированнный номер карты в виде строки XXXX XX** **** XXXX
    """
    # проверка количества введенных символов
    if len(card_number) != 16:
        raise ValueError("номер карты должен содержать 16 цифр")

    # маскировка номера карты
    masked = (
        card_number[:4]
        + " "
        + card_number[4:6]
        + "**"
        + " "
        + "****"
        + " "
        + card_number[-4:]
    )
    # возвращаем маскировку номера карты
    return masked


def get_mask_account(account_number: str) -> str:
    """функция маскировки номера счета
    :param account_number: номер счета
    :return: замаскированный номер счета в виде **XXXX"""
    #  проверяем кол-во символов
    if len(account_number) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")
    # возвращаем маскировку номера счета
    return f"**{account_number[-4:]}"
