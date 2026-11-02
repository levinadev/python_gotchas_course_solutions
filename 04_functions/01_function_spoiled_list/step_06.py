"""
Урок 4.1 "Функция испортила чужой список", шаг 6

Функция `clean` должна привести имена гостей к аккуратному виду, то есть убрать пробелы по краям и
сделать первую букву заглавной, остальные строчными. Но программа выводит имена в исходном виде.

Найдите и исправьте ошибку. Подойдёт любой способ из урока.

Ввод. Имена через запятую, вокруг имён могут быть пробелы.

Вывод. Аккуратные имена через запятую и пробел.

Программа с ошибкой, которая лежит в редакторе на Stepik

    def clean(names):
        names = [name.strip().capitalize() for name in names]

    guests = input().split(",")
    clean(guests)
    print(*guests, sep=", ")
"""

def clean(names):
    for i in range(len(names)):
        names[i] = names[i].strip().capitalize()

guests = input().split(",")
clean(guests)
print(*guests, sep=", ")
