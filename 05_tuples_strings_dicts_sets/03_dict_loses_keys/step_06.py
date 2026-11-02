"""
Урок 5.3 "Словарь, который теряет ключи", шаг 6

Программа должна убрать со склада товары, которых не осталось, и вывести остальные. На многих данных
она падает с ошибкой.

Найдите и исправьте ошибку.

Ввод. Товары через пробел в формате `название=количество`.

Вывод. Товары с ненулевым количеством в порядке ввода, строками `название количество`, или `пусто`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    stock = {}
    for pair in input().split():
        name, qty = pair.split("=")
        stock[name] = int(qty)
    for name in stock:
        if stock[name] == 0:
            del stock[name]
    if not stock:
        print("пусто")
    for name in stock:
        print(name, stock[name])
"""

stock = {}
for pair in input().split():
    name, qty = pair.split("=")
    stock[name] = int(qty)
for name in list(stock):
    if stock[name] == 0:
        del stock[name]
if not stock:
    print("пусто")
for name in stock:
    print(name, stock[name])
