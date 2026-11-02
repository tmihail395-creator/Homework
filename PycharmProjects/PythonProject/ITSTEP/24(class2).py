# import random
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         # protected prop
#         self._age = age
#         # private prop
#         self.__person_id = random.randint(1, 100)
#
#     def get_info(self):
#         self.__show_id()
#         return f"{self.name} is {self._age} years old"
#
#     def getHi(self, text):
#         return f"{text}! I am {self.name}"
#
#     def _get_name(self):
#         return self.name
#
#     def __show_id(self):
#         print(self.__person_id)
#
# papich=Person("Papich", 20)
# print(papich.get_info())
import os


class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
    def call(self, number):
        print(f"Дзвінок на {number}")
    def show_phone_info(self):
        print(f"Номер: {self.phone_number}")

class Camera:
    def __init__(self, megapixels):
        self.megapixels = megapixels
    def take_photo(self):
        print("Фото зроблено")
    def show_camera_info(self):
        print(f"Камера: {self.megapixels}MP")

class Smartphone(Phone, Camera):
    def __init__(self, brand, model, phone_number, megapixels):
        Phone.__init__(self, phone_number)
        Camera.__init__(self, megapixels)
        self.brand = brand
        self.model = model
    def show_info(self):
        print(f"{self.brand} {self.model} | Номер: {self.phone_number} | Камера: {self.megapixels}MP")
    def __str__(self):
        return f"[Сутність Смартфон] {self.brand} {self.model} ({self.phone_number})"

phone1 = Smartphone("Apple", "15 Pro", "+380501111111", 48)
phone2 = Smartphone("Samsung", "S24", "+380632222222", 50)
print(phone1)
print(phone2)
print("-" * 30)
phone1.show_info()
phone1.call("+380679999999")
phone2.take_photo()



