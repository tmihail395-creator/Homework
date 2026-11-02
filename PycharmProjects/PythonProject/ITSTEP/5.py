# try:
# except: офіційна назва помилки as перероблюємо помилку на змінну:
# finally: можем написать финал
#raise вызывает ошибку (указать ее)
try:
    money = int(input("How much do you wan`t to have: "))
    if money%10==0 and money<=1000:
        cod=input("Enter cod: ")
        if cod=="9365":
            print(f"Your {money}")
        else:
            print("The system calls 911!")
    else:
        raise Exception ("Not enough money")
except ValueError:
    print("Enter in a different format")
finally:
    print("The end.")

