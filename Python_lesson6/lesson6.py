# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# arr1 = []
# n = int(input("input length of arr 1: "))
# for i in range(n):
#     arr1.append(int(input("input number for arr1:")))
# p = int(input("input length of arr 2: "))
# arr2 = []
# for i in range(p):
#     arr2.append(int(input("input number for arr2:")))
# arr3 = []
# for el in arr1:
#     if el not in arr2:
#         arr3.append(el)
# print(*arr3)


# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# arr1 = []
# n = int(input("input length of arr 1: "))
# for i in range(n):
#     arr1.append(int(input("input number for arr1:")))
# count = 0
# for i in range(1, len(arr1)-1):
#     if arr1(i-1) < arr1(i) and arr1(i+1) < arr1(i):
#         count +=1

# print(count)

# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# count = 0
# arr = [1, 2, 3, 2, 3]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] == arr[j]:
#             count +=1
# print(count)


# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10**5
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# k = int(input("input a numbre: "))
# lst1 = []
# for i in range(1, k + 1):
#     sum1 = 0
#     for j in range(1, i//2 + 1):
#         if i % j == 0:
#             sum1 += j
#     lst1.append([i, sum1])

# for i in range(len(lst1)):
#     for j in range(i + 1, len(lst1)):
#         if lst1[i][0] == lst1[j][1] and lst1[i][1] == lst1[j][0]:
#             print(lst1[i])

# Дан многомерный список произвольного уровня вложенности:

# [
# 	'a': [
# 		'b': [
# 			'c': '+++'
# 		]
# 	],
# ]
# Сделайте функцию, которая будет возвращать элементы объекта, параметром получая строку с ключами объекта, разделенными точками:

# func('a.b.c'); // вернет '+++'

def find_plus(dct: dict, stroka):
    if type(stroka) == str:
        lst = stroka.split(".")
    elif type(stroka) == list:
        lst = stroka
    find_key = lst[0]
    if len(lst) == 1:
        return dct[find_key]
    for key in dct:
        if key == find_key:
            return find_plus(dct[key], lst[1:])


complex_dict = {
    'user_info': {
        'name': 'Alice',
        'age': 30,
        'contacts': {
            'email': 'alice@example.com',
            'phone': {
                'home': '123-456-7890',
                'work': '987-654-3210'
            }
        }
    },
    'products': {
        'electronics': {
            'laptop': {
                'brand': 'Dell',
                'price': 1200
            },
            'smartphone': {
                'brand': 'Apple',
                'price': 800
            }
        },
        'clothing': {
            'shirts': {
                'brand': 'Nike',
                'price': 40
            },
            'jeans': {
                'brand': 'Levi\'s',
                'price': 50
            }
        }
    }
}

keys_str = 'user_info.contacts.phone'
print(find_plus(complex_dict,keys_str))