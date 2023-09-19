# LISTS

# empty lists creation

# list_1 = []
# list_1 = list()

# initialise list with elements:

# list_2 = [1, 2, 3, 4, 5] # you just put the elements inside the brackets, in print we will see brackets. 
#If not needed - we need to use * in print
# print(*list_2) #here, no brackets

# print(len(list_2)) # len is applicable to all types of data

# calling out the elements of list is easy: 

# print(list_2[0])

# ammending list

# list_1 = [1, 5]
# print(list_1)
# list_1.append(2) #adding element as the new last one
# print(list_1)
# list_1.pop()
# print(list_1) #removing last element
# # we can use pop to delete desired element via adding index of the element in brackets:

# list_2 = [1, 2, 3, 8283, 49, 69]
# print(list_2)
# list_2.pop(3)
# print(list_2)

# # we can insert element on desired position via "insert" function. we put() first argument goes for index, second for the element

# list_2.insert(3, 881324712)
# print(list_2)

# # lists also can be sliced

# print(list_2[1:3])

# #we can also input steps in the slice, so we can choose several pieces

# print(list_2[::2]) #all list with step of 2

# TUPLES

#tuple - unchanging list. faster, safer if no changes are intended, less memory used
#we can initialise tuples as empty:

# t = ()

# # or we can initialise them with element:

# t = (1, ) # we do need to put comma in here

# # we can make tuple out of the list:

# listToBeTupled = [1, 2, 3, 4, 69]
# print(listToBeTupled)
# tupledList = tuple(listToBeTupled)
# print(tupledList) #we can delete brackets in the output via adding * before the argument
# print(type(tupledList))
# #we can also separate tuple for veriables via multiple assignment:
# a, b, c, d, e = tupledList
# print(a, b, c, d, e)

# DICTIONARIES

# dic_k = {} #created empty dictionary
# dic_k2 = dict() #another way to create empty dictionary
# dic_k2["q"] = "qwerty" # we made dictionary with element "qwerty" and the key "q"
# print(dic_k2)
# dic_k2["w"] = "suck" #we added new key and element
# print(dic_k2)
# print(dic_k2["w"]) #this how we print an element of the dictionary
# we have keys values and items
# #dictrionaries support all types of data, including lists and tuples, and you can put all element types within one dictionary
# del dic_k2["q"] #this how we delete elements of dictionary
# print(dic_k2)
# print(dic_k2.items())

# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# # print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# QUANTITIES

# colors = {"red", "green", "blue"} # here is quantity
# print(colors)
# colors.add("spinach") # how we add element into a quantity
# # here's the thing, if we are trying to add an element which is already in quantity - nothing will change, cause it holds only value
# print(colors)
# colors.remove("red") #removing element, obvious, isn't it?
# print(colors)
# # cool way to remove:
# colors.discard("blue") #it removes argument, if it is within the quantity, and if not - slips, while "remove" will give you a mistake
# print(colors)
# # we can delete every element with colors.clear() - it will return an empty quantity
# we can set an empty quantity:
# q = set() #here we go

# we can also do math with quantities:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5} # crossing, elements in both quantities
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}
# we can freeze a quantity
# a = {1, 8, 6}
# b = frozenset(a) # same data within, but unchangable

# LIST COMPREHENSION

# it is a feature of python. We use "for" cycle within this and it also may contain conditions via if-else

# list_1 = [exp for item in iterable]
# list_1 = [exp for item in iterable (if conditional)]

# so we need a fucka list withnumbers from 1 to 100. we can go as below:

# list_1 = []
# for i in range(1, 101):
#     list_1.append(i)
# print(list_1)

# or we can do this crazy muthafacka

# list_1 = [i for i in range(1, 101)] 

# # if we need evens:

# list_1 = [i for i in range(1, 101) if i % 2 == 0]

# # if we decided to make tuples:

# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] 

# # and even some math action

# list_1 = [i * 2 for i in range(10) if i % 2 == 0]


