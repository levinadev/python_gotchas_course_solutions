"""
Урок 8.1 "Изменился один объект, а за ним все", шаг 4

Класс `Playlist` хранит песни. Программа создаёт два плейлиста и выводит их, но во втором
оказываются песни из первого.

Найдите и исправьте ошибку.

Ввод. Две строки с названиями песен через пробел.

Вывод. Песни первого плейлиста, затем песни второго.

Программа с ошибкой, которая лежит в редакторе на Stepik

    class Playlist:
        songs = []

        def add(self, song):
            self.songs.append(song)


    first = Playlist()
    for s in input().split():
        first.add(s)
    second = Playlist()
    for s in input().split():
        second.add(s)
    print(*first.songs)
    print(*second.songs)
"""

class Playlist:
    def __init__(self):
        self.songs = []

    def add(self, song):
        self.songs.append(song)


first = Playlist()
for s in input().split():
    first.add(s)
second = Playlist()
for s in input().split():
    second.add(s)
print(*first.songs)
print(*second.songs)
