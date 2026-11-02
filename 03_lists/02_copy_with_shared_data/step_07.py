"""
Урок 3.2 "Копия есть, а данные общие", шаг 7

Считайте состав отделов, по строке на отдел, и последней строкой перевод сотрудника в формате `имя
номер`. Создайте новую структуру, в которой сотрудник ушёл из своего отдела и встал в конец отдела с
этим номером (нумерация с единицы). Исходная структура должна остаться прежней.

Ввод. Несколько строк с именами через пробел, затем строка перевода. Сотрудник переходит в другой
отдел.

Вывод. Отделы до перевода, строка `---`, отделы после перевода. Отдел, в котором никого не осталось,
выводится словом `пусто`.
"""

import copy
import sys

lines = sys.stdin.read().splitlines()
before = [line.split() for line in lines[:-1]]
name, number = lines[-1].split()
after = copy.deepcopy(before)
for dept in after:
    if name in dept:
        dept.remove(name)
after[int(number) - 1].append(name)
for dept in before:
    print(*dept)
print("---")
for dept in after:
    print(*dept if dept else ["пусто"])
