"""
Урок 8.2 "Одинаковые объекты, которые Python считает разными", шаг 5

Класс `Card` описывает игральную карту. Программа считает, сколько раз выпала каждая карта, но
падает с ошибкой.

Найдите и исправьте ошибку.

Ввод. Несколько строк, в каждой достоинство и масть карты через пробел.

Вывод. Для каждой карты в порядке первого появления строка `достоинство масть количество`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    import sys

    class Card:
        def __init__(self, rank, suit):
            self.rank, self.suit = rank, suit

        def __eq__(self, other):
            return (self.rank, self.suit) == (other.rank, other.suit)


    counts = {}
    for line in sys.stdin.read().splitlines():
        card = Card(*line.split())
        counts[card] = counts.get(card, 0) + 1
    for card, n in counts.items():
        print(card.rank, card.suit, n)
"""

import sys

class Card:
    def __init__(self, rank, suit):
        self.rank, self.suit = rank, suit

    def __eq__(self, other):
        return (self.rank, self.suit) == (other.rank, other.suit)

    def __hash__(self):
        return hash((self.rank, self.suit))


counts = {}
for line in sys.stdin.read().splitlines():
    card = Card(*line.split())
    counts[card] = counts.get(card, 0) + 1
for card, n in counts.items():
    print(card.rank, card.suit, n)
