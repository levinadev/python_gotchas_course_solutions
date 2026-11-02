"""
Урок 3.2 "Копия есть, а данные общие", шаг 5

Программа хранит поле 3×3 для игры в крестики-нолики и его снимок до хода. После хода снимок должен
остаться прежним, но он почему-то меняется вместе с полем.

Найдите и исправьте ошибку.

Ввод. Три строки по три символа (`.`, `X` или `O`), затем строка с номером строки и столбца хода (от
0 до 2) через пробел. Ход делает `X`.

Вывод. Снимок поля до хода, пустая строка, поле после хода.

Программа с ошибкой, которая лежит в редакторе на Stepik

    board = [list(input()) for _ in range(3)]
    before = board.copy()
    r, col = map(int, input().split())
    board[r][col] = "X"
    for row in before:
        print("".join(row))
    print()
    for row in board:
        print("".join(row))
"""

board = [list(input()) for _ in range(3)]
before = [row[:] for row in board]
r, col = map(int, input().split())
board[r][col] = "X"
for row in before:
    print("".join(row))
print()
for row in board:
    print("".join(row))
