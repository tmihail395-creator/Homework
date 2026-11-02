# import math
# from linecache import clearcache
#
# numbers=[1, 4 ,3 ,6]
#
# for num in numbers:
#     print(num)
#
# for i in range(len(numbers)):
#     numbers[i]+=10
#     print(numbers[i])
#
#
# #tuple кортеж
# PI=math.pi
# print(PI)
# NUMBER_PI="qwerty"
#
# #creating tuple
# years=(2000, 2001, 2002, 2003, 2004)#кортеж
# for year in years:
#     print(year)
# print(type(years))
# #TypeError: 'tuple' object does not support item assignment
# #years[0]=1999
#
# empty=()
# print(type(empty))
#
# numbers=tuple(numbers)
# print(type(numbers))
#
# #Доступ до елементів
# colors=("red", "green", "blue")
# print(colors[1])
# print(colors[0])
# print(colors.count("анатолий"))
# if "blue" in colors:
#     print(colors.index("blue"))
#
# def shownums(*nums):
#     print(nums)
# shownums(1,2,3,4,5)
# print(type(shownums))
#
# person=('Anton', 15)
# name, age=person
# print(name)
# print(age)
#
# a=1
# b=2
# a,b=b,a
# print(a, b)
#
#
# students = (
#     ('Anton', 15),
#     ('vanya', 40)
# )
# print(students[0][0])
#
#
#
# #1
# # fruits=(
# #     ('apple', 'banana', 'apple'),
# #     ('pear', 'orange'),
# #     ('grape'))
# # choice=int(input("Number: "))
# # print(len(fruits[choice]))
#
# emails=["ivanov.alex99@gmail.com",
#         "marketing@companyname.ua",
#         "info.promos2026@ukr.net",
#         "marketing@companyname.ua"]
# unique=set(sorted(emails))
# print(unique)
#
# numbers={1, 2, 3, 4, 5, 6}
# print(numbers)
#
# nums=[2, 2, 3, 3, 4, 4]
# print(set(nums))
#
# s=set()#set быстрее остальных
# print(type(s))
#
# a={}
# print(type(a))
#
# # Methods
# numbers.add("гей")
# print(numbers)
#
# iphoneSet1={'iphone11', 'iphone12', 'iphone13'}
# iphoneSet2={'iphone13', 'iphone12', 'iphone15', 'iphone16'}
#
# #deference
# print(iphoneSet1.difference(iphoneSet2))
# #порівняння колекцій
# print(iphoneSet2.difference(iphoneSet1))
# print(iphoneSet1-iphoneSet2)
# print(iphoneSet2-iphoneSet1)
# print(iphoneSet1.intersection(iphoneSet2))
# print(iphoneSet2.intersection(iphoneSet1))
# print(iphoneSet2 & iphoneSet1)
#
# #union
# print(iphoneSet1.union(iphoneSet2))
# print(iphoneSet1 | iphoneSet2)
#
#
# #frozenset()
# frozenA = frozenset(iphoneSet1)
# print(frozenA)

# countre={'Россия', 'США', 'Китай', 'Франция', 'Япония', 'Италия', 'Канада', 'Испания', 'ТурцияЕгипет'}
# choice=int(input("1 - додавати країни\n"
#                  "2 - видаляти країни\n"
#                  "3 - пошуку країн за введеними символами\n"
#                  "4 - перевіряти, чи міститься країна в множині.\n"))
# if choice==1:
#     adding=input("Назва країни: ")
#     print(countre)
# elif choice==2:
#     removing = input("Назва країни: ")
#     if removing in countre:
#         print(countre.remove(removing))
# elif choice==3:
#     founding=input("Пошук країни: ")
#     if founding in countre:
#         print(founding)
#     else:
#         print("Такої країни немає")
# elif choice==4:
#     founding_countre = input("Пошук країни: ")
#     if founding_countre in countre:
#         print(True)
# else:
#     print("Немає такого вибору")




iphoneSet1={'Днепр', 'Київ', 'Одеса'}
iphoneSet2={'Харьків', 'Днепр', 'Одеса', 'Херсон'}
print(iphoneSet1.union(iphoneSet2))






