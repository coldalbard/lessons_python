# Задача 34:  Винни-Пух попросил Вас посмотреть,
# есть ли в его стихах ритм. Поскольку разобраться
# в его кричалках не настолько просто, насколько легко
# он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе
# стихотворения одинаковое. Фраза может состоять
# из одного слова, если во фразе несколько слов,
# то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
# **Вывод:** Парам пам-пам



# 1 решение(в лоб))
# vowel_letters = ["а", "о", "у", "ы", "э", "е", "ё", "и", "ю", "я"]
# text = input("Please enter your text: ").lower().split()
# count1 = 0
# count = 0
# print(f'Vowel letters: {vowel_letters}')
#
# for i in range(len(text)):
#     for j in range(len(text[i])):
#         if text[i][j] in vowel_letters:
#             count1 += 1
#             if count == 0 and j == len(text[i]) - 2:
#                 count = count1
# if count1 / count == len(text): # если наше общее количество
#     # гласных букв разделить на количество гласных букв любого из слов
#     # ответ должен быть количеством наших слов)
#     print("there is a rhythm: Парам пам-пам)")
# else:
#     print("there is no rhythm: Пам парам(")



# 2 решение
# без циклов и по читабельнее выглядит, но идею нашел в интернете(

# vowel_letters = ["а", "о", "у", "ы", "э", "е", "ё", "и", "ю", "я"]
# text = "пара-ра-рам рам-пам-папам па-ра-па-да".lower().split()
# print(f'Vowel letters: {vowel_letters}')
# def rhythm(text, vowel_letters):
#     count = lambda x: sum(1 for i in x if i in vowel_letters)
#     tmp = count(text[0])
#     if all([count(i) == tmp for i in text]):
#         return "there is a rhythm: Парам пам-пам)"
#     return "there is no rhythm: Пам парам("
# print(rhythm(text, vowel_letters))








# Задача 36: Напишите функцию print_operation_table
# (operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число
# строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36



# 1 решение
# def print_operation_table(num_rows, num_columns):
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_columns + 1):
#             print(i * j, end="\t")
#         print()
# print(print_operation_table(6, 6))


# 2 решение, по сути отличие только в lambda и operation
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_columns + 1):
#             print(*list(map(operation, [i], [j])), end="\t")
#         print()
# print(print_operation_table(lambda x, y: x * y))