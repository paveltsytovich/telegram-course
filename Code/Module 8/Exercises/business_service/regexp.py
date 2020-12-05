import re

def check_phone(message):
    match = re.search(r'^Телефон ((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$',message)
    if match:
        return "Телефон корректный"
    else:
        return "Неверный формат номера телефона"
    
def check_email(message):
    match = re.search(r'^Почта [^@]+@[^@.]+\.[^@]+$',message)
    if match:
        return "Адрес электронной почты корректный"
    else:
        return "Адрес некорректный"