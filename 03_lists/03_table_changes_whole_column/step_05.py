"""
Урок 3.3 "Таблица, которая меняется целым столбцом", шаг 5

Программа строит таблицу умножения размером `n`×`m`. В строке `i` и столбце `j` (нумерация с
единицы) стоит `i * j`. Но все строки таблицы получаются одинаковыми.

Найдите и исправьте ошибку.

Ввод. Два числа `n` и `m` через пробел (от 1 до 9).

Вывод. `n` строк по `m` чисел через пробел.

Программа с ошибкой, которая лежит в редакторе на Stepik

    n, m = map(int, input().split())
    table = [[0] * m] * n
    for i in range(n):
        for j in range(m):
            table[i][j] = (i + 1) * (j + 1)
    for row in table:
        print(*row)
"""

n, m = map(int, input().split())
table = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        table[i][j] = (i + 1) * (j + 1)
for row in table:
    print(*row)
