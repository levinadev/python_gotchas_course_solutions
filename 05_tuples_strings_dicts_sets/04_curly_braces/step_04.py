"""
Урок 5.4 "Что скрывают фигурные скобки", шаг 4

Программа убирает повторы из списка покупок и сохраняет порядок первого появления. Она падает с
ошибкой.

Найдите и исправьте ошибку.

Ввод. Слова через пробел.

Вывод. Слова без повторов через пробел, в порядке первого появления.

Программа с ошибкой, которая лежит в редакторе на Stepik

    seen = {}
    result = []
    for item in input().split():
        if item not in seen:
            seen.add(item)
            result.append(item)
    print(*result)
"""

seen = set()
result = []
for item in input().split():
    if item not in seen:
        seen.add(item)
        result.append(item)
print(*result)
