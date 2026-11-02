"""
Урок 9.1 "Всё вместе", шаг 7

Функция `min_max` возвращает наименьшее и наибольшее значение. Программа вызывает её для каждой
строки ввода и падает с ошибкой.

Найдите и исправьте ошибку.

Ввод. Несколько строк с целыми числами через пробел.

Вывод. Для каждой строки минимум и максимум через пробел.

Программа с ошибкой, которая лежит в редакторе на Stepik

    import sys

    def min_max(values):
        return min(values), max(values)

    for line in sys.stdin.read().splitlines():
        values = map(int, line.split())
        low, high = min_max(values)
        print(low, high)
"""

import sys

def min_max(values):
    return min(values), max(values)

for line in sys.stdin.read().splitlines():
    values = list(map(int, line.split()))
    low, high = min_max(values)
    print(low, high)
