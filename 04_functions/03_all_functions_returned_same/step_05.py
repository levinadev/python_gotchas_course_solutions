"""
Урок 4.3 "Все функции вернули одно и то же", шаг 5

Программа создаёт для каждого гостя функцию-приветствие через `def`, а потом вызывает их по очереди.
Но все функции здороваются с последним гостем.

Найдите и исправьте ошибку.

Ввод. Имена гостей через пробел.

Вывод. Для каждого гостя строка `Привет, <имя>!`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    names = input().split()
    greetings = []
    for name in names:
        def greet():
            return f"Привет, {name}!"
        greetings.append(greet)
    for g in greetings:
        print(g())
"""

names = input().split()
greetings = []
for name in names:
    def greet(name=name):
        return f"Привет, {name}!"
    greetings.append(greet)
for g in greetings:
    print(g())
