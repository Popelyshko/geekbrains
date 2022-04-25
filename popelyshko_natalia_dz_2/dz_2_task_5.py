price_list = [57.8, 46.51, 97, 64.56, 58.98, 18.25, 17, 76.67, 89, 43, 34.56, 78.76, 89.45, 13.18, 12.34, 79, 26]


def print_price(price_item):
    price_item_str = (format(price_item, '.2f'))
    price_list_str: list[str] = price_item_str.split('.')
    result = f'{price_list_str[0]} руб. {price_list_str[1]} коп.'
    return result


for price_item in price_list:
    str_item = print_price(price_item)
    print(str_item, end=', ')


print('')
price_list.sort()
for price_item in price_list:
    str_item = print_price(price_item)
    print(str_item, end=', ')


print('')
new_price_list = price_list.copy()
new_price_list.sort(reverse=True)
for price_item in new_price_list:
    str_item = print_price(price_item)
    print(str_item, end=', ')


print('')
for price_item in new_price_list[:5]:
    str_item = print_price(price_item)
    print(str_item, end=', ')









