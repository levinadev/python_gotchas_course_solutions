"""
Урок 4.4 "Переменная есть, а Python её не видит", шаг 6

Функция `write` дописывает событие в журнал `log`, это строка, где события разделены точкой с
запятой. Программа падает с ошибкой.

Исправьте программу, объявив переменную глобальной через `global`.

Ввод. События через пробел.

Вывод. Журнал, после каждого события стоит `;`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    log = ""

    def write(event):
        log += event + ";"

    for event in input().split():
        write(event)
    print(log)
"""

log = ""

def write(event):
    global log
    log += event + ";"

for event in input().split():
    write(event)
print(log)
