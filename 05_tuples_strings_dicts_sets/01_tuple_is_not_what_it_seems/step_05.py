"""
Урок 5.1 "Кортеж не то, чем кажется", шаг 5

Программа хранит ученика кортежем из имени и списка оценок и добавляет в этот список новые оценки.
Она падает с ошибкой.

Найдите и исправьте ошибку.

Ввод. Строка с именем и оценками через пробел, затем строка с новыми оценками.

Вывод. Имя и все оценки через пробел.

Программа с ошибкой, которая лежит в редакторе на Stepik

    name, *grades = input().split()
    student = (name, list(map(int, grades)))
    new = list(map(int, input().split()))
    student[1] += new
    print(student[0], *student[1])
"""

name, *grades = input().split()
student = (name, list(map(int, grades)))
new = list(map(int, input().split()))
student[1].extend(new)
print(student[0], *student[1])
