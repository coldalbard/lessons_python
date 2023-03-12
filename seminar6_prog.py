import random


# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12
# size1 = int(input("Please, enter size first array: "))
# size2 = int(input("Please, enter size second array: "))
# array1 = [random.randint(1, 10) for i in range(size1)]
# print(array1)
# array2 = [random.randint(1, 10) for i in range(size2)]
# print(array2)
# def count_array1(array1, array2):
#     lst = []
#     for i in range(len(array1)):
#         if array1[i] not in array2:
#             lst.append(array1[i])
#     return lst
# print(count_array1(array1, array2))




# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# вводится число N — количество элементов в массиве  Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.

# size1 = int(input("Please, enter size array: "))
# arr1 = [random.randint(1, 10) for i in range(size1)]
# print(arr1)
# def count_numbers(arr1):
#     count = 0
#     for i in range(1, len(arr1) - 1):
#         if arr1[i - 1] < arr1[i] > arr1[i + 1]:
#             count += 1
#     return count
# print(count_numbers(arr1))


# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
#
# len_array = int(input("Please, enter size array: "))
# arr1 = [random.randint(1, 10) for i in range(len_array)]
# print(arr1)
# def count(arr1):
#     count = 0
#     for i in range(len(arr1)):
#         for j in range(i + 1, len(arr1)):
#             if arr1[i] == arr1[j]:
#                 count += 1
#     return count
# print(count(arr1))


# 45)Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105.
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# def number_k():
#     K = int(input("Please, enter your K number: "))
#     if K > 10**5:
#         print("error")
#         return number_k()
#     return K
# K = number_k()
#
# def friend_numbers(K):
#     lst = []
#     for i in range(1, K):
#         summa = 0
#         for j in range(1, i):
#             if i % j == 0:
#                 summa += j
#         lst.append([i, summa])
#     return lst
# lst = friend_numbers(K)
# print(lst)
#
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i][0] == lst[j][1] and lst[i][1] == lst[j][0]:
#             print(lst[i][0], lst[j][0])


# lst = [(i, sum([j for j in range(1, i) if i % j == 0])) for i in range(1, 300)]
# for i in range(len(lst)):
#     for j in range(i, len(lst)):
#         if lst[i][1] == lst[j][0] and lst[j][1] == lst[i][0] and lst[i][0] != lst[i][1]:
#             print(lst[i])


# def func(number):
#     def friendly_number(num):
#         lst = []
#         for i in range(1, num//2 + 1):
#             if num % i == 0:
#                 lst.append(i)
#         return sum(lst)
#     num_1 = friendly_number(number)   # 284
#     num_2 = friendly_number(num_1)      # 220
#     if num_2 == number and num_1 != num_2:
#         print(number, num_1)
#
#
# for i in range(1, 10000):
#     func(i)



# На входе имеем список строк разной длины.
# Необходимо написать функцию all_eq(lst), которая вернет новый список из строк одинаковой длины.
# Длину итоговой строки определяем исходя из самой большой из них.
# Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов.
# Расположение элементов начального списка не менять.
# lst = ["fafsafa41654", "adsd", "qwer", "ac", "fghj"]
# def all_eq(lst):
#     len_max = lst[0]
#     for i in range(len(lst)):
#         if len(lst[i]) > len(len_max):
#             len_max = lst[i]
#     for j in range(len(lst)):
#         if len(len_max) > len(lst[j]):
#             lst[j] += "_" * (len(len_max) - len(lst[j]))
#     return lst
# print(all_eq(lst))



# cities = ['Moscow', 'Berlin', 'Minsk', 'Mongolia', 'Kanada', 'z']
# max_cities = max(cities, key=len)
# lst = [i if len(i) == len(max_cities) else i +
#        (len(max_cities) - len(i))*"_" for i in cities]
# print(lst)