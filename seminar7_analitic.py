# адача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает,
# когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Пример ввода и вывода данных представлены на следующем
# слайде

# 1 решение
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformation = lambda x: x
# transormed_values = list(map(transformation, values))
# print(transormed_values)

# 2 решение
# transormed_values = list(map(lambda x: x, values))
# print(transormed_values)
# if values == transormed_values:
#     print("YES")
# else:
#     print("NO")


# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде]

# list_of_orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# 1 решение
# def find_farthest_orbit(list_of_orbits):
#     max_orbits = 0
#     index_orbits = 0
#     for i in range(len(list_of_orbits)):
#         if list_of_orbits[i][0] * list_of_orbits[i][1] > max_orbits \
#                 and list_of_orbits[i][0] != list_of_orbits[i][1]:
#             index_orbits = list_of_orbits[i]
#             max_orbits = list_of_orbits[i][0] * list_of_orbits[i][1]
#     return index_orbits
# print(find_farthest_orbit(list_of_orbits))

# 2 решение
# def find_farthest_orbit(list_of_orbits):
#     return max(list_of_orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1])
# list_of_orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(list_of_orbits))


# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# 1 решение
# values = [0, 1, 10, 6]
# def same_by(values):
#     count = 0
#     for i in range(len(values)):
#         if values[i] % 2 == 0:
#             count += 1
#     if count == len(values):
#         print("YES")
#     else:
#         print("NO")
# same_by(values)


# 2 решение
# values = [0, 2, 10, 6]
# def same_boy(f, val):
#     return len(set([f(x) for x in val])) == 1
#
# if same_boy(lambda x: x % 2, values):
#     print("YES")
# else:
#     print("NO")