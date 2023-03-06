# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()


# text = "a a a b c a a d c d d"
# text_lst = text.split()
# new_lst = []
# for i in range(len(text_lst)):
#     if text_lst[i] in text_lst[:i]:
#         new_lst.append(text_lst[i]+"_"+str(text_lst[:i].count(text_lst[i])))
#     else:
#         new_lst.append(text_lst[i])
# print(', '.join(new_lst))



# *доп. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и вывести его в терминал.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# значениея выражения можно записать в виде:
# 2*x^2+5=0
# (если коэффициент равен 0 - значение не пишется,)



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Сжатие:
# 111222334 -> 31322414
# aaabbbbbccd -> 3a3b2c1d
# Восстановление:
# 31322414 ->111222334
# 3a3b2c1d->aaabbbbbccd

# lst = [int(i) for i in input().split()]
# res = []
# count = 0
# for i in range(1, len(lst)):
#     if lst[i - 1] == lst[i]:
#         count += 1
#     if lst[i - 1] != lst[i]:
#         res += lst[i]
#         res += count
#         count = 1
# print(res)

# def shifr(number):
#     lst = []
#     for i in range(len(number)-1):
#         if number[i] != number[i+1]:
#             lst.append(str(number[:i+1].count(number[i]))+str(number[i]))
#     lst.append(str(number.count(number[-1])) + str(number[-1]))
#     return ''.join(lst)
#
#
# def deshifr(number):
#     lst = []
#     i = 0
#     j = 1
#     while i < len(number)-1:
#         lst.append(int(number[i])*number[j])
#         i += 2
#         j += 2
#     return ''.join(lst)
#
#
#
# choice = input('Нужна шифровка или дешифровка? (ш, д): ').lower()
# num = input('Введите натуральное число: ')
# if choice == 'ш':
#     print(shifr(num))
# else:
#     print(deshifr(num))
#
# num = input('Введите натуральное число: ')
#
# print(deshifr(num))