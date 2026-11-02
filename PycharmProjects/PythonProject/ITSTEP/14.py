#                       ФУНКЦИИ
#def welcome()
#   print("Hello World!")
#
#
#
#abs-меняет знак на позитивный (математика)
#round-округляет число (математика)
#len-считает числа (математика)
#sum-считает сумму чисел (математика)
#
#
#hours, minutes = divmod(130, 60)
#print(f"Hours: {hours}, minutes: {minutes}")
#
#
# import random
# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print(numbers)
#
#
#
#
#термин (интроспекция) - изучение чего то самостоятельно
#
#
#
#
# def bio():
#     name=input("ПІБ: ")
#     word=name.split()
#     print(list(word))
# bio()


# def add(num1, num2):
#     return num1+num2
# result=add(2, 2)*2
# print(result)
#
# def menu(chooce):
#     if chooce == 1:
#         return "Your choice 1"
#     elif chooce == 2:
#         return "Your choice 2"
# print(menu(2))

# num1=int(input("Введіть перше число: "))
# num2=int(input("Введіть друге число: "))
# def diapazone(num1, num2):
#     for i in range (num1, num2+1):
#         if i % 2 == 0:
#             print(i)
# diapazone(num1, num2)



# def show_line(high, symbol, nap):
#     if nap == "x":
#         print(high*symbol)
#     elif nap == "y":
#         for i in range(high):
#             print(symbol)
#     else:
#         print("Error input!")
# high = int(input("Введіть довжину лінії: "))
# nap = input("x - горизонталь\n"
#                 "y - вертикаль\n")
# symbol = input("Введіть символ: ")
# show_line(high, symbol, nap)




def number(nums):
    print(max(nums))
nums = list(input("Enter numbers: "))
number(nums)









