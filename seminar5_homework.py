# Задача 26:  Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

a = int(input("Please enter the number A: "))
b = int(input("Please enter the number B: "))
def Degree(a, b):
    if b > 1:
        b -= 1
        return a * Degree(a, b)
    return a
print(f'{a}^{b} = {Degree(a, b)}')


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4
# a = int(input("Please enter the number A: "))
# b = int(input("Please enter the number B: "))
# def SumNumbers(a, b):
#     if 0 == b:
#         return a
#     return SumNumbers(a + 1, b - 1)
# print(f'{a} + {b} = {SumNumbers(a, b)}')