import re

list_email = []
dict_info = {}


def email_parse(email_address):
    parsed = re.findall(r'(^[\w\.-]+)@([\w\.-]+)$', email_address)
    if len(parsed) < 1:
        raise ValueError("Ошибка валидации емайла")

    result = {'login': parsed[0][0], 'domain': parsed[0][1]}

    return result

print(email_parse('shop24@gmail.com'))
print(email_parse('!!!!!f@gma'))
