"""
Урок 4.3 "Все функции вернули одно и то же", шаг 6

Для каждой скидки из первой строки создайте функцию, которая получает цену и возвращает цену со
скидкой, `price * (100 - p) // 100`, где `p` это размер скидки в процентах. Сложите функции в список
`discounts`.

Ввод. Строка со скидками в процентах через пробел, затем строка с ценой (целое число).

Вывод. Цена после каждой скидки, по одной на строке.

Программа с ошибкой, которая лежит в редакторе на Stepik

    percents = list(map(int, input().split()))
    price = int(input())
    discounts = []

    # заполните список discounts функциями

    for f in discounts:
        print(f(price))
"""

percents = list(map(int, input().split()))
price = int(input())
discounts = []

for p in percents:
    discounts.append(lambda price, p=p: price * (100 - p) // 100)

for f in discounts:
    print(f(price))
