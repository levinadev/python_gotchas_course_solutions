"""
Урок 9.1 "Всё вместе", шаг 10

Считайте покупки, по одной на строке, это товар и цена. Один товар может встречаться несколько раз.
Выведите сумму по каждому товару в порядке первого появления и общий итог. Чтобы суммы не разошлись
с копейками, считайте через `Decimal`.

Ввод. Несколько строк, в каждой название товара и цена через пробел. У цены не больше двух знаков
после точки.

Вывод. Строки `товар сумма`, затем строка `Итого сумма`. Все суммы с двумя знаками после точки.
"""

import sys
from decimal import Decimal

totals = {}
for line in sys.stdin.read().splitlines():
    item, price = line.split()
    totals[item] = totals.get(item, Decimal("0")) + Decimal(price)
for item, total in totals.items():
    print(item, total.quantize(Decimal("0.01")))
print("Итого", sum(totals.values()).quantize(Decimal("0.01")))
