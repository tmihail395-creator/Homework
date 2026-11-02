# Ctrl + Alt + L (уберает лишнюю дестаницию, вспомогательный)
# while True:
#     num=int(input("Число: "))
#     for i in range(1, 11):
#         print(num*i)


import random

num_random = random.randint(1, 10)
tries = 0
game = 0
while True:
    choice = int(input("Вгадайте число 1 до 10: "))
    if choice < 0 or choice > 10:
        print("Вихід за межі!")
    elif choice == 0:
        print("Вихід!")
        break
    tries += 1
    if choice == num_random:
        game += 1
        print("Вітаю, ви виграли!")
        print(f"Використанні спроби: {tries}\n"
              f"Виграно ігр: {game}")
        spr = input("Бажаєте пограти ще? ")
        if spr == "No":
            break
        else:
            print("Лудомания")
            tries = 0
    elif choice < num_random:
        print("Більше!")
    else:
        print("Менше!")
