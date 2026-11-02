#len помогает определить кол-во символов




# try:
#     cod=int(input("Введите код: "))
#     if cod==1111:
#         print("Золото")
#     else:
#         print("911 call")
# except ValueError:
#     print("Ввод цифрами")



# try:
#     price=150
#     age=int(input("How old are you?"))
#     quantity=int(input("How many people are you in?"))
#     total_price=0
#     if age<=0 or quantity<=0:
#         print("Age and quantity need to be positive")
#     else:
#         total_price=price*quantity
#         if age<=12:
#             total_price=total_price-total_price*0.5
#             print(f"Price of your tickets: {total_price}")
#         elif age>=60:
#             total_price = total_price - total_price * 0.3
#             print(f"Price of your tickets: {total_price}")
#         else:
#             print(f"Price of your tickets: {total_price}")
# except ValueError:
#     print("Please enter a number")



# try:
#     dollar=44,21
#     uah=int(input("UAH: "))
#     if uah<0:
#         print("Need to be positive")
#     else:
#         print(f"UAH in USD = {dollar*uah}")
# except ValueError:
#     print("Please enter a number")


# try:
#     login=input("You login: ")
#     if login=="":
#         print("Логин не должен быть пустым или иметь пробелы!")
#     if login==" ":
#         print("Логин не должен быть пустым или иметь пробелы!")
#     password=input("You password: ")
#     if len(password)<=4:
#         print("Пароль должен иметь больше символов!")
#     age=int(input("You age: "))
#     if age<=13:
#         print("Возвращайся позже")
#     else:
#         print(f"Добро пожаловать, ваши данные: {login, age, password}")
# except ValueError:
#     print("Введите число возраста в цифрах")\

coffe=100
cruasan=200
cake=400
print("~~~Menu~~~")
print(f"Кофе: {coffe}           (1)")
print(f"Круасан: {cruasan}          (2)")
print(f"Тортик: {cake}          (3)")





