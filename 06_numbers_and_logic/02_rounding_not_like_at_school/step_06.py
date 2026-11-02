"""
Урок 6.2 "Округление не как в школе", шаг 6

Программа округляет цены до копеек по-школьному. Но цену 2.675 она округляет до 2.67, а не до 2.68.

Найдите и исправьте ошибку.

Ввод. Цены через пробел, у каждой не больше трёх знаков после точки.

Вывод. Каждая цена на отдельной строке с двумя знаками после точки.

Программа с ошибкой, которая лежит в редакторе на Stepik

    from decimal import Decimal, ROUND_HALF_UP

    for x in input().split():
        price = Decimal(float(x))
        print(price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
"""

from decimal import Decimal, ROUND_HALF_UP

for x in input().split():
    price = Decimal(x)
    print(price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
