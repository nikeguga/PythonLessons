# list comprehension

# lst = [[i, j] for i in range(5) for j in range(5, 10)] # здесь получаем списки, где для каждого i цикл j и дет полный круг
# print(lst)

# lst = [i for i in range (10) if i % 2 == 0] # сюда же через if можно прописать условие добавления в список
# print(lst)

# lst = [i if i % 2 == 0 else 69 for i in range (10)] # если есть else - цикл проверок ставим влево от рэйнджа
# print(lst)

# also there is dict comprehension:

# dct = {k:9 for k in range (36)} # also we can define 9 as veriable 
# a = [[1, 2], [3, 4], [5, 6]]
# dct = {k:v for k, v in a} # if we choose to do this via list we need to be sure to have as many veriables as values in each sublists
# print(dct)

# enumerate

# a = "keka69"
# print(list(enumerate(a))) # counting elements from 0, returns tuple
# # unpacking tuple:
# lst = []
# for index, value in enumerate(a):
#     lst.append([index, value])   # unpacking tuple to sublists as example

# print(lst) 

# zip

# a = "keka69"
# b = [5, 6, 3, 9, 41]
# c = {0: "z", 1: "a", 2: "l"}
# print(list(zip(a, b, c))) # connecting elements in chronological order until somewhere there is no unconnected elements left,returns tuple
# # there is ziplong that works until the last element, returns null for absent elements

# for a, b, c, in zip(a, b, c): # we can walk through several sequences
#     if b % 2 == 0 and a != "k":
#         print("poopy")

# lambda anonymus function

# def sum(a, b):
#     return a+b
# print(sum(4, 5))

# sum = lambda a, b: a+b
# print(sum(7, 8))

# so it is a compact replacement of methods

# map

# a = [4, 3, 2, 1, 5]

# print(map(str, a)) # map принимает 2 значения, функцию и последовательность. Функция принимать может только один аргумент
# # Мэп берет каждый элемент из последоватлеьности и применяет к ним функцию. Возвращает объект класса map. str - встроенная функция

# но можно рукописные:

# def jope (k):
#     return f"{k}" + " jopa"
# a = [4, 3, 2, 1, 5]
# # print(list(map(jope, a)))
# # часто вместо функции внутри map записывается в виде lambda

# print(list(map(lambda x: f"{x} jopa" if x < 5 else "jopa is here", a)))

# map не может не вернуть что-то, т.е. удалить элемент полностью нельзя, можно вернуть null, например

# filter

# a = [4, 3, 2, 1, 5]
# print(list(filter(lambda x: f"{x} jopa" if x < 5 else False, a))) # при фильтре значение False исчезает, если нет - элемент остается, но не изменяется

# a = [i for i in range (20)]
# print(a)
# print()

# print(list(filter(lambda x: not x%2, a))) # выводим только чётные 

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] #Список, которому нужна копия
# transformed_values = list(map(lambda x: x, values)) # копия через лямбду в map
# print(transformed_values)

# поиск самой большой орбиты. Даны большой и малый радиусы планет, нужно найти наибольшую площадь арбиты по формуле пи * малый * большой. 
# круглые орбиты игнорируем
# import math
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# s = list(map(lambda x: math.pi*x[0]*x[1] if x[0] != x[1] else 0, orbits))
# # print(s)
# max_s = max(s)
# # print(max_s)

# print(*orbits[s.index(max_s)]) # * для снятия скобок при выводе

# def find_farthest_orbit(f):
#     return max(f, key=lambda x: x[0] * x[1] if x[0] != x[1] else -1) # max возвращает элемент, который дает большее значение 
# по заданному параметру, а не больший результат по параметру, т.е. вывод будет как надо


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# проверка исходного списка со списком после применения условия из лямбда
# def same_by(f, v):
#     lst = list(filter(f, v))
#     return lst == v

# values = [0, 2, 10, 6]

# if same_by(lambda x: True if x % 2 == 0 else False, values):
#     print('same')
# else:
#     print('different')

