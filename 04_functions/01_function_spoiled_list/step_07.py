"""
Урок 4.1 "Функция испортила чужой список", шаг 7

Допишите функцию `without_min(nums)`. Она возвращает новый список без одного наименьшего числа
(первого из наименьших, если их несколько) и не меняет переданный список.

Ввод. Целые числа через пробел.

Вывод. Две строки, исходный список и результат функции. Если в результате ничего не осталось, во
второй строке выведите `пусто`.

Программа с ошибкой, которая лежит в редакторе на Stepik

    def without_min(nums):
        # напишите код функции
        pass


    data = list(map(int, input().split()))
    rest = without_min(data)
    print(*data)
    print(*rest if rest else ["пусто"])
"""

def without_min(nums):
    result = nums.copy()
    result.remove(min(result))
    return result


data = list(map(int, input().split()))
rest = without_min(data)
print(*data)
print(*rest if rest else ["пусто"])
