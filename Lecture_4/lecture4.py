# arr = [1, 2, 3, 5, 8, 15, 23, 38]

# # for i in range(len(arr)):
# #     if arr[i]% 2 == 0:
# #         print(f"{arr[i]} and square {arr[i]*arr[i]}" )


# или

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]

# res = select(int, arr)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1)) # map — функция высшего порядка, используемая во многих языках программирования,
#  которая применяет какую-либо функцию к каждому элементу списка своих аргументов, выдавая список результатов как возвращаемое значение
# print(list_1)

# data = '15 156 96 3 5 8 52 5'

# data = list(map(int, data.split())) # тут мы конвертим строку в список, затем список строк в список интов
# print(data)

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data)) # фильтруем список по заданному параметру, в нашем случае по лямбде (всё что кончается на 5)
# print(res)

#zip

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)

# если параметров недостаточно - зип бежит по минимальному сету

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data)

# Функция enumerate
# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
# кортежами из индекса и элементов входных данных.
# Функция enumerate() позволяет пронумеровать набор данных.

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users)
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]