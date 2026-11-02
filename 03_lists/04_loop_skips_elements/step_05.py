"""
Урок 3.4 "Цикл, который пропускает элементы", шаг 5

Имя `shared` указывает на тот же список, что и `nums`. Удалите из `nums` все числа, равные `x`, так,
чтобы изменения увидело имя `shared`. Новый список создавать нельзя.

Ввод. Строка с целыми числами через пробел, затем строка с числом `x`.

Вывод. Элементы `shared` через пробел или `пусто`, если список опустел.

Программа с ошибкой, которая лежит в редакторе на Stepik

    nums = list(map(int, input().split()))
    shared = nums
    x = int(input())

    # удалите из nums все числа x

    print(*shared if shared else ["пусто"])
"""

nums = list(map(int, input().split()))
shared = nums
x = int(input())

for value in nums[:]:
    if value == x:
        nums.remove(value)

print(*shared if shared else ["пусто"])
