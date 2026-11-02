"""
Урок 4.2 "Откуда в пустом списке старые данные", шаг 6

Для каждого слова программа выводит, сколько раз в нём встречается самая частая буква. Для первого
слова ответ верный, а дальше числа получаются слишком большими.

Найдите и исправьте ошибку.

Ввод. Несколько строк, в каждой одно слово.

Вывод. Для каждого слова строка, само слово и число через пробел.

Программа с ошибкой, которая лежит в редакторе на Stepik

    import sys

    def count_letters(word, counts={}):
        for ch in word:
            counts[ch] = counts.get(ch, 0) + 1
        return counts

    for word in sys.stdin.read().split():
        counts = count_letters(word)
        print(word, max(counts.values()))
"""

import sys

def count_letters(word, counts=None):
    if counts is None:
        counts = {}
    for ch in word:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

for word in sys.stdin.read().split():
    counts = count_letters(word)
    print(word, max(counts.values()))
