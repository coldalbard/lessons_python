# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# 3 3 2 12 (каждое число вводится с новой строки)
import random


# array1 = [int(i) for i in input().split()]
# array2 = [int(i) for i in input().split()]
# lst = []
# print(array1)
# print(array2)
# def unique_first_array(array1, array2):
#     for i in range(len(array1)):
#         if array1[i] not in array2:
#             lst.append(i)
#     print(lst)
# unique_first_array(array1, array2)


# n = int(input())
# m = int(input())
# a = [random.randint(1, 10) for i in range(n)]
# print(a)
# b = [random.randint(1, 10) for i in range(m)]
# print(b)
# def findMissing(a, b, n, m):
#     for i in range(n):
#         for j in range(m):
#             if (a[i] == b[j]):
#                 break
#         if (j == m - 1):
#             print(a[i], end=" ")
# print(findMissing(a, b, n, m))



# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5
# 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

# size1 = int(input())
# size2 = int(input())
# lst1 = [random.randint(1, 10) for i in range(size1)]
# print(lst1)
# lst2 = [random.randint(1, 10) for i in range(size2)]
# print(lst2)
# def CountNumbers(size, lst):
#     count = 0
#     for i in range(size - 1):
#         if 0 < i < size and lst[i - 1] < lst[i] > lst[i + 1]:
#             count += 1
#         elif i == size and lst[i - 1] < lst[i] > lst[0]:
#             count += 1
#         elif i == 0 and lst[i] < lst[i + 1] > lst[-1]:
#             count += 1
#     return count
# print(CountNumbers(size1, lst1))
# print(CountNumbers(size2, lst2))




# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 5 2 5 5 5 5
# 2
# new_array = [int(i) for i in input().split()]
# def PairsElements(array):
#     count = 0
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             if array[i] == array[j]:
#                 count += 1
#     return count
# print(PairsElements(new_array))

# 2 решение
# n = [1, 3, 6, 4, 9, 7, 9, 12, 24, 4, 22, 5, 5, 5, 5, 33, 12, 5, 4]
# count = 0
# for i in range(len(n)):
#     count += n[i+1:].count(n[i])
# print(count)





# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284

# def number():
#     print("Please, enter your number: ")
#     K = int(input())
#     if K > 10**5:
#         print("error")
#         return number()
#     else:
#         return K
# K = number()

