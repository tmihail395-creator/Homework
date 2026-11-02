#high=int(input("Введіть висоту: "))
# line=int(input("Введіть ширину: "))
# for i in range(high):
#     print("*"*line)



# type=int(input("~~~Оберіть фігуру~~~\n"
#            "(1) - квадрат\n"
#            "(2) - прмяокутник\n"
#             ""))
# symbol=input("Оберіть символ: ")
# if type == 1:
#     kv=int(input("Доавжина квадрату: "))
#     for i in range(kv):
#         print(symbol*kv)
# elif type == 2:
#     high=int(input("Введіть висоту: "))
#     line=int(input("Введіть ширину: "))
#     for i in range(high):
#         print(symbol*line)
# else:
#     print("Некоректне введення")




# high=int(input("Введіть висоту: "))
# line=int(input("Введіть ширину: "))
# for i in range(high):
#     if i==0 or i==high-1:
#         print("*"*line)
#     else:
#         print("*"+" "*(line-2)+"*")



# import random
# win=0
# rounds=0
# bot=0
# nich=0
# while True:
#     game=input("Оберіть дію:\n"
#                "к - Камень\n"
#                "н - Ножниці\n"
#                "п - Папір\n"
#                "в - Вихід\n"
#                "")
#     if game=="в":
#         break
#     if game not in 'кнп':
#         print("Невелика помилка(")
#         continue
#     computer=random.choice('кнп')
#     print(f"Бот обирає: {computer}")
#     if game==computer:
#         print("Ничья")
#         nich+=1
#     elif game=="к" and computer=="н" or game=="н" and computer=="п" or game=="п" and computer=="к":
#         win+=1
#         rounds+=1
#         print(f"WIN!!!\n "
#               f"Win score: {win}\n "
#               f"Rounds: {rounds}")
#     elif game=="к" and computer=="п" or game=="н" and computer=="к" or game=="п" and computer=="н":
#         bot+=1
#         rounds+=1
#         print("Lose(\n"
#               f"Win score: {win}\n"
#               f"Rounds: {rounds}: ")
#     if rounds==3:
#         print("Кінець гри")
#         if win==2:
#             print("Ви безумновний переможець")
#             break
#         elif bot==2:
#             print("Нажаль вас перемогли(")
#     elif nich==1 and win==1 and bot==1 or nich%3==0:
#         print("Додаткові раунди")



# try:
#     import random
#     while True:
#         menu=int(input("~Вітаємо вас у грі 'Втеча з підземелля'!\n"
#                        "\t\tВи лицар, що потрапив у підземелля, \n"
#                        "\t\t\t\tпройдіть 10 кімнат, щоб втекти!~\n"
#                        "Гарної гри)\n"
#                        "~~~Menu~~~\n"
#                    "(1) - Грати\n"
#                    "(2) - Вихід\n"))
#         if menu == 2:
#             print("Ще побачимось, бувай!")
#             break
#         elif menu == 1:
#             hp = 100
#             balance = 0
#             room = 0
#             while True:
#
#                 monster = random.randint(10, 30)
#                 money = random.randint(10, 100)
#                 hill = random.randint(-20, 20)
#                 choice = random.choice([monster, money, hill])
#                 if choice == monster:
#                     doing1=int(input("На вас напав монстр, ваші дії?\n (1) - захищатись\n (2) - бігти\n"))
#                     if doing1 == 2:
#                         hp-=monster
#                         print("Ви втелки, але монстер вас вдарив")
#                     elif doing1 == 1:
#                         balance+=money
#                         print(f"Ви вбили монстра та отримали нагороду {money} монети!")
#                     room+=1
#                     print(f"Кімнат пройдено: {room}")
#
#                 if choice == hill:
#                     doing2=int(input("Ви знайшли зілля, бажаєте випити його?\n"
#                                      "(1) - Так\n"
#                                      "(2) - Ні\n"))
#                     if doing2 ==1:
#                         hp += hill
#                         if hill>1:
#                             print("Зілля було корисним!")
#                         elif hill<1:
#                             print("Ви отруїлись")
#                     elif doing2 == 2:
#                         continue
#                     room+=1
#                     print(f"Кімнат пройдено: {room}")
#                 if choice == money:
#                     balance+=money
#                     print("Вітаю, ви знайшли гроші!")
#                     room+=1
#                     print(f"Кімнат пройдено: {room}")
#
#                 if hp<=0:
#                     print("Ви померли")
#                     resh=int(input("Хочете зіграти ще?\n"
#                                "(1) - Так\n"
#                                "(2) - Ні"))
#                     if resh==1:
#                         continue
#                     elif resh==2:
#                         break
#                 elif room==10:
#                     print("Ви пройшли гру!)\n"
#                           "Ваші досягнення:\n"
#                           f"{balance} монет\n"
#                           f"{hp} здоров'я\n")
#                     break
#             break
# except ValueError:
#     print("Такого вибору не існує")
