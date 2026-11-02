"""
Урок 4.4 "Переменная есть, а Python её не видит", шаг 4

Функция `add` должна прибавлять число к общей сумме `total`. Но программа падает с ошибкой
`UnboundLocalError`.

Исправьте программу. Подойдёт любой способ из урока.

Ввод. Целые числа через пробел.

Вывод. Их сумма.

Программа с ошибкой, которая лежит в редакторе на Stepik

    total = 0

    def add(n):
        total += n

    for x in map(int, input().split()):
        add(x)
    print(total)
"""

total = 0

def add(current, n):
    return current + n

for x in map(int, input().split()):
    total = add(total, x)
print(total)
