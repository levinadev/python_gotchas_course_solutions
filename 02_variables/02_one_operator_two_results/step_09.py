"""
Урок 2.2 "Один оператор, два разных результата", шаг 9

Имя `archive` указывает на тот же список писем, что и `inbox`. Добавьте в `inbox` новые письма из
второй строки так, чтобы их увидело и имя `archive`.

Ввод. Две строки, в каждой названия писем через пробел.

Вывод. Число писем до добавления, затем письма из `archive` через пробел.

Программа с ошибкой, которая лежит в редакторе на Stepik

    inbox = input().split()
    archive = inbox
    count_before = len(inbox)
    new = input().split()

    # добавьте письма из new в inbox

    print(count_before)
    print(*archive)
"""

inbox = input().split()
archive = inbox
count_before = len(inbox)
new = input().split()

inbox += new

print(count_before)
print(*archive)
