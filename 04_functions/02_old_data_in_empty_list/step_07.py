"""
Урок 4.2 "Откуда в пустом списке старые данные", шаг 7

Допишите функцию `add_unique(item, items)`. Она добавляет `item` в список `items`, если его там ещё
нет, и возвращает этот список. Если список не передан, функция начинает новый пустой список.

Ввод. Несколько строк со словами через пробел.

Вывод. Для каждой строки её слова без повторов в порядке первого появления.

Программа с ошибкой, которая лежит в редакторе на Stepik

    import sys

    # напишите функцию add_unique


    for line in sys.stdin.read().splitlines():
        words = line.split()
        tags = add_unique(words[0])
        for word in words[1:]:
            add_unique(word, tags)
        print(*tags)
"""

import sys

def add_unique(item, items=None):
    if items is None:
        items = []
    if item not in items:
        items.append(item)
    return items


for line in sys.stdin.read().splitlines():
    words = line.split()
    tags = add_unique(words[0])
    for word in words[1:]:
        add_unique(word, tags)
    print(*tags)
