"""
Урок 7.2 "Второй проход ничего не находит", шаг 7

Программа составляет словарь цен, выводит каждую позицию строкой `товар цена`, а затем общую сумму.
Сумма выводится верно, а позиции не выводятся совсем.

Найдите и исправьте ошибку.

Ввод. Строка с названиями товаров через пробел, затем строка с ценами через пробел. Названия не
повторяются.

Вывод. Позиции в порядке ввода, затем строка `Итого сумма`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    items = input().split()
    prices = list(map(int, input().split()))
    pairs = zip(items, prices)
    price_of = dict(pairs)
    for item, price in pairs:
        print(item, price)
    print("Итого", sum(price_of.values()))
"""

items = input().split()
prices = list(map(int, input().split()))
pairs = list(zip(items, prices))
price_of = dict(pairs)
for item, price in pairs:
    print(item, price)
print("Итого", sum(price_of.values()))
