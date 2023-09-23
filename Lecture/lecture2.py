# def sumNumbers(n):
#     sumSum = 0
#     for i in range (1, n+1):
#         sumSum += i
#     print(sumSum)

# sumNumbers(12) функция для печати

# def sumNum(n):
#     sumSum = 0
#     for i in range(1, n + 1):
#         sumSum += i
#     return sumSum

# print(sumNum(15))

# сумма для неограниченного количества аргументов

# def sum_str(*args):
#     res = " "
#     for i in args:
#         res += i
#     return res


# print(sum_str('k', 'e', 'k'))

# модули. делаешь файл в той же папке, или закидываешь готовый туда.
# далее импортируешь его. потом берешь название файла, точка + название функции и аргументы. Вот так у тебя появилась своя библиотека
# import module as m1
# m1.function(1,2)
# или

# from module import *

# РЕКУРСИЯ

# пользователь вводит число n и программа выводит последовательность фиббоначи с соответствующим количеством значений. считаем от 0

# def fibo(n):
#     if n in [1, 2]: # basis of recurssion
#         return 1
#     return fibo(n-1) + fibo(n-2)

# list1 = []
# for i in range(1, 10):
#     list1.append(fibo(i))
# print(list1)

# Быстрая сортировка

# def quick_sort(array):
#     if len(array) <= 1: # если длина списка после очередной теации будет 1 или меньше - возвращается это значение и цикл прекращается
#         return array
#     else:
#         pivot = array[0]  # начальный элемент - всегда первый элемент массива
#     less = [i for i in array[1:] if i <= pivot] # создается массив с элементами менее либо равными пивоту
#     more = [i for i in array[1:] if i > pivot] # создается элемент массива с элементами строго более пивота
#     return quick_sort(less) + [pivot] + quick_sort(more) # сложение отсортированного списка, при этом вызов рекурсии для неотсортированных частей

# print(quick_sort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))

# Сортировка слиянием

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums)//2  # делим список надвое
#         # формируем левый список со значениями менее серидины
#         left = nums[:mid]
#         # формируем правый список со значением больше середины
#         right = nums[mid:]
#         merge_sort(left)  # рекрсия
#         merge_sort(right)
#         i = j = k = 0  # создаем переменные для цикла, i - левый, j - правый, k - общий ход
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i] # сравниваем два значения - добавляем в новый список 
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left): # циклы на остатки
#             nums[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list1 = [1, 5, 6, 9, 8, 7, 2, 1, 69, 2, 4]
# merge_sort(list1)
# print(list1)