import utils_module

value = utils_module.currency_rates('eur')
print(f'За Евро {value} рублей')
value = utils_module.currency_rates('usd')
print(f'За Доллар {value} рублей')
