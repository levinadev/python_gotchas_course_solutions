"""
Урок 8.1 "Изменился один объект, а за ним все", шаг 5

В классе `Order` список товаров задаётся параметром по умолчанию в `__init__`. Каждый заказ должен
содержать только свои товары, но они накапливаются от заказа к заказу.

Найдите и исправьте ошибку.

Ввод. Несколько строк, в каждой товары одного заказа через пробел.

Вывод. Для каждого заказа строка `Заказ N: товары`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    import sys

    class Order:
        def __init__(self, items=[]):
            self.items = items

        def add(self, item):
            self.items.append(item)


    for n, line in enumerate(sys.stdin.read().splitlines(), 1):
        order = Order()
        for item in line.split():
            order.add(item)
        print(f"Заказ {n}:", *order.items)
"""

import sys

class Order:
    def __init__(self, items=None):
        self.items = items if items is not None else []

    def add(self, item):
        self.items.append(item)


for n, line in enumerate(sys.stdin.read().splitlines(), 1):
    order = Order()
    for item in line.split():
        order.add(item)
    print(f"Заказ {n}:", *order.items)
