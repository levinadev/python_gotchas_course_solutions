"""
Урок 5.3 "Словарь, который теряет ключи", шаг 5

Программа раскладывает слова по первой букве. Но в каждой группе оказываются все слова сразу.

Найдите и исправьте ошибку.

Ввод. Слова через пробел (строчными буквами).

Вывод. Для каждой буквы в алфавитном порядке строка `буква: слова`. Слова в группе идут в порядке
ввода.

Программа с ошибкой, которая лежит в редакторе на Stepik

    words = input().split()
    letters = sorted(set(w[0] for w in words))
    groups = dict.fromkeys(letters, [])
    for w in words:
        groups[w[0]].append(w)
    for letter in letters:
        print(f"{letter}:", *groups[letter])
"""

words = input().split()
letters = sorted(set(w[0] for w in words))
groups = {letter: [] for letter in letters}
for w in words:
    groups[w[0]].append(w)
for letter in letters:
    print(f"{letter}:", *groups[letter])
