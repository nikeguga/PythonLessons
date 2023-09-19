# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# firstLength = abs(int(input("click damn digits. FIRST LENGTH: ")))

# listOne = []

# for i in range(firstLength):
#     listOne.append(int(input('input a number, you sad creature: ')))

# print(f"let me show the result you've acheved so far: {listOne}")

# secondLength = abs(int(input("you got lucky once, try it again, dumdum. SECOND LENGTH6: ")))

# listTwo = []

# for i in range(secondLength):
#     listTwo.append(int(input('so passion, much skill, ten digits are mastered: ')))

# print(f'oh, you hoped we are done? Not yet: {listTwo}')
# print('Are you happy?')

# listOne = set(listOne)
# listTwo = set(listTwo)
# listOne = listOne.union(listTwo)
# listOne = list(listOne)

# i = 0

# while i < len(listOne) - 1:
#     min = i
#     j = i + 1
#     while j < len(listOne):
#         if listOne[j] < listOne[min]:
#             min = j
#         j += 1
#     listOne[i], listOne[min] = listOne[min], listOne[i]
#     i += 1

# print(f'Vzhuh and some sorting has done this to your hard typing skills: {listOne}')

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# amountOfBushes = abs(int(input('HOW MANY BUSHES DO YOU HAVE? BUSHES!!! GIVE ME NUMBER: ')))

# bushes = {}

# for i in range(amountOfBushes):
#     bushes[i] = abs(int(input('Berries. How many? How many goddamn berries on this goddamn bush?: ')))

# berriesCount = []

# for i in range(amountOfBushes):
#     berriesCount.append(bushes[i])

# for i in range(amountOfBushes-1):
#     if i == 0:
#         sum = berriesCount[i] + berriesCount[i+1] + berriesCount[-1]
#         max = sum
#         count = 0
#     elif i == amountOfBushes:
#         sum = berriesCount[i-1] + berriesCount[i] + berriesCount[0]
#         if sum > max:
#             max = sum
#             bush = i
#     elif 0 < i < amountOfBushes:
#         sum = berriesCount[i-1] + berriesCount[i] + berriesCount[i+1]
#         if sum > max:
#             max = sum
#             bush = i

# print(f'you greedy piece of bush, your best bet to get as many berries as you can carry in one go is this bush: numbre {i}: {bushes[i]}')