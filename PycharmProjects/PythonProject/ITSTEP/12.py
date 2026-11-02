#list - набір даних, може переформутувати дані до списку

# append - только добавляет в список
# insert - заменяет в списке значение на значение
# extend - добавляет список к списку через переменную
# sort - сортирует (странно работает, не знаю че)
# reverse - меняет местами
# pop - удаляет последний елемент (если не добавить значение)
# remove - удаляет елемент (по значению)
# clear - удаляет все
# count - считает количество елементов (по значению)
# len - считает длину списка




#LIBRARY
# book1=1
# book2=10
# book3=11
# book4=100
# book5=110
#
# shelfs=[book1,book2,book3,book4,book5]
# for shelf in shelfs:
#     print(shelf, end=" | ")

numbers = []
plus = 0
while True:
    num1 = int(input("Enter number: "))
    if num1 == 0:
        break
    numbers.append(num1)
    if num1 > 0:
        plus += num1
print(plus)

