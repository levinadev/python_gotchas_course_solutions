"""
Урок 9.1 "Всё вместе", шаг 9

Класс `PiggyBank` описывает копилку с целью. Для каждой копилки программа выводит, сколько было
взносов и набрана ли цель. Но число взносов растёт от копилки к копилке, а цель иногда не
засчитывается, хотя сумма совпадает. В программе две ошибки.

Найдите и исправьте обе.

Ввод. Несколько строк, в каждой цель копилки и её взносы через пробел, это числа не больше чем с
двумя знаками после точки.

Вывод. Для каждой копилки число взносов и `Да`, если сумма взносов равна цели, или `Нет`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    import sys

    class PiggyBank:
        history = []

        def __init__(self, goal):
            self.goal = goal
            self.total = 0.0

        def put(self, amount):
            self.total += amount
            self.history.append(amount)


    for line in sys.stdin.read().splitlines():
        goal, *amounts = map(float, line.split())
        bank = PiggyBank(goal)
        for a in amounts:
            bank.put(a)
        print(len(bank.history), "Да" if bank.total == bank.goal else "Нет")
"""

import math
import sys

class PiggyBank:
    def __init__(self, goal):
        self.goal = goal
        self.total = 0.0
        self.history = []

    def put(self, amount):
        self.total += amount
        self.history.append(amount)


for line in sys.stdin.read().splitlines():
    goal, *amounts = map(float, line.split())
    bank = PiggyBank(goal)
    for a in amounts:
        bank.put(a)
    print(len(bank.history), "Да" if math.isclose(bank.total, bank.goal) else "Нет")
