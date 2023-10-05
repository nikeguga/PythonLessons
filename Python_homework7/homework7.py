# каждая фраза разделена пробелом,каждое слово разделено дефисом. Утверждение верно если в каждой фразе одинаковое количество слогов. 

# vowels = ['а' ,'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka.split(" ") # сделали список по пробелам
# for i in range(len(phrases)):
#     phrases[i] = list(filter(lambda x: x if x in vowels else False, phrases[i])) # убрали всё кроме гласных
# # if phrases.count(phrases[0]) == len(phrases): # смоторим, сколько встречается элемент в списке, можно сделать аналогичное сравнение по длине списка
# #     print("Парам пам-пам")
# # else:
# #     print("Пам парам")
# length = [len(phrases[i]) for i in range (len(phrases))]
# if length.count(length[0]) == len(length) and len(phrases) > 1:
#     print("Парам пам-пам")
# elif len(phrases) <= 1:
#     print("Количество фраз должно быть больше одной!")
# else:
#     print("Пам парам")

# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         print(' '.join([str(i) for i in range(1, num_columns + 1)]))
#     for i in range(2, num_rows + 1):
#         print(i, end = ' ')
#         for j in range(2, num_columns + 1):
#             print(operation(i, j), end = ' ')
#         print()
        

# print_operation_table(lambda x, y: x * y)