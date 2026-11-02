"""
Урок 3.3 "Таблица, которая меняется целым столбцом", шаг 6

Программа рисует поле `n`×`n` для морского боя и отмечает клетки с кораблями символом `#`. Но каждый
корабль появляется сразу во всех строках поля.

Найдите и исправьте ошибку.

Ввод. Число `n` (от 1 до 9), затем строки с номером строки и столбца корабля через пробел (нумерация
с нуля).

Вывод. `n` строк поля, пустая клетка обозначается точкой.

Программа с ошибкой, которая лежит в редакторе на Stepik

    import sys

    lines = sys.stdin.read().splitlines()
    n = int(lines[0])
    field = [["."] * n] * n
    for line in lines[1:]:
        r, col = map(int, line.split())
        field[r][col] = "#"
    for row in field:
        print("".join(row))
"""

import sys

lines = sys.stdin.read().splitlines()
n = int(lines[0])
field = [["."] * n for _ in range(n)]
for line in lines[1:]:
    r, col = map(int, line.split())
    field[r][col] = "#"
for row in field:
    print("".join(row))
