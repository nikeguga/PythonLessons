# возведение в степень

# def f(a,b):
#     global c
#     if (b<=1):
#         return (1,a)[b]
#     p=a
#     z=a
#     k=1
#     while True:
#         k2=k+k
#         if k2<b:
#             p=p*z
#             c+=1
#             z=p
#             k=k2
#         else:
#             return p*f(a,b-k)
 
# c=0
# a = 3
# b = 5
# print(f(a,b))

# сумма через рекурсию

# def sum(a, b):
#     global c
    
#     if a == 0:
#         return c
#     if a > 0:
#         if b > 0:
#             c+=1
#             b-=1
#             return sum(a, b)
#         c+=1
#         a-=1
#         return sum(a, b)

# c = 0
# a = 12
# b = 10
# print(sum(a, b))