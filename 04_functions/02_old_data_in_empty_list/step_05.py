"""
Урок 4.2 "Откуда в пустом списке старые данные", шаг 5

Функция `make_team` собирает команду, то есть добавляет капитана в список участников и возвращает
его. Для каждой строки ввода нужна отдельная команда, но команды почему-то "слипаются".

Найдите и исправьте ошибку.

Ввод. Несколько строк. В каждой строке имя капитана, затем имена остальных участников через пробел.

Вывод. Для каждой строки участники команды через пробел, сначала остальные, капитан в конце.

Программа с ошибкой, которая лежит в редакторе на Stepik

    import sys

    def make_team(captain, members=[]):
        members.append(captain)
        return members

    for line in sys.stdin.read().splitlines():
        captain, *others = line.split()
        team = make_team(captain, others) if others else make_team(captain)
        print(*team)
"""

import sys

def make_team(captain, members=None):
    if members is None:
        members = []
    members.append(captain)
    return members

for line in sys.stdin.read().splitlines():
    captain, *others = line.split()
    team = make_team(captain, others) if others else make_team(captain)
    print(*team)
