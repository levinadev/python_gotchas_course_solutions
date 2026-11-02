"""
Урок 8.2 "Одинаковые объекты, которые Python считает разными", шаг 4

Посчитайте, сколько разных точек введено. Допишите класс `Point` так, чтобы одинаковые точки
считались равными и программа работала.

Ввод. Несколько строк, в каждой два целых числа, координаты точки.

Вывод. Количество разных точек.

Программа с ошибкой, которая лежит в редакторе на Stepik

    import sys

    class Point:
        def __init__(self, x, y):
            self.x, self.y = x, y


    points = set()
    for line in sys.stdin.read().splitlines():
        x, y = map(int, line.split())
        points.add(Point(x, y))
    print(len(points))
"""

import sys

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))


points = set()
for line in sys.stdin.read().splitlines():
    x, y = map(int, line.split())
    points.add(Point(x, y))
print(len(points))
