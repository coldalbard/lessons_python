import random


# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# 1 решение
# num_list = [1, 1, 2, 0, -1, 3, 4, 4]
# count = 1
# for i in range(len(num_list)):
#     if num_list[i] != num_list[count]:
#         count += 1
#     i += 1
# print(count)

# 2 решение
# test = [1, 1, 2, 0, -1, 3, 4, 4]
# test_list = []
# count2 = 0
# for num in test:
#     if num not in test_list:
#         test_list.append(num)
#         count2 += 1
# print(f"{test_list} \n{count2}")

# 3 решение
# list1 = [1, 1, 2, 0, -1, 3, 4, 4]
# list1 = set(list1)
# print(list1)




# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# # 1 решение
# list2 = [1, 2, 3, 4, 5]
# k = 3
# new_list2 = []
#
# for i in range(k, len(list2)):
#     new_list2.append(list2[i])
# for j in range(k):
#     new_list2.append(list2[j])
# print(new_list2)

# # 2 решение
# list_new = [1, 2, 3, 4, 5]
# k2 = 3
# temp = 0
# for i in range(len(list_new) - k2):
#     temp = list_new[i]
#     list_new[i] = list_new[k2]
#     list_new[k2] = temp
#     k2 += 1
# print(list_new)

# 3 решение
# numbers_list2 = [1, 2, 3, 4, 5, 6, 7]
# num_k = 3
# numbers_new_list = []
# temp2 = []
# for num in numbers_list2:
#     if num_k > 0:
#         temp2.append(num)
#         num_k -= 1
#     else:
#         numbers_new_list.append(num)
# numbers_new_list += temp2
# print(numbers_new_list)

# 4 решение
# new_list2 = [1, 2, 3, 4, 5, 6, 7]
# num_list2 = []
# num2_k = 3
# num_list2 = new_list2[-num2_k:] + new_list2[:-num2_k]
# print(num_list2)




# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# # Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# # Примечание: Список словарей задан изначально.
# # Пользователь его не вводит

# # 1 решение
# dictionary_test = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {"V": "S009"}, {"VIII": "S007"}]
# res = []
# for item in dictionary_test:
#     item = item.values()
#     for i in item:
#         if i not in res:
#             res.append(i.strip(' '))
# print(set(res))

# # 2 решение
# lst2 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {"V": "S009"}, {"VIII": "S007"}]
# res2 = set([value.strip() for diction in lst2 for value in diction.values()])
# print(res2)


# Задача. Создайте список случайных чисел. Найдите номер его последнего локального
# максимума (локальный максимум - это элемент который, больше любого
# из своих соседей)

# test_list2 = []
# max = 0
#
# for i in range(8):
#     test_list2.append(random.randint(1, 15))
# print(test_list2)
#
# for i in range(len(test_list2)):
#     if test_list2[i - 1] < test_list2[i] > test_list2[i + 1]:
#         max = i
# print(max)




# 3.Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2

# test_list3 = []
#
# for i in range(8):
#    test_list3.append(random.randint(1, 15))
# print(test_list3)
# #
# max = test_list3[0]
# max2 = test_list3[0]
#
# for i in range(len(test_list3)):
#     if test_list3[i] > max:
#       max = test_list3[i]
#     if max2 < test_list3[i] < max:
#        max2 = test_list3[i]
# print(max, max2)



# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает
# количество элементов массива, больших предыдущего
# (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2
# Пояснение: (-1 < 5, 2 < 3)

# lst = []
# for i in range(8):
#     lst.append(random.randint(1, 15))
# print(lst)
#
# counter = 0
#
# for i in range(1, len(lst)):
#     if lst[i - 1] < lst[i]:
#         print(lst[i - 1], '<', lst[i])
#         counter += 1
# print(counter)



# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X


