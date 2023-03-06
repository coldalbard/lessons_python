# import modul1 as m1


# n = int(input())
# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
# a = sum_numbers(n)
# print(a)


# def sum_stry(*args):
#     res = ""
#     for i in args:
#         res += 1
#     return res
# print(sum_stry("q", "w", "e", "r"))
# print(m1.max1(15, 9))


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# list1 = []
# for i in range(1, 10):
#     list1.append(fib(i))
# print(list1)


# def qick_sort(array):
#     if len(array) <= 1:
#         return  array
#     else:
#         pivot = array[0]
#     les = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return qick_sort(les) + [pivot] + qick_sort(greater)
# print(qick_sort([14, 5, 9, 28, 1, 68, 5]))


# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
# list1 = [1, 9, 8, 7, 0, 6, 5, 2]
# merge_sort(list1)
# print(list1)

