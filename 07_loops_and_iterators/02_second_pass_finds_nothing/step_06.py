"""
Урок 7.2 "Второй проход ничего не находит", шаг 6

Программа выводит, сколько учеников сдали зачёт, то есть набрали не меньше порога, а затем их баллы.
Количество верное, а вместо баллов выводится пустая строка.

Найдите и исправьте ошибку.

Ввод. Строка с баллами через пробел, затем строка с порогом. Хотя бы один ученик сдал зачёт.

Вывод. Количество сдавших, затем их баллы в порядке ввода через пробел.

Программа с ошибкой, которая лежит в редакторе на Stepik

    scores = list(map(int, input().split()))
    limit = int(input())
    passed = filter(lambda s: s >= limit, scores)
    print(len(list(passed)))
    print(*passed)
"""

scores = list(map(int, input().split()))
limit = int(input())
passed = list(filter(lambda s: s >= limit, scores))
print(len(passed))
print(*passed)
