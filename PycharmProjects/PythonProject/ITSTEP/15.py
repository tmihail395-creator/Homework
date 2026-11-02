#обов'зкові
# def add(a, b):
#     return a + b
#
# res = add(2,3)
# print(res)
from importlib.resources import read_text

#за замовченням
# def greet(name='guest'):
#     print("Hello, " + name)
#
# greet(name="John")
#
# def power(number, degree=2):
#     return number**degree
#
# print(power(2))
# print(power(2, 3))
#
# print(power(number=3, degree=4))


#список аргументов, набор данных
# def total(*args):
#     print(args)
#     return sum(args)
#
# total(1, 2 , 3)
#
# nums = [1, 2, 3]
# total(*nums)


# def numbers(start, end):
#     if start > end:
#         start, end = end, start
#     result=1
#     for i in range(start, end+1):
#         result*=i
#     return result
# print(numbers(1,4))
# print(numbers(2,5))
# print(numbers(3,6))


# def find(numbers):
#     maximum = numbers[0]
#     for num in numbers:
#         if num > maximum:
#             maximum = num
#     return maximum
# nums = [5, 12, 3, 8, 20, 7]
# print(find(nums))


# def sum_list(numbers):
#     return sum(numbers)
# print(sum_list([1, 2, 3, 4, 5]))

# global_num=100
#namespace global


from random import randint
import random



# def test():
#     #namespace local
#     global global_num
#     #делает фнкцию глобально (за пределами функции)
#     x=10
#     print(x)
#     global_num=500
#     print(f"Global num: {global_num}")
#
# test()
# print(f"glob num: {global_num}")
#
#
# def outer():
#     value=0
#     def inner():
#         nonlocal value
#         print("Inner func working")
#         value=1
#         print(value)
#     inner()
#     print(value)
# outer()
#
#
#
#
#
# def countDown(n):
#     if n==0:
#         return
#     print(n)
#     countDown(n-1)
#
# countDown(5)
#
#
# def factorial(num):
#     if num==0:
#         return
#     return num*factorial(num-1)




def func(n):
    if n == 1:
        return 1
    return n + func(n - 1)
print(func(10))


def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)
print(power(2, 5))



























