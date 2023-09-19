# Task 1: Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.

# #list_1 = [1, 2, 3, 4, 5]
# #k = 3

# # Введите ваше решение ниже
# count = 0
# for i in range (len(list_1)):
#     if list_1[i] == k:
#         count +=1
# print(count)

# Task 2: Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# list_1 = [1, 4, 3, 7, 8, 9, 2]
# k = 10
# closest = max(list_1)
# min = max(list_1)
# for i in range (len(list_1)):
#     if k - list_1[i] > 0 and k - list_1[i] < min:
    
#         closest = list_1[i]
#         min = k - list_1[i]

#     elif list_1[i] - k > 0 and list_1[i] - k < min:
#         closest = list_1[i]
#         min = list_1[i] - k
#     elif list_1[i] - k == 0:
#         closest = list_1[i]
#         min = list_1[i] - k
# print(closest)

# Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# english = {'1': ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 
#            '2': ['D', 'G'], 
#            '3': ['B', 'C', 'M', 'P'], 
#            '4': ['F', 'H', 'V', 'W', 'Y'], 
#            '5': ["K"], 
#            '8': ['J', 'X'], 
#            '10': ['Q', 'Z'] }
# russian = {'1': ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
#            '2': ['Д', 'К', 'Л', 'М', 'П', 'У'],
#            '3': ['Б', 'Г', 'Ё', 'Ь', 'Я'],
#            '4': ['Й', 'Ы'],
#            '5': ['Ж', 'З', 'Х', 'Ц', 'Ч'],
#            '8': ['Ш', 'Э', 'Ю'],
#            '10': ['Ф', 'Щ', 'Ъ']}
# k = 'ноутбук'
# k = str.upper(k)
# b = []
# count = 0
# for i in range (len(k)):
#     b.append(k[i:i+1])
# for i in range (len(b)):
#     if b[i] in english['1'] or b[i] in russian['1']:
#         count +=1
#     elif b[i] in english['2'] or b[i] in russian['2']:
#         count +=2
#     elif b[i] in english['3'] or b[i] in russian['3']:
#         count +=3
#     elif b[i] in english['4'] or b[i] in russian['4']:
#         count +=4
#     elif b[i] in english['5'] or b[i] in russian['5']:
#         count +=5
#     elif b[i] in english['8'] or b[i] in russian['8']:
#         count +=8
#     elif b[i] in english['10'] or b[i] in russian['10']:
#         count +=10

# print(count)