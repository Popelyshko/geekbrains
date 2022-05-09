import requests
import xml.etree.ElementTree as ET


def currency_rates(char_code: str):
    char_code = char_code.upper()
    cbr_xml = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    root = ET.fromstring(cbr_xml.text)
    node = root.find(f'Valute[CharCode="{char_code}"]/Value')
    if node is None:
        return None
    else:
        return float(node.text)


value = currency_rates('eur')
print(f'За Евро {value} рублей')
value = currency_rates('usd')
print(f'За Доллар {value} рублей')



