# def anti(x):
#     return x*x
#
# result=anti(2)
# print(result)
#
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# result=[]
#
# for n in numbers:
#     result.append(n**2)
#
# print(result)
#
#
# ressult=list(map(lambda x: x**2, numbers))
# print(ressult)
#
#
# def apply_operator(a, b, operation):
#         return operation(a,b)
#
# def add(x, y):
#     return x+y
#
# def multiply(x, y):
#     return x*y
#
# def divide(x, y):
#     return x/y
#
# print(apply_operator(2, 3, multiply))
# print(apply_operator(1, 3, add))
# print(apply_operator(2, 4, divide))
#
#
#
# def nameUpper(name):
#     return 'user'+name.upper()
#
# def nameLower(name):
#     return 'user'+name.lower()
#
# def makeLog(userName, maker):
#     return maker(userName)
#
# print(nameUpper('user'))
# print(nameLower('user'))
#
#
# #lambda
# square=lambda x: x**2
# print(square(3))
#
# add=lambda x,y:x+y
# print(add(3,4))
#
# is_even=lambda x:x%2==0
# print(is_even(3))
# print(is_even(4))
#
# maximum=lambda x,y:x if x>y else y
# print(maximum(3,2))
# print(maximum(3,7))
#
#
#
#
# students=[["Max", 87],["Vlad", 134],["Toha", 70]]
#
# print(students)
# sortedSts=sorted(students, key=lambda x: x[1])
# print(sortedSts)
#
#
#
# studentsYear=[]
# studentsBirthYear=[2000, 1997, 2003, 1996, 2010]
# for year in studentsBirthYear:
#     studentsYear.append(2026-year)
# print(studentsYear)
#
# studAges=list(map(lambda year: 2026-year, studentsBirthYear))
# print(studAges)
#
#
# userLogs1 = ['Admin', 'STUDENT', 'QEWgskd', 'User']
# print(userLogs1)
# userLogsLower=list(map(str.lower, userLogs1))
# print(userLogsLower)
#
# def modifPizzaTypes(pizzaTypes):
#     return pizzaTypes+"Pizza"
# pizzaTypes=['Meat', '4Cheese', 'Margorita']
# print(pizzaTypes)
# pizzaNames=list(map(modifPizzaTypes, pizzaTypes))
# print(pizzaNames)
#
# #filter
# prices=[100, 8, 56, 34, 120, 230]
# expensive=list(filter(lambda x: x>=100, prices))
# print(expensive)
#
#
# #zip
# userLogs=['1234efdf', 'f12rfgrwdw', '214t2sad']
# userPass=['413', '54312', '42340']
#
# for log,passw in zip(userLogs, userPass):
#     print(f"Login: {log}, pass: {passw}")
# print(type(zip(userLogs, userPass)))

#3
# user_input = input("Введіть цілі числа через пробіл: ")
# int_list = [int(x) for x in user_input.split()]
# string_list = [str(num) for num in int_list]
# print("Список рядків:", string_list)



#4
# prices = [120, 250, 99, 560, 310]
# expensive=list(filter(lambda x: x>=200, prices))
# discounted = [x * 0.9 for x in expensive]
# print(discounted)



students = ["Анна", "Олег", "Марія", "Іван"]
scores = [95, 67, 88, 73]
for std,scr in zip(students, scores):
    if scr>=80:
        print(f'Студент: {std}, Бал: {scr}')







