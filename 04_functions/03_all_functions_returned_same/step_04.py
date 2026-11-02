"""
Урок 4.3 "Все функции вернули одно и то же", шаг 4

Программа создаёт список функций. Функция с номером `k` умножает число на `k` (от 1 до `n`). Затем
каждая функция применяется к числу `x`. Но все результаты получаются одинаковыми.

Найдите и исправьте ошибку.

Ввод. Два числа `n` и `x` через пробел.

Вывод. `n` чисел через пробел.

Программа с ошибкой, которая лежит в редакторе на Stepik

    n, x = map(int, input().split())
    multipliers = []
    for k in range(1, n + 1):
        multipliers.append(lambda value: value * k)
    print(*[f(x) for f in multipliers])
"""

n, x = map(int, input().split())
multipliers = []
for k in range(1, n + 1):
    multipliers.append(lambda value, k=k: value * k)
print(*[f(x) for f in multipliers])
