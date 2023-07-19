import re


def has_asci(value: str) -> bool:
    return value.isascii()


def has_space(value: str) -> bool:
    return ' ' in value


def has_number(value: str) -> bool:
    x = re.findall("[0-9]", value)
    if len(x) != 0:
        return True
    else:
        return False


def has_big_leters(value: str) -> bool:
    for m in value:
        if m.isupper():
            return True
    return False


def has_small_leters(value: str) -> bool:
    for m in value:
        if m.islower():
            return True
    return False


def has_specific_charecters(value: str) -> bool:
    x = "+-/*!\"№;%:?*\()="
    for i in x:
        for char in value:
            if i == char:
                return False
    return False


def is_valid_password_length(value: str) -> bool:
    if len(value) < 8 and value.isascii():
        return False
    else:
        return True


def is_password_suituble(value: str) -> bool:
    if has_space(value):
        return False
    if has_number(value):
        return True
    if has_big_leters(value):
        return True
    if has_small_leters(value):
        return True
    if has_specific_charecters(value):
        return True
    if is_valid_password_length(value):
        return True
    if has_asci(value):
        return True
