# class Car:
#     def __init__(self):
#         self.__color = "red"
#
#     def color(self):
#         return self.__color
#
# ferrary = Car()
# print(ferrary.color())
#
#
#
# class Car:
#     color = "red"
#     def info(self):
#         print(self.color + "!")
#
# ferrary = Car()
# cadilac = Car()
# ferrary.info()
# cadilac.info()
# Car.color = "silver"
# ferrary.info()
# cadilac.info()
#
#
#
# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.login='qwerty'
#     def info(self):
#         print(self.name)
#
# pakOstin = Player('pak')
# print(type(pakOstin))

# class Animal:
#     def __init__(self, name, age, color):
#         self._name = name
#         self._age = age
#         self._color = color
#
#     def get_info(self):
#         print(self._name)
#         print(self._age)
#         print(self._color)
#
#     def golos(self):
#         print("animal golos")
#
#
# class Dog(Animal):
#     def __init__(self, name, age, color):
#         print("Start creating the Dog")
#         super().__init__(name, age, color)
#
#     def golos(self):
#         print("Wooow!..woooow!.....")
#
#
# class Cat(Animal):
#     def __init__(self, name, age, color):
#         print("Start creating the Cat")
#         super().__init__(name, age, color)
#         self.hp = 9
#
#     def get_info(self):
#         super().get_info()
#         print(self.hp)
#
#     def golos(self):
#         print("MEEEOOOOOW.....")
#
#
# class Cow(Animal):
#     def __init__(self, name, age, color, milk):
#         print("Start creating the Cow")
#         super().__init__(name, age, color)
#         self.milk = milk
#
#     def get_info(self):
#         super().get_info()
#         print(self.milk)
#
#     def golos(self):
#         print("moooooooooow.....")
#
#
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def get_info(self):
#         # Добавлены подчёркивания к переменным
#         return f"{self._name} is {self._age} years old"
#
#     def getHi(self, text):
#         # Добавлено подчёркивание к переменной
#         return f"{text}! I am {self._name}"
#
#
# nps1 = Person("John", 18)
# print(nps1.getHi("Hello"))
#
#
# class Student(Person):
#     spec = "computer science"
#
#     def __init__(self, name, age, score):
#         super().__init__(name, age)
#         self.score = score
#
#     def isSuccessfull(self, score):
#         return True if score >= 75 else False
#
#     def get_info(self):
#         return super().get_info() + f" Score is {self.score}"
#
#
# student1 = Student("Alex", 19, 80)
# print(student1.getHi("Hi"))
# print(student1.get_info())
# print(student1.isSuccessfull(90))
#
# st2 = Student("Bob", 20, 50)
# print(st2.getHi("Hello"))
# print(st2.get_info())
# print(st2.isSuccessfull(30))
#
#
# class Employee(Person):
#     def __init__(self, name, age, salary, jobTitle):
#         super().__init__(name, age)
#         self.salary = salary
#         self.jobTitle = jobTitle
#
#     def get_info(self):
#         return super().get_info() + f" salary is {self.salary}, jobTitle is {self.jobTitle}"

class Character:
    def __init__(self, name, health, damage):
        self._name = name
        self._health = health
        self._damage = damage

    def show_info(self):
        print(f"[{self.__class__.__name__}] {self._name} | HP: {self._health} | DMG: {self._damage}")

    def attack(self, target):
        print(f"{self._name} attacks {target._name}!")
        target.take_damage(self._damage)

    def take_damage(self, amount):
        self._health = max(0, self._health - amount)
        print(f"{self._name} gets {amount} damage. Current HP: {self._health}")


class Warrior(Character):
    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage)
        self.armor = armor

    def show_info(self):
        super().show_info()
        print(f"-> Armor status: {self.armor}")

    def attack(self, target):
        total_dmg = self._damage + 5
        print(f"{self._name} hits {target._name} with a heavy sword!")
        target.take_damage(total_dmg)

    def take_damage(self, amount):
        blocked = min(amount, self.armor)
        actual_dmg = max(0, amount - blocked)
        print(f"{self._name} blocks {blocked} damage with armor.")
        super().take_damage(actual_dmg)


class Mage(Character):
    def __init__(self, name, health, damage, mana):
        super().__init__(name, health, damage)
        self.mana = mana

    def show_info(self):
        super().show_info()
        print(f"-> Mana level: {self.mana}")

    def attack(self, target):
        if self.mana >= 20:
            self.mana -= 20
            spell_dmg = self._damage * 2
            print(f"{self._name} casts a powerful fireball spell at {target._name}!")
            target.take_damage(spell_dmg)
        else:
            print(f"{self._name} has no mana left! Hits with a basic staff strike.")
            super().attack(target)


class Archer(Character):
    def __init__(self, name, health, damage, arrows):
        super().__init__(name, health, damage)
        self.arrows = arrows

    def show_info(self):
        super().show_info()
        print(f"-> Arrows left: {self.arrows}")

    def attack(self, target):
        if self.arrows > 0:
            self.arrows -= 1
            print(f"{self._name} shoots a fast arrow at {target._name}! (Arrows remaining: {self.arrows})")
            target.take_damage(self._damage)
        else:
            print(f"{self._name} has no arrows! Attacks in close combat with less damage.")
            target.take_damage(self._damage // 2)







