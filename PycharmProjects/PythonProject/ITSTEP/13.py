# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)
#
##[вираз for elem in послідовність]
#
# squares=[x**2 for x in range(1,11)]
# print(squares)
#
# list1=[I*3 for I in "GngBng"]
# print(list1)
#
# e_n=[x for x in range(21) if x%2==0]
# print(e_n)
#
#
# prices=[100, 200, 300, 400, 500]
# n_prices=[prices*0.9 for prices in prices]
# print(n_prices)
#
#
# matrix=[[0 for j in range(2)]for i in range(3)]
# print(matrix)
#
#
# import random
# rand_nums=[random.randint(0,1) for i in range(3)]
# print(rand_nums)

# user_str='2 2 2'
# list_nums=[int(x) for x in user_str.split()]
# print(list_nums)
#
# list_nums.extend([1, 2, 3])
# print(list_nums)
#
# list_nums.copy()
#
# new_list = list_nums.copy()
# print(list_nums)
# new_list.sort(reverse=True, key=int)
# print(new_list)
#
#
# word=['agfc','bc','a']
# word.sort(key=len)
# print(word)
#
#
#
# del new_list[0]
# print(new_list)
#
#
# grades=[
#     [10, 12, 11],
#     [9, 10, 12],
#     [11, 8, 10]
# ]
# grades[1][0]=22
# for row in grades:
#     for col in row:
#         print(col, end=" | ")
#     print()
#


#MATRIX
# import random
# while True:
#     numbers = random.randint(0, 1)
#     matrix=[[numbers for j in range(4)]for i in range(4)]
#     for row in matrix:
#         for col in row:
#             print(col, end="   ")
#         print()



numbers =[1, 2, 3, 4, 5]
matrix=[[i * j for j in numbers] for i in numbers]
for row in matrix:
    for col in row:
        print(col, end="   ")
    print()


import random
original_list = [random.randint(-20, 20) for _ in range(15)]

list1 = [num for num in original_list if num % 2 == 0]
list2 = [num for num in original_list if num % 2 != 0]
list3 = [num for num in original_list if num < 0]
list4 = [num for num in original_list if num > 0]

print(f"Початковий список: {original_list}\n")
print(f"лист1 (парні):     {list1}")
print(f"лист2 (непарні):   {list2}")
print(f"лист3 (від'ємні):  {list3}")
print(f"лист4 (додатні):   {list4}")








