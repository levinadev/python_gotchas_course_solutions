"""
Урок 6.2 "Округление не как в школе", шаг 4

Округлите каждое число "по-школьному", половинки всегда вверх.

Ввод. Неотрицательные числа с одним знаком после точки, через пробел.

Вывод. Округлённые целые числа через пробел.
"""

from decimal import Decimal, ROUND_HALF_UP

result = [Decimal(x).quantize(Decimal("1"), rounding=ROUND_HALF_UP) for x in input().split()]
print(*result)
