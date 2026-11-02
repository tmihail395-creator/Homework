# line=int(input("Введіть довжину лінії"))
# symbol=input("Символ для заполнения линии")
# for i in range(line):
#     print(symbol,end=" ")
from itertools import count

# num=input("Enter a number: ")
# count=0
# for i in num:
#    count+=1
# print(count)


while True:
    try:
        choice=input("~~~Menu~~~\n"
                     "Оберіть:\n"
                     "(+)-додавання\n"
                     "(-)-віднімання\n"
                     "(/)-ділення\n"
                     "(Leave)-вихід\n")
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))
        if choice=="+":
            print(n1+n2)
        elif choice=="-":
            print(n1-n2)
        elif choice=="/":
            print(n1/n2)
        elif choice=="Leave":
            print("Bye")
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid format of text")

