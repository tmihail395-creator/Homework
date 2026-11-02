# from abc import ABC, abstractmethod
# # Удален некорректный импорт async_generator, так как он не использовался
#
# class AbstractBasePlayer(ABC):
#     def __init__(self, name, rase): # Оставлено исходное имя аргумента rase
#         self.name = name
#         self.rasa = rase
#
#     @abstractmethod
#     def attack(self):
#         pass
#
#     def show_info(self):
#         print(f'Name: {self.name}\nRasa: {self.rasa}')
#
# class Human(AbstractBasePlayer):
#     def __init__(self, name, rasa, age):
#         super().__init__(name, rasa)
#         self.age = age
#
#     def attack(self):
#         print("Human attack with sword!")
#
#     def show_info(self):
#         # Удалены дублирующие строки print, так как super().show_info() уже выводит Name и Rasa
#         super().show_info()
#         print(f'Age: {self.age}')
#
# class Elf(AbstractBasePlayer):
#     def __init__(self, name, rasa):
#         super().__init__(name, rasa)
#
#     def attack(self):
#         print("Elf attack with bowl!")
#
# class Game:
#     def __init__(self):
#         self.players = []
#
#     def add_player(self, player):
#         # Исправлена логика проверки дубликатов:
#         # player.name сравнивался со списком объектов игроков. Теперь проверяются имена внутри списка.
#         if isinstance(player, AbstractBasePlayer) and player.name not in [p.name for p in self.players]:
#             self.players.append(player)
#
#     def show_players(self):
#         if self.players:
#             for player in self.players:
#                 player.show_info()
#
#     def battle(self):
#         if self.players:
#             for player in self.players:
#                 player.attack()
#
# # Исходная симуляция
# h1 = Human("Human", 1, 45)
# h2 = Human("HumaN", 2, 73)
# elf1 = Elf("Jhonn", 1)
# elf2 = Elf("Stacy", 2)
#
# game = Game()
# game.add_player(elf1)
# game.add_player(elf2)
# game.add_player(h1)
# game.add_player(h2)
# game.add_player(h1)
# game.add_player(h2)
# game.add_player(h1)
#
# # Вызов методов для проверки работы
# game.show_players()
# game.battle()

#
# from abc import ABC, abstractmethod
#
# class Transport(ABC):
#     def __init__(self, mark: str, speed: int):
#         self.mark = mark
#         self.speed = speed
#     def show_info(self):
#         print(f'Transport: {self.mark}\n Speed: {self.speed}')
#     @abstractmethod
#     def move(self):
#         pass
#
# class Car(Transport):
#     def move(self):
#         print(f"Auto: {self.mark}, run with speed: {self.speed}")
#
# class Bike(Transport):
#     def move(self):
#         print(f"Model bike: {self.mark}, run with speed: {self.speed}")
#
# class Plane(Transport):
#     def move(self):
#         print(f"Mark plane: {self.mark}, pline with speed: {self.speed}")
#
#
# transport=[
#     Car("McLaren", 190),
#     Bike("Kavasaki", 300),
#     Plane("Boeing", 1100)
# ]
#
# for techno in transport:
#     techno.show_info()
#     techno.move()
#
#



# class MyMetaClass(type):
#     def __new__(cls, name, bases, dict):
#         print("Hello from __new__()")
#         print(f'type of the class created: {cls}')
#         print(f"name: {name}")
#         print(f"bases: {bases}")
#         print(f"dict: {dict}")
#         return super().__new__(cls, name, bases, dict)
#
#
#
# class MyMetaClass1(type):
#     def __new__(cls, name, bases, dict):
#         if 'id' not in dict.keys():
#             print(f"No id attribute in class {name}")
#         else:
#             merhods= {key: value for key, value in dict.items() if callable(value)}
#             if len(merhods) >2:
#                 print(f"Error more then 2 method in class {name}")
#             else:
#                 print(f"Class {name} is creating")
#                 return super().__new__(cls, name, bases, dict)
#
#
# class MyClass(metaclass=MyMetaClass):
#     attr = 100
#
#     id=0
#
# class MyClass2(metaclass=MyMetaClass1):
#     name="fsdfds"
#     num=0
#     id=0
#     def method1(self):
#         pass
#     def method2(self):
#         pass
#     def method3(self):
#         pass
# obj = MyClass()


class RequiredMethodMeta(type):
    def __new__(mcs, name, bases, attrs):
        if 'show_info' not in attrs or not callable(attrs['show_info']):
            raise TypeError(f"Error: the class '{name}' must implement the show_info() method.")
        return super().__new__(mcs, name, bases, attrs)


class GoodClass(metaclass=RequiredMethodMeta):
    def show_info(self):
        print("All data is successfully displayed!")
print("Class GoodClass was created successfully.")

try:
    class BadClass(metaclass=RequiredMethodMeta):
        def custom_method(self):
            print("This class is missing the required method.")
except TypeError as err:
    print(f"\nAn error was caught:\n{err}")

