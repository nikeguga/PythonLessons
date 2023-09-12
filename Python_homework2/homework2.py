# task 1

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# ammount = abs(int(input("input ammount of coins:")))
# heads = 0
# tails = 0
# throws = 0

# while throws < ammount:
#     result = int(input("input \"0\" for heads \"1\" for tails: "))
#     if result == 1:
#         tails +=1
#     else:
#         heads +=1
#     throws +=1

# if heads > tails:
#     print(f"heads won, turn damn tails, there are only {tails} of them")
# elif tails > heads:
#     print(f"damn tails won it, turn the hell out of heads, they can't do nothing, there are only {heads} of them")
# else:
#     print("oh turn whatever you want, dude, you bore me")

# task 2

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# import math

# sum = int(input("input sum of those mysterious numbers: "))
# product = int(input("input your product of multiplication: "))

# disc = sum**2 - 4*product # y = sum - x, prod = x * (sum - x) -x**2 + sumX - prod = 0 , so we have -1 * negative product and "-" in formula
# firstX = (-sum + math.sqrt(disc))/-2
# secondX = (-sum - math.sqrt(disc))/-2
# if firstX > 0: #as we now that numbers were natural
#     x = int(firstX)
# elif secondX > 0:
#     x = int(secondX)
# y = int(sum - x)
# print(f"the numbers are: {x} and {y}")

# task 3

# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# num = int(input("input your number: "))
# powersOfTwo = [1] # we create a list as we need all powers, not the last one, and we input 2**0 from the get go
# i = 1
# power = 0
# while power*2 <= num:
#     power = 2 ** i
#     powersOfTwo.append(power)
#     i+=1
# print(f"all powers of 2 in inputed range are: {powersOfTwo}")