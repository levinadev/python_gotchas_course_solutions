"""
Урок 8.1 "Изменился один объект, а за ним все", шаг 6

Каждый новый билет должен получать следующий номер, 1, 2, 3 и так далее, а класс `Ticket` должен
помнить, сколько билетов выдано. Но у всех билетов номер 1, а выдано, по словам класса, ноль.

Найдите и исправьте ошибку.

Ввод. Имена владельцев билетов через пробел.

Вывод. Для каждого билета строка `номер имя`, затем строка `Всего выдано N`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    class Ticket:
        issued = 0

        def __init__(self, owner):
            self.issued += 1
            self.owner = owner
            self.number = self.issued


    tickets = [Ticket(name) for name in input().split()]
    for t in tickets:
        print(t.number, t.owner)
    print("Всего выдано", Ticket.issued)
"""

class Ticket:
    issued = 0

    def __init__(self, owner):
        Ticket.issued += 1
        self.owner = owner
        self.number = Ticket.issued


tickets = [Ticket(name) for name in input().split()]
for t in tickets:
    print(t.number, t.owner)
print("Всего выдано", Ticket.issued)
