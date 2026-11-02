# Решения задач курса [Подводные камни Python](https://stepik.org/a/304053) на Stepik

В репозитории собраны все 77 задач курса на программирование. В одних задачах нужно найти и исправить ошибку в готовой программе, в других написать программу самому. В файле задачи есть условие, программа с ошибкой (если она была в редакторе) и решение, которое проходит проверку на Stepik. Репозиторий нужен, чтобы после решения задачи можно было сравнить свой код с вариантом автора курса.

## Как пользоваться

1. Сначала решите задачу сами и отправьте решение на Stepik.
2. Найдите файл задачи. Он лежит в папке модуля, внутри неё в папке урока и называется `step_NN.py`, где `NN` означает номер шага в уроке. Ссылки на все файлы есть в содержании ниже.
3. Сравните своё решение с решением из файла.

Если задача не получается, не открывайте решение сразу. Перечитайте теорию урока, запустите программу на своих данных и выведите через `print()` переменные, в которых сомневаетесь, посмотрите комментарии под шагом на Stepik. Подсмотренное решение почти ничему не учит.

## Как запустить решение

Нужен Python 3.10 или новее, сторонние библиотеки не нужны. Решения читают входные данные через `input()`, как на Stepik. Например, так запускается первая задача.

```bash
python 02_variables/01_what_a_variable_holds/step_05.py
```

или

```bash
python3 02_variables/01_what_a_variable_holds/step_05.py
```

После запуска введите данные с клавиатуры, как описано в условии в начале файла. Некоторые решения читают строки до конца ввода через `sys.stdin`. В них после последней строки нажмите `Ctrl+D` (в Windows `Ctrl+Z`, затем `Enter`).

## Содержание

Номер модуля в названии папки совпадает с номером модуля в курсе, а номер урока с номером урока внутри модуля.

### 2. Переменные

| Урок | Шаг | Файл |
|---|---|---|
| 2.1 Что на самом деле хранит переменная | 5 | [`02_variables/01_what_a_variable_holds/step_05.py`](02_variables/01_what_a_variable_holds/step_05.py) |
| 2.1 Что на самом деле хранит переменная | 6 | [`02_variables/01_what_a_variable_holds/step_06.py`](02_variables/01_what_a_variable_holds/step_06.py) |
| 2.1 Что на самом деле хранит переменная | 7 | [`02_variables/01_what_a_variable_holds/step_07.py`](02_variables/01_what_a_variable_holds/step_07.py) |
| 2.2 Один оператор, два разных результата | 7 | [`02_variables/02_one_operator_two_results/step_07.py`](02_variables/02_one_operator_two_results/step_07.py) |
| 2.2 Один оператор, два разных результата | 8 | [`02_variables/02_one_operator_two_results/step_08.py`](02_variables/02_one_operator_two_results/step_08.py) |
| 2.2 Один оператор, два разных результата | 9 | [`02_variables/02_one_operator_two_results/step_09.py`](02_variables/02_one_operator_two_results/step_09.py) |
| 2.3 Равны, но не одинаковы | 6 | [`02_variables/03_equal_but_not_identical/step_06.py`](02_variables/03_equal_but_not_identical/step_06.py) |
| 2.3 Равны, но не одинаковы | 7 | [`02_variables/03_equal_but_not_identical/step_07.py`](02_variables/03_equal_but_not_identical/step_07.py) |
| 2.3 Равны, но не одинаковы | 8 | [`02_variables/03_equal_but_not_identical/step_08.py`](02_variables/03_equal_but_not_identical/step_08.py) |

### 3. Списки

| Урок | Шаг | Файл |
|---|---|---|
| 3.1 Один список изменился, и второй тоже | 4 | [`03_lists/01_one_list_changed_both/step_04.py`](03_lists/01_one_list_changed_both/step_04.py) |
| 3.1 Один список изменился, и второй тоже | 5 | [`03_lists/01_one_list_changed_both/step_05.py`](03_lists/01_one_list_changed_both/step_05.py) |
| 3.1 Один список изменился, и второй тоже | 6 | [`03_lists/01_one_list_changed_both/step_06.py`](03_lists/01_one_list_changed_both/step_06.py) |
| 3.2 Копия есть, а данные общие | 5 | [`03_lists/02_copy_with_shared_data/step_05.py`](03_lists/02_copy_with_shared_data/step_05.py) |
| 3.2 Копия есть, а данные общие | 6 | [`03_lists/02_copy_with_shared_data/step_06.py`](03_lists/02_copy_with_shared_data/step_06.py) |
| 3.2 Копия есть, а данные общие | 7 | [`03_lists/02_copy_with_shared_data/step_07.py`](03_lists/02_copy_with_shared_data/step_07.py) |
| 3.3 Таблица, которая меняется целым столбцом | 5 | [`03_lists/03_table_changes_whole_column/step_05.py`](03_lists/03_table_changes_whole_column/step_05.py) |
| 3.3 Таблица, которая меняется целым столбцом | 6 | [`03_lists/03_table_changes_whole_column/step_06.py`](03_lists/03_table_changes_whole_column/step_06.py) |
| 3.3 Таблица, которая меняется целым столбцом | 7 | [`03_lists/03_table_changes_whole_column/step_07.py`](03_lists/03_table_changes_whole_column/step_07.py) |
| 3.4 Цикл, который пропускает элементы | 3 | [`03_lists/04_loop_skips_elements/step_03.py`](03_lists/04_loop_skips_elements/step_03.py) |
| 3.4 Цикл, который пропускает элементы | 4 | [`03_lists/04_loop_skips_elements/step_04.py`](03_lists/04_loop_skips_elements/step_04.py) |
| 3.4 Цикл, который пропускает элементы | 5 | [`03_lists/04_loop_skips_elements/step_05.py`](03_lists/04_loop_skips_elements/step_05.py) |

### 4. Функции

| Урок | Шаг | Файл |
|---|---|---|
| 4.1 Функция испортила чужой список | 5 | [`04_functions/01_function_spoiled_list/step_05.py`](04_functions/01_function_spoiled_list/step_05.py) |
| 4.1 Функция испортила чужой список | 6 | [`04_functions/01_function_spoiled_list/step_06.py`](04_functions/01_function_spoiled_list/step_06.py) |
| 4.1 Функция испортила чужой список | 7 | [`04_functions/01_function_spoiled_list/step_07.py`](04_functions/01_function_spoiled_list/step_07.py) |
| 4.2 Откуда в пустом списке старые данные | 5 | [`04_functions/02_old_data_in_empty_list/step_05.py`](04_functions/02_old_data_in_empty_list/step_05.py) |
| 4.2 Откуда в пустом списке старые данные | 6 | [`04_functions/02_old_data_in_empty_list/step_06.py`](04_functions/02_old_data_in_empty_list/step_06.py) |
| 4.2 Откуда в пустом списке старые данные | 7 | [`04_functions/02_old_data_in_empty_list/step_07.py`](04_functions/02_old_data_in_empty_list/step_07.py) |
| 4.3 Все функции вернули одно и то же | 4 | [`04_functions/03_all_functions_returned_same/step_04.py`](04_functions/03_all_functions_returned_same/step_04.py) |
| 4.3 Все функции вернули одно и то же | 5 | [`04_functions/03_all_functions_returned_same/step_05.py`](04_functions/03_all_functions_returned_same/step_05.py) |
| 4.3 Все функции вернули одно и то же | 6 | [`04_functions/03_all_functions_returned_same/step_06.py`](04_functions/03_all_functions_returned_same/step_06.py) |
| 4.4 Переменная есть, а Python её не видит | 4 | [`04_functions/04_variable_not_visible/step_04.py`](04_functions/04_variable_not_visible/step_04.py) |
| 4.4 Переменная есть, а Python её не видит | 5 | [`04_functions/04_variable_not_visible/step_05.py`](04_functions/04_variable_not_visible/step_05.py) |
| 4.4 Переменная есть, а Python её не видит | 6 | [`04_functions/04_variable_not_visible/step_06.py`](04_functions/04_variable_not_visible/step_06.py) |

### 5. Кортежи, строки, словари, множества

| Урок | Шаг | Файл |
|---|---|---|
| 5.1 Кортеж не то, чем кажется | 4 | [`05_tuples_strings_dicts_sets/01_tuple_is_not_what_it_seems/step_04.py`](05_tuples_strings_dicts_sets/01_tuple_is_not_what_it_seems/step_04.py) |
| 5.1 Кортеж не то, чем кажется | 5 | [`05_tuples_strings_dicts_sets/01_tuple_is_not_what_it_seems/step_05.py`](05_tuples_strings_dicts_sets/01_tuple_is_not_what_it_seems/step_05.py) |
| 5.1 Кортеж не то, чем кажется | 6 | [`05_tuples_strings_dicts_sets/01_tuple_is_not_what_it_seems/step_06.py`](05_tuples_strings_dicts_sets/01_tuple_is_not_what_it_seems/step_06.py) |
| 5.2 Метод сработал, а результат пропал | 4 | [`05_tuples_strings_dicts_sets/02_method_result_lost/step_04.py`](05_tuples_strings_dicts_sets/02_method_result_lost/step_04.py) |
| 5.2 Метод сработал, а результат пропал | 5 | [`05_tuples_strings_dicts_sets/02_method_result_lost/step_05.py`](05_tuples_strings_dicts_sets/02_method_result_lost/step_05.py) |
| 5.2 Метод сработал, а результат пропал | 6 | [`05_tuples_strings_dicts_sets/02_method_result_lost/step_06.py`](05_tuples_strings_dicts_sets/02_method_result_lost/step_06.py) |
| 5.3 Словарь, который теряет ключи | 5 | [`05_tuples_strings_dicts_sets/03_dict_loses_keys/step_05.py`](05_tuples_strings_dicts_sets/03_dict_loses_keys/step_05.py) |
| 5.3 Словарь, который теряет ключи | 6 | [`05_tuples_strings_dicts_sets/03_dict_loses_keys/step_06.py`](05_tuples_strings_dicts_sets/03_dict_loses_keys/step_06.py) |
| 5.3 Словарь, который теряет ключи | 7 | [`05_tuples_strings_dicts_sets/03_dict_loses_keys/step_07.py`](05_tuples_strings_dicts_sets/03_dict_loses_keys/step_07.py) |
| 5.4 Что скрывают фигурные скобки | 4 | [`05_tuples_strings_dicts_sets/04_curly_braces/step_04.py`](05_tuples_strings_dicts_sets/04_curly_braces/step_04.py) |
| 5.4 Что скрывают фигурные скобки | 5 | [`05_tuples_strings_dicts_sets/04_curly_braces/step_05.py`](05_tuples_strings_dicts_sets/04_curly_braces/step_05.py) |
| 5.4 Что скрывают фигурные скобки | 6 | [`05_tuples_strings_dicts_sets/04_curly_braces/step_06.py`](05_tuples_strings_dicts_sets/04_curly_braces/step_06.py) |

### 6. Числа и логика

| Урок | Шаг | Файл |
|---|---|---|
| 6.1 Простая сумма с неверным ответом | 4 | [`06_numbers_and_logic/01_simple_sum_wrong_answer/step_04.py`](06_numbers_and_logic/01_simple_sum_wrong_answer/step_04.py) |
| 6.1 Простая сумма с неверным ответом | 5 | [`06_numbers_and_logic/01_simple_sum_wrong_answer/step_05.py`](06_numbers_and_logic/01_simple_sum_wrong_answer/step_05.py) |
| 6.1 Простая сумма с неверным ответом | 6 | [`06_numbers_and_logic/01_simple_sum_wrong_answer/step_06.py`](06_numbers_and_logic/01_simple_sum_wrong_answer/step_06.py) |
| 6.2 Округление не как в школе | 4 | [`06_numbers_and_logic/02_rounding_not_like_at_school/step_04.py`](06_numbers_and_logic/02_rounding_not_like_at_school/step_04.py) |
| 6.2 Округление не как в школе | 5 | [`06_numbers_and_logic/02_rounding_not_like_at_school/step_05.py`](06_numbers_and_logic/02_rounding_not_like_at_school/step_05.py) |
| 6.2 Округление не как в школе | 6 | [`06_numbers_and_logic/02_rounding_not_like_at_school/step_06.py`](06_numbers_and_logic/02_rounding_not_like_at_school/step_06.py) |
| 6.3 Минус в делении меняет ответ | 4 | [`06_numbers_and_logic/03_minus_in_division/step_04.py`](06_numbers_and_logic/03_minus_in_division/step_04.py) |
| 6.3 Минус в делении меняет ответ | 5 | [`06_numbers_and_logic/03_minus_in_division/step_05.py`](06_numbers_and_logic/03_minus_in_division/step_05.py) |
| 6.3 Минус в делении меняет ответ | 6 | [`06_numbers_and_logic/03_minus_in_division/step_06.py`](06_numbers_and_logic/03_minus_in_division/step_06.py) |
| 6.4 Условие, которое срабатывает всегда | 5 | [`06_numbers_and_logic/04_condition_always_true/step_05.py`](06_numbers_and_logic/04_condition_always_true/step_05.py) |
| 6.4 Условие, которое срабатывает всегда | 6 | [`06_numbers_and_logic/04_condition_always_true/step_06.py`](06_numbers_and_logic/04_condition_always_true/step_06.py) |
| 6.4 Условие, которое срабатывает всегда | 7 | [`06_numbers_and_logic/04_condition_always_true/step_07.py`](06_numbers_and_logic/04_condition_always_true/step_07.py) |

### 7. Циклы и итераторы

| Урок | Шаг | Файл |
|---|---|---|
| 7.1 Что остаётся после цикла | 5 | [`07_loops_and_iterators/01_what_remains_after_loop/step_05.py`](07_loops_and_iterators/01_what_remains_after_loop/step_05.py) |
| 7.1 Что остаётся после цикла | 6 | [`07_loops_and_iterators/01_what_remains_after_loop/step_06.py`](07_loops_and_iterators/01_what_remains_after_loop/step_06.py) |
| 7.1 Что остаётся после цикла | 7 | [`07_loops_and_iterators/01_what_remains_after_loop/step_07.py`](07_loops_and_iterators/01_what_remains_after_loop/step_07.py) |
| 7.2 Второй проход ничего не находит | 5 | [`07_loops_and_iterators/02_second_pass_finds_nothing/step_05.py`](07_loops_and_iterators/02_second_pass_finds_nothing/step_05.py) |
| 7.2 Второй проход ничего не находит | 6 | [`07_loops_and_iterators/02_second_pass_finds_nothing/step_06.py`](07_loops_and_iterators/02_second_pass_finds_nothing/step_06.py) |
| 7.2 Второй проход ничего не находит | 7 | [`07_loops_and_iterators/02_second_pass_finds_nothing/step_07.py`](07_loops_and_iterators/02_second_pass_finds_nothing/step_07.py) |
| 7.3 Данные пропали без единой ошибки | 4 | [`07_loops_and_iterators/03_data_lost_without_errors/step_04.py`](07_loops_and_iterators/03_data_lost_without_errors/step_04.py) |
| 7.3 Данные пропали без единой ошибки | 5 | [`07_loops_and_iterators/03_data_lost_without_errors/step_05.py`](07_loops_and_iterators/03_data_lost_without_errors/step_05.py) |
| 7.3 Данные пропали без единой ошибки | 6 | [`07_loops_and_iterators/03_data_lost_without_errors/step_06.py`](07_loops_and_iterators/03_data_lost_without_errors/step_06.py) |

### 8. Классы

| Урок | Шаг | Файл |
|---|---|---|
| 8.1 Изменился один объект, а за ним все | 4 | [`08_classes/01_one_object_changed_all/step_04.py`](08_classes/01_one_object_changed_all/step_04.py) |
| 8.1 Изменился один объект, а за ним все | 5 | [`08_classes/01_one_object_changed_all/step_05.py`](08_classes/01_one_object_changed_all/step_05.py) |
| 8.1 Изменился один объект, а за ним все | 6 | [`08_classes/01_one_object_changed_all/step_06.py`](08_classes/01_one_object_changed_all/step_06.py) |
| 8.2 Одинаковые объекты, которые Python считает разными | 4 | [`08_classes/02_equal_objects_seen_as_different/step_04.py`](08_classes/02_equal_objects_seen_as_different/step_04.py) |
| 8.2 Одинаковые объекты, которые Python считает разными | 5 | [`08_classes/02_equal_objects_seen_as_different/step_05.py`](08_classes/02_equal_objects_seen_as_different/step_05.py) |
| 8.2 Одинаковые объекты, которые Python считает разными | 6 | [`08_classes/02_equal_objects_seen_as_different/step_06.py`](08_classes/02_equal_objects_seen_as_different/step_06.py) |

### 9. Финал

| Урок | Шаг | Файл |
|---|---|---|
| 9.1 Всё вместе | 6 | [`09_final/01_all_together/step_06.py`](09_final/01_all_together/step_06.py) |
| 9.1 Всё вместе | 7 | [`09_final/01_all_together/step_07.py`](09_final/01_all_together/step_07.py) |
| 9.1 Всё вместе | 8 | [`09_final/01_all_together/step_08.py`](09_final/01_all_together/step_08.py) |
| 9.1 Всё вместе | 9 | [`09_final/01_all_together/step_09.py`](09_final/01_all_together/step_09.py) |
| 9.1 Всё вместе | 10 | [`09_final/01_all_together/step_10.py`](09_final/01_all_together/step_10.py) |
