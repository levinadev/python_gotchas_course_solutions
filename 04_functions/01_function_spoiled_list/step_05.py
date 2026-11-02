"""
Урок 4.1 "Функция испортила чужой список", шаг 5

Функция `top3` должна возвращать три лучших результата, не меняя переданный список. Программа
выводит исходный список и тройку лучших, но исходный список оказывается отсортированным.

Найдите и исправьте ошибку.

Ввод. Не меньше трёх целых чисел через пробел.

Вывод. Числа в исходном порядке, затем три наибольших по убыванию.

Программа с ошибкой, которая лежит в редакторе на Stepik

    def top3(scores):
        scores.sort(reverse=True)
        return scores[:3]

    results = list(map(int, input().split()))
    best = top3(results)
    print(*results)
    print(*best)
"""

def top3(scores):
    return sorted(scores, reverse=True)[:3]

results = list(map(int, input().split()))
best = top3(results)
print(*results)
print(*best)
