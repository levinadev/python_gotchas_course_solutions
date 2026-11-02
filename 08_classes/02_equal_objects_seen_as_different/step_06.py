"""
Урок 8.2 "Одинаковые объекты, которые Python считает разными", шаг 6

Робот ходит по клеткам, буквы `U`, `D`, `L` и `R` означают шаг вверх, вниз, влево и вправо. Начинает
он в клетке (0, 0). Программа считает, сколько раз робот приходил в клетку, где уже бывал, но всегда
выводит 0.

Найдите и исправьте ошибку.

Ввод. Строка из букв `U`, `D`, `L` и `R`.

Вывод. Количество возвращений в уже посещённые клетки.

Программа с ошибкой, которая лежит в редакторе на Stepik

    class Cell:
        def __init__(self, x, y):
            self.x, self.y = x, y


    steps = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    x = y = 0
    visited = [Cell(0, 0)]
    returns = 0
    for move in input():
        dx, dy = steps[move]
        x, y = x + dx, y + dy
        cell = Cell(x, y)
        for old in visited:
            if old == cell:
                returns += 1
                break
        else:
            visited.append(cell)
    print(returns)
"""

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


steps = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
x = y = 0
visited = [Cell(0, 0)]
returns = 0
for move in input():
    dx, dy = steps[move]
    x, y = x + dx, y + dy
    cell = Cell(x, y)
    for old in visited:
        if old == cell:
            returns += 1
            break
    else:
        visited.append(cell)
print(returns)
