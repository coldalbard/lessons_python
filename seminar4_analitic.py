import random


# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
# text = [i for i in input().split()]


# input_string = input()
# words = input_string.split()
#
# output_string = ""
# counts = {}
# for word in words:
#     if word in counts:
#         counts[word] += 1
#         output_string += word + "_" + str(counts[word] - 1) + " "
#     else:
#         counts[word] = 1
#         output_string += word + " "
# print(output_string)


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# 1 решение
# text = [i.upper() for i in input().split()]
# new_text = []
# for i in text:
#     if i not in new_text:
#         new_text += i.split()
# print(len(new_text))

# 2 решение
# text = [i for i in input().split()]
# text1 = set(text)
# print(len(text1))




# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Примечание: Программные коды на следующих
# слайдах

# 1 решение

# max_number = -1
# while (n := random.randint(0, 15)) != 0:
#     print(n)
#     if n > max_number:
#         max_number = n
# print(n)
# print(max_number)


# 2 решение

# numbers = None
# max_number = -1
# while numbers != 0:
#     numbers = int(input())
#     if max_number < numbers:
#         max_number = numbers
# print(max_number)
