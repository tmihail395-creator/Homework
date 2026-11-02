#декораторы
from itertools import count
from os import times


# def hello():
#     print("Hello World")
#
#
# #1 decorator
# def decorator(func):
#     def wrapper():
#         print("Start")
#         func()
#         print("End")
#     return wrapper#без скобок, не как вызов функции
# newHello= decorator(hello)
# newHello()
# #короче вызываем функцию в функции, тем самым декорирую ее
#
#
# @decorator
# def hello2():
#     print("Hello World")
# hello2()
#
#
#
#
# def decorator_V2(func):
#     def wrapper(*args, **kwargs):
#         print("Start")
#         func(*args, **kwargs)
#         print("End")
#     return wrapper
#
# @decorator_V2
# def add(a, b, c):
#     print(a+ b+ c)
# add(2, 2, 4)
#
#
#
# def decorator_V3(func):
#     def wrapper(*args, **kwargs):
#         print("Start")
#         result=func(*args, **kwargs)
#         print("End")
#         return result
#     return wrapper
#
# @decorator_V3
# def mul(a, b, c):
#     return a * b * c
# res=mul(2, 2, 4)
# print(res)
#
#
#
# import time
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start=time.time()
#         result=func(*args, **kwargs)
#         end=time.time()
#         print(end-start)
#         return result
#     return wrapper
#
# @timer
# def sleep():
#     time.sleep(1)
# sleep()
#
#
# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f'Calling:{func.__name__}')
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper
#
# @timer
# @logger
# def sleep():
#     time.sleep(1)
# sleep()
#
# def counter(func):
#     count = 0
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(count)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @counter
# def show():
#     print("testing")
# for i in range(5):
#     show()
#
#
# #decorator with args
# def repeat(func):
#     def decorator(*args, **kwargs):
#         def wrapper(*args, **kwargs):
#             for i in range(timer):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat(3)
# def hello3():
#     print("Hi Git.... hub.... Hi Github!")
# hello()


# 1
def login_required(func):
    def wrapper(*args, **kwargs):
        if logd:
            return func(*args, **kwargs)
        else:
            print("Доступ заблокован!")
        return func(*args, **kwargs)
    return wrapper
logd=False

@login_required
def open_profile():
    print("Профіль відкрито")

open_profile()


#2
def only_numbers(func):
    def wrapper(*args):
        for arg in args:
            if type(arg) != int:
                print("Це не числа!!!")
                return
        return func(*args)
    return wrapper

@only_numbers
def add(a, b):
    print(a + b)
add(7, 43)
add(5, "10")


#3
def limit_calls(max_calls):
    def decorator(func):
        count = 0
        def wrapper(*args, **kwargs):
            nonlocal count
            if count < max_calls:
                count += 1
                return func(*args, **kwargs)
            else:
                print("Ліміт викликів вичерпано!!")
        return wrapper
    return decorator

@limit_calls(3)
def hello():
    print("Hi")
hello()
hello()
hello()
hello()

















