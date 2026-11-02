"""
Урок 9.1 "Всё вместе", шаг 6

Программа ведёт таблицу баллов. Для каждого из `n` дней копирует базовые баллы и прибавляет к ним
бонус этого дня. В конце она выводит базовые баллы и таблицу. Но и таблица, и базовые баллы
получаются неверными.

Найдите и исправьте ошибку.

Ввод. Число дней `n`; строка с базовыми баллами через пробел; затем `n` строк с бонусом каждого дня.

Вывод. Строка `База.` с исходными баллами, затем `n` строк таблицы.

Программа с ошибкой, которая лежит в редакторе на Stepik

    n = int(input())
    base = list(map(int, input().split()))
    table = [base] * n
    for i in range(n):
        bonus = int(input())
        for j in range(len(table[i])):
            table[i][j] += bonus
    print("База:", *base)
    for row in table:
        print(*row)
"""

n = int(input())
base = list(map(int, input().split()))
table = [base[:] for _ in range(n)]
for i in range(n):
    bonus = int(input())
    for j in range(len(table[i])):
        table[i][j] += bonus
print("База:", *base)
for row in table:
    print(*row)
