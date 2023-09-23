# def foo(x,y,*args,**kwargs):
#     print(x,y) переменные
#     print(args) кортеж (неименованные, те, что не заданы как переменные в функции)
#     print(kwargs) словарь (поименованные с присвоением, которые не входят в первые два)
    
# foo(1,3,5,6,7,a=4,b=3,d=16)

# рекурсия

# def recr(num,degree,res):
#     if degree == 0:
#         return res
#     a = int(input())
#     b = recr(num, degree-1, res*num)
#     print(a)
#     return b

# degree = int(input())
# print(recr(2, degree, 1))

# ищем строку в списках

# def recr(a):
#     for el in a:
#         if isinstance(el,list):
#             return recr(el)
#         if isinstance(el,str):
#             return el

# a = [1,2,[2,3,[4,5,["qe",12]]]]
# print(recr(a))

# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# def fibo(n):
#     if n in [1, 2]: # basis of recurssion
#         return 1
#     return fibo(n-1) + fibo(n-2)

# k = abs(int(input('input number: ')))
# list1 = []
# for i in range(1, k+1):
#     list1.append(fibo(i))
# print(list1)

# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# grade = abs(int(input('input amount of grades: ')))

# grades = []
# max = 0
# min = 10
# for i in range(grade):
#     temp = int(input("grade: "))
#     grades.append(temp)
#     if temp > max:
#         max = temp
#     if min > temp:
#         min = temp

# print(f'{min}  +  {max}')

# for i in range(len(grades)):
#     if grades[i] == max:
#         grades[i] = min
                

# print(grades)

# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# def prime_number(num):
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# number = int(input('Input number: '))

# if prime_number(number):
#     print(f'{number} is prime number')
# else:
#     print(f"{number} isn't prime number")

# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# def recurs(num):
#     if num == 0:
#         return ''
#     number_1 = input('Input number: ')
#     return recurs(num-1) + ' ' + number_1

# print(recurs(3))