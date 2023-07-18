import re
def has_asci(value:str)->bool:
    return value.isascii()
def has_space(value:str)->bool:
    return ' ' in value
def has_number(value: str)->bool:
    x=re.findall("[0-9]", value)
    if len(x)!=0:
        return True
    else:
        return False
def has_big_Leters(value:str)->bool:
    for m in value:
        if m.isupper():
            return True
def has_small_Leters(value:str)->bool:
    for m in value:
        if m.islower():
            return True
def has_specific_charecters(value:str)->bool:
    x="+-/*!\"№;%:?*\()="
    for i in x:
        for char in value:
            if i==char:
                return False
            if i!=char:
                return True
def password_length(value:str)->bool:
    if len(value)<8:
        return False
    else:
        return True
def IsPasswordSuituble(value: str) -> bool:
    if has_space(value):
        return False
    if not has_number(value):
        return False
    if not has_big_Leters(value):
        return False
    if not has_small_Leters(value):
        return False
    if not has_specific_charecters(value):
        return False
    if password_length(value):
        return True
    if has_asci(value):
        return True

