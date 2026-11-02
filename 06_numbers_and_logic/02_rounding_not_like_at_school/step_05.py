"""
Урок 6.2 "Округление не как в школе", шаг 5

Итоговая оценка это средний балл, округлённый по-школьному. При среднем 4.5 ученик должен получить
5, а программа иногда ставит оценку ниже.

Найдите и исправьте ошибку.

Ввод. Оценки от 2 до 5 через пробел.

Вывод. Итоговая оценка.

Программа с ошибкой, которая лежит в редакторе на Stepik

    grades = list(map(int, input().split()))
    print(round(sum(grades) / len(grades)))
"""

from decimal import Decimal, ROUND_HALF_UP

grades = list(map(int, input().split()))
average = Decimal(sum(grades)) / Decimal(len(grades))
print(average.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
