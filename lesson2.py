# list1 = []
# list2 = list()
# list3 = [1, 2, 3, 45, 5, 6, 7]
# print(f"list1 type = {type(list1)} \nlist1 = {list1} \nlist2 type = {type(list2)} \nlist2 = {list2}")
# print(f"list3 type = {type(list3)} \nlist3 = {list3}")
# списки






# newList = [1, 2]
# print(newList)
# newList.append(26)
# print(newList)
# пример добавления в конец списка






# newList2 = []
# print(newList2)
# for i in range(5):
#     newList2.append(i)
#     print(newList2)
# пример добавления в список с помощью цикла







'''
list_1 = [12, 7, -1, 21, 0]
print(list_1.pop()) # 0
print(list_1) # [12, 7, -1, 21]
print(list_1.pop()) # 21
print(list_1) # [12, 7, -1]
print(list_1.pop()) # -1
print(list_1) # [12, 7]
print(list_1.pop(1)) # удаление числа по индексу. Индекс 7-ки= 1
print(list_1)
'''
# пример удаления последнего элемента списка или удаление по индексу.









# testList = [12, 7, -1, 21, 0]
# print(testList)
# testList.insert(2, 11)
# # 1-e значение в insert это индекс
# # в который мы хотим добавить элемент. А 2-е значение это
# # сам элемент который мы добавляем
# print(testList) # [12, 7, 11, -1, 21, 0]
# # пример добавления элемента в список по индексу.







'''
newListTest = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(newListTest[0]) # 1
print(newListTest[1]) # 2
print(newListTest[len(newListTest) - 1]) # 10
print(newListTest[-5]) # 6
print(newListTest[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(newListTest[:2]) # [1, 2]
print(newListTest[len(newListTest) - 2:]) #[9, 10]
print(newListTest[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(newListTest[6:-18]) # []
print(newListTest[0:len(newListTest):6]) # [1, 7]
print(newListTest[::6]) # [1, 7]
# пример среза списков
'''








# t = ()
# print(type(t))
# t = (1, 2)
# print(type(t))

# v = [1, 8, 9]
# # print(v)
# # print(type(v))
# v = tuple(v)
# # обозначаем переменную v как кортеж, до этого наша перемнная была списком
# print(type(v))
# # кортежей и их присваивания

# a, b, c = v # пример множественного присваивания
# print(type(a))
# print(a, b, c) # каждой перемнной мы назчаем по элементу из кортежа v
# # причем переменная a, остается переменной класса int

# t2 = (1, 2, 3, 5)
# print(t2[3]) # как и в списках можно работать с элементами по индексам
# for i in t2:
#     print(i) # тоже самое касается и циклов

# for j in range(len(t2)):
#     print(t2[j]) # в таком виде тоже работает

# t2[0] = 2
# в консоль выведется ошибка, потомучто данные в кортеже нельзя менять
# но если это был бы списко, то все бы работало






# d = {} # работа со словарями
# d = dict() # словарь можно обозначить как {} или задать параметр dict()
#
# d['q'] = 'qwerty' # q будет являться ключом, а ответом на
# # этот запрос будет строка qwerty
# d['w'] = 'windows' # w будет являться ключом, а ответом на
# # этот запрос будет строка windows
# print(d) # {'q': 'qwerty', 'w': 'windows'} - наш вывод
# # сначала идет ключ а затем ответ на этот ключ
# print(d['q']) # выводом будет qwerty

# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →
# # примеры работы сос словарями





# Множества
# Множества содержат в себе уникальные элементы, не обязательно
# упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два
# множества, Вы можете совершать над ними любые стандартные операции,
# например, объединение, пересечение и разность. Давайте разберем их.
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()



# Операции со множествами в Python
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}




# Неизменяемое или замороженное множество(frozenset) — множество, с которым
# не будут работать методы удаления и добавления.
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})




# 1. Создать список чисел от 1 до 100
# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]
# # Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]
# print(list_1)

# 2. Добавить условие (только чётные числа)
# list_1 = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         list_1.append(i)
# print(list_1)
# # Эту же функцию можно записать так:
# list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# print(list_1)

# Допустим, вы решили создать пары каждому из чисел (кортежи)
# list_1 = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         list_1.append((i, i))
# print(list_1)
# # Эту же функцию можно записать так:
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,
# # (100, 100)]
# print(list_1)

# Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.
# list_1 = []
# for i in range(10):
#     if i % 2 == 0:
#         list_1.append(i * 2)
# print(list_1)
# # Эту же функцию можно записать так:
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]




# Профилирование и отладка
# Мы с вами люди, а людям суждено ошибаться, даже при написании программного
# кода 🙂
# Давайте разберем с Вами самые частые ошибки в написании кода на Python.
# 🔥 Самые распространенные ошибки:


# # ● SyntaxError(Синтаксическая ошибка)
#
# number_first = 5
# number_second = 7
# if number_first > number_second: # !!!!!
#     print(number_first)
#
# # # Отсутствие :
#

# # ● IndentationError(Ошибка отступов)

# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # !!!!!
#
# # IndentationError:
# # expected an indented block after 'if' statement on line 270
# # Отсутствие отступов


# # ● TypeError(Типовая ошибка)
#
# text = 'Python'
# number = 5
# print(text + number)
#
# # TypeError: can only concatenate str (not "int") to str
# # Нельзя складывать строки и числа


# # ● ZeroDivisionError(Деление на 0)
#
# number_first = 5
# number_second = 0
# print(number_first // number_second)
#
# # ZeroDivisionError: integer division or modulo by zero
# # Делить на 0 нельзя


# # ● KeyError(Ошибка ключа)
#
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
#
# # line 299, in <module>
# #     print(dictionary[3])
# # KeyError: 3
# # Такого ключа не существует


# # ● NameError(Ошибка имени переменной)
#
# name = 'Ivan'
# print(names)
#
# # line 315, in <module>
# #     print(names)
# # NameError: name 'names' is not defined. Did you mean: 'name'?
# Переменной names не существует


# # ● ValueError(Ошибка значения)
#
# text = 'Python'
# print(int(text))
#
# # line 326, in <module>
# #     print(int(text))
# # ValueError: invalid literal for int() with base 10: 'Python'
# # Нельзя символы перевести в целые значения


# Итоги:
# 1. Мы изучили коллекции данных:
# ● списки
# ● кортежи
# ● словари
# ● множества
# 2. List Comprehension
# 3. Профилирование и отладка
