for percent_item in range(1, 101):
    if percent_item in [1, 21, 31, 41, 51, 61, 71, 81]:
        name = "процент"
    elif 2 <= percent_item <= 4:
        name = "процента"
    elif 5 <= percent_item <= 20:
        name = "процентов"
    elif 22 <= percent_item <= 24:
        name = "процента"
    elif 32 <= percent_item <= 34:
        name = "процента"
    elif 42 <= percent_item <= 44:
        name = "процента"
    elif 52 <= percent_item <= 54:
        name = "процента"
    elif 62 <= percent_item <= 64:
        name = "процента"
    elif 72 <= percent_item <= 74:
        name = "процента"
    elif 82 <= percent_item <= 84:
        name = "процента"
    elif 92 <= percent_item <= 94:
        name = "процента"
    else:
        name = "процентов"
    print(f"{percent_item} {name}")
