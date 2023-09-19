# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# someString = 'a a a b c a a d c d d'

# someString2 = str.split(someString)

# diction = dict()

# for i in someString2:
#     if i in diction:
#         diction[i] +=1
#         print(f'{i}_{diction[i]}', end = ' ')
#     else:
#         diction[i] = 0
#         print(i, end = ' ')



# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text = 'She sells sea shells on the sea shore The shells that she sells are sea shells I\'m sure. So if she sells sea shells on the sea shore I\'m sure that the shells are sea shore shells'

# text = text.upper().replace('.', ' ')
# text = text.split()
# text = set(text)
# print(type(text))
# print(text)
# print(len(text))

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах


# max = -1

# while number > 0:
#     number = int(input())
#     if number > max:
#         max = number

# print(max)
# max = -1

# while True:
#     number = int(input())
#     if number > max:
#         max = number
#     if number == 0:
#         break

# print(max)

# # Ваня:
# # n = int(input()) !!!
# # max_number = 1000 !1 ошибка
# # while n != 0:
# #  n = int(input())
# #  if max_number > n: !2 ошибка
# #  max_number = n
# # print(max_number)

# # Петя:
# # n = int(input()) !!!
# # max_number = -1
# # while n < 0: !1 ошибка
# #  n = int(input())
# #  if max_number < n: 
# #  n = max_number !2 ошибка
# # print(n) !3 ошибка

# 20:46
# max = -1

# while n > 0:
#     number = int(input())
#     if number > max:
#         max = number

# print(max)

# Задача №112305. Удаление дубликатов
# Напишите программу, которая выполняет "сжатие массива" – заполняет все копии уже ранее встречавшихся элементов нулями 
# и переставляет все нулевые элементы в конец массива. При этом все оставшиеся элементы располагаются в начале массива 
# в том же порядке, что и в исходном массиве.

# Входные данные
# Первая строка содержит размер массива N . Во второй строке через пробел задаются N чисел – элементы массива. 
# Гарантируется, что 0 < N ≤ 10000 .

# Выходные данные
# Программа должна вывести в одну строчку все элементы получившегося массива, разделив их пробелами.

# Примеры
# входные данные
# 6
# 0 1 2 1 2 3
# выходные данные
# 1 2 3 0 0 0

# array = [0, 1, 2, 1, 2, 3]
# print(array)

# for i in range(len(array)):
#     for j in range(len(array)):
#         if array[i] != array[j]:
#             continue
#         elif i == j:
#             continue
#         else:
#             array[j] = 0

# print(array)

# for i in range(len(array)):
#     if array[i] == 0:
#         array.append(array[i])
#         array.pop(i)
#         for j in range(len(array)):
#             if array[j] == 0:
#                 array.append(array[j])
#                 array.pop(j)

# print(array)

# numbers = list(map(int, input().split(' ')))

# # for i in range(len(numbers)):
# #     numbers[i] = int(numbers[i])

# numbers_dup = list(set(numbers))

# if 0 in numbers_dup:
#     numbers_dup.remove(0)
#     # numbers_dup.append(0)


# for i in range(len(numbers) - len(numbers_dup)):
#     numbers_dup.append(0)

# print(*numbers_dup)

# Напишите программу, которая отделяет положительные элементы массива от отрицательных: 
# переставляет все положительные (в том же порядке) в начало массива, а все отрицательные 
# (в том же порядке) – в конец массива, все нулевые элементы должны оказаться в середине массива.

# Входные данные
# Первая строка содержит размер массива N . Во второй строке через пробел задаются N чисел – элементы массива. 
# Гарантируется, что 0 < N ≤ 10000 .

# Выходные данные
# Программа должна вывести в одну строчку все элементы получившегося массива, разделив их пробелами.

# Примеры
# входные данные
# 6
# 1 -1 2 -2 0 3
# выходные данные
# 1 2 3 0 -1 -2

import os  #очищаем
clear = lambda: os.system('cls')
clear()

numbers = list(map(int, input().split())) # вычищаем от лишних знаков строку, конвертируем в список

numbers_negative = [] # создаем пустой список

count = 0

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] < 0:
        numbers_negative.append(numbers.pop(i))
    if numbers[i] == 0:
        numbers.pop(i)
        count +=1
    
print(numbers)

numbers_negative.reverse()

numbers += ['0'*count] + numbers_negative

print(' '.join(list(map(str, numbers)))) # форматируем под запрошенный вывод, т.е. объединяем элементы списка пробелом, мэппим, переводим список в строку
