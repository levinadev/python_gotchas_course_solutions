"""
Урок 4.4 "Переменная есть, а Python её не видит", шаг 5

После каждого результата программа должна выводить лучший результат на данный момент. Но она падает
с ошибкой `UnboundLocalError`, хотя присваивание стоит внутри условия.

Исправьте программу. Подойдёт любой способ из урока.

Ввод. Неотрицательные целые числа через пробел.

Вывод. Лучший результат после каждого числа, по одному на строке.

Программа с ошибкой, которая лежит в редакторе на Stepik

    best = 0

    def update(score):
        if score > best:
            best = score

    for s in map(int, input().split()):
        update(s)
        print(best)
"""

best = 0

def update(current, score):
    if score > current:
        return score
    return current

for s in map(int, input().split()):
    best = update(best, s)
    print(best)
