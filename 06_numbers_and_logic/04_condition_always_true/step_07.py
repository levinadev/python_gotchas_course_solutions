"""
Урок 6.4 "Условие, которое срабатывает всегда", шаг 7

Если скидка не указана (пустая строка), действует скидка 10%. Скидка 0 означает, что скидки нет. Но
при скидке 0 программа всё равно отнимает 10%.

Найдите и исправьте ошибку.

Ввод. Две строки, скидка в процентах (может быть пустой) и цена, целое число.

Вывод. Цена со скидкой, `price * (100 - discount) // 100`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    raw = input()
    price = int(input())
    discount = int(raw) if raw else None
    discount = discount or 10
    print(price * (100 - discount) // 100)
"""

raw = input()
price = int(input())
discount = int(raw) if raw else None
if discount is None:
    discount = 10
print(price * (100 - discount) // 100)
