#while - цикл з умовою
#break - стоп сигнал

# num=1000
# while num>=-1:
#     print(f"{num}")
#     num-=7



# n1 = 1
# while n1 < 11:
#     if not n1 % 2:
#         print(n1)
#     n1 += 1



# num=int(input("Введіть з клавіатури перше число"))
# num1=int(input("Введіть з клавіатури друге число"))
# while num<=num1:
#     if num%2==0:
#         print(num)
#     num+=1



# while True:
#     try:
#         print(" -- Menu -- ")
#         print(" 1 Balance")
#         print(" 2 Exit")
#         choice = int(input("Press btn - "))
#         if choice == 1:
#             print("Balance 1000")
#         elif choice == 2:
#             print("End work")
#             break
#     except ValueError:
#         print("Write numbers only")



# try:
#     num1=int(input("Введите превое число"))
#     num2=int(input("Введите второе число"))
#     choice=int(input("1 - спадаючий, 2 - зростаючий"))
#     if choice==1:
#         while num2>=num1:
#             print(num2)
#             num2-=1
#     if choice==2:
#         while num2>=num1:
#             print(num1)
#             num1+=1
# except ValueError:
#     print("Ввод числами")


# try:
#     num1=int(input("Первое число"))
#     num2=int(input("Второе число"))
#     if num1> num2:
#         while num1>num2:
#             if num1%2==1:
#                 print(num1)
#             num1-=1
#     if num2>num1:
#         while num2>num1:
#             if num2%2==1:
#                 print(num2)
#             num2-=1
# except ValueError:
#     print("Введеня числами")



num1=int(input("Перше число"))
num2=int(input("Друге число"))
while num1<=num2:
    if num1%2==0:
        print(num1)
    num1+=1
    if num1%2==1:
        print(num1)