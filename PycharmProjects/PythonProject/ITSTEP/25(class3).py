# class Book:
#     def __init__(self, title, director, pages):
#         self.title = title
#         self.director = director
#         self.pages = pages
#
#     def showInfo(self):
#         print(self.title)
#         print(self.director)
#         print(self.pages)
#
#     def __str__(self) -> str:
#         return f"{self.title} {self.director}, {self.pages}"
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
#     def __eq__(self, other):
#         if isinstance(other, Book):
#             return self.title == other.title and self.director == other.director
#         else:
#             return False
#
#
# b1 = Book("Книга 1", "Режиссер 1", 500)
# b2 = Book("Книга 2", "Режиссер 2", 300)
#
# b1.showInfo()
# print(b1)
# print(b1 > b2)
# print(b1 == b2)
#
# from typing import Self
#
# print("positive")
# print(123)
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person1 = Person("Max", 18)
# print(person1)
#
# print(2 + 2)
# print("2" + "2")
#
#
# # print("2" + 2)
#
#
# class Film:
#     def __init__(self, title, director, age):
#         self.title = title
#         self.director = director
#         self.age = age
#
#     def showInfo(self):
#         print(self.title)
#         print(self.director)
#         print(self.age)
#
#     def __str__(self):
#         return f"{self.title} {self.director} {self.age}"
#
#
# class Book:
#     def __init__(self, title, director, pages):
#         self.title = title
#         self.director = director
#         self.pages = pages
#
#     def showInfo(self):
#         print(self.title)
#         print(self.director)
#         print(self.pages)
#
#     def __str__(self) -> str:
#         return f"{self.title} {self.director}, {self.pages}"
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
#     def __eq__(self, other):
#         if isinstance(other, Book):
#             return self.title == other.title and self.director == other.director
#         else:
#             return False
#
#
# film1 = Film("Python", "Max", 18)
# book1 = Book("qwerty", "Bill", 150)
# book2 = Book("qwerty", "Bill2", 50)
# for item in (film1, book1):
#     # item.showInfo()
#     print(item)
#
# print(book1 == book2)
#
#
# class Class1:
#     def __new__(cls):
#         print("Hi i am __new__ magic method!")
#         return super(Class1, cls).__new__(cls)
#
#     def __init__(self):
#         print("Hi i am __init__ magic method!")
#
#
# obj1 = Class1()
# print(book1 > book2)
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self) -> str:
#         return f"({self.x} : {self.y})"
#
#     def __mul__(self, other):
#         if isinstance(other, Point):
#             return Point(self.x * other.x, self.y * other.y)
#         elif isinstance(other, int):
#             return Point(self.x * other, self.y * other)
#         else:
#             raise TypeError("error multiplication")
#
#     def __iadd__(self, other):
#         if isinstance(other, int):
#             self.x += other
#             self.y += other
#             return self
#         elif isinstance(other, Point):
#             self.x += other.x
#             self.y += other.y
#             return self
#         else:
#             raise TypeError("error addition")
#
#
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# print(p1)
# print(p2)
# print(p1 * p2)
# print(p1 * 2)
# # print(p1 * 3.5)
#
# a = 1
# a += 10
# print(a)
# print(p1)
# p1 += p2
# print(f"{p1}")
#
# print(2 + "4")


class Library:
    def __init__(self, name: str = "No Name", address: str = "No Address", book_count: int = 0):
        self.name = name
        self.address = address
        self.book_count = max(0, book_count)
    def __add__(self, value: int):
        return Library(self.name, self.address, self.book_count + value)
    def __sub__(self, value: int):
        return Library(self.name, self.address, max(0, self.book_count - value))
    def __iadd__(self, value: int):
        self.book_count += value
        return self
    def __isub__(self, value: int):
        self.book_count = max(0, self.book_count - value)
        return self
    def __lt__(self, other): return self.book_count < other.book_count
    def __gt__(self, other): return self.book_count > other.book_count
    def __le__(self, other): return self.book_count <= other.book_count
    def __ge__(self, other): return self.book_count >= other.book_count
    def __eq__(self, other): return self.book_count == other.book_count
    def __ne__(self, other): return self.book_count != other.book_count
    def __str__(self):
        return f"Библиотека: '{self.name}' | Книг: {self.book_count}"

lib1 = Library("Центральная", "ул. Главная, 1", 5000)
lib2 = Library("Научная", "пр. Науки, 10", 7000)
lib1 += 500
print(lib1)
print(lib1 < lib2)






