"""
Урок 3.2 "Копия есть, а данные общие", шаг 6

Программа хранит журнал, по строке оценок на ученика. Для отчёта в копии журнала каждому ученику
добавляется оценка 5 за проект. Исходный журнал должен остаться прежним, но пятёрки появляются и в
нём.

Найдите и исправьте ошибку.

Ввод. Несколько строк, в каждой оценки одного ученика через пробел.

Вывод. Исходный журнал, строка `---`, журнал с оценками за проект.

Программа с ошибкой, которая лежит в редакторе на Stepik

    import sys

    journal = [line.split() for line in sys.stdin.read().splitlines()]
    report = journal.copy()
    for row in report:
        row.append("5")
    for row in journal:
        print(*row)
    print("---")
    for row in report:
        print(*row)
"""

import sys

journal = [line.split() for line in sys.stdin.read().splitlines()]
report = [row[:] for row in journal]
for row in report:
    row.append("5")
for row in journal:
    print(*row)
print("---")
for row in report:
    print(*row)
