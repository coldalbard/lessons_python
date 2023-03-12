
# def calk2(a, b):
#     return a * b
# def math(op, x, y):
#     print(op(x, y))
#
# math(lambda a, b: a + b, 5, 45)








# lst = [1, 2, 3, 5, 8, 15, 23, 38]
# def n(lst):
#     lst2 = []
#     for i in range(len(lst)):
#         if lst[i] % 2 == 0:
#             lst2.append((lst[i], lst[i] * lst[i]))
#     return lst2
# print(n(lst))


# lst = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list(map(int, lst))
# print(res)
# res = list(filter(lambda x: x % 2 == 0, res))
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)









# list1 = [x for x in range(1, 20)]
# print(list1)
# list1 = list(map(lambda x: x + 10, list1))
# print(list1)


# array = "1, 2, 3, 5, 8, 15, 23, 38"
# array = list(map(int, array.split(",")))
# print(array)








# new_arr = [15, 65, 9, 6, 75]
# res = list(filter(lambda x: x % 10 == 5, new_arr))
# print(res)






# 1. Режим a
# a – открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл,
# то файл будет создан и в него начнется запись

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()



# w – открытие для записи данных.
# ○ Позволяет записывать данные и создавать файл, если его не существует.

# with open('file.txt', 'w') as data:
#    data.write('line 1\n')
#    data.write('line 2\n')



# 2. Режим r
# ● Чтение данных из файла:

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()



# 3. Режим w
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()


