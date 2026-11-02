"""
Урок 2.1 "Что на самом деле хранит переменная", шаг 7

После пересдачи все двойки в журнале заменяются тройками. Программа должна вывести оценки до
пересдачи и после, но двоек нет уже в обеих строках.

Найдите и исправьте ошибку.

Ввод. Оценки от 2 до 5 через пробел.

Вывод. Две строки, оценки до пересдачи и после.

Программа с ошибкой, которая лежит в редакторе на Stepik

    grades = list(map(int, input().split()))
    retake = grades
    for i in range(len(retake)):
        if retake[i] == 2:
            retake[i] = 3
    print(*grades)
    print(*retake)
"""

grades = list(map(int, input().split()))
retake = grades.copy()
for i in range(len(retake)):
    if retake[i] == 2:
        retake[i] = 3
print(*grades)
print(*retake)
