# import pickle, json
# from os import write
#
# people={
#     'name':"Max",
#     'age':18,
#     'grade': [10, 11, 10]
# }
#
# #виконали серіалізацію зі збереженням у файл
# with open('people.pkl', 'wb') as file:
#     pickle.dump(people, file)
#
# with open('people.pkl', 'rb') as file:
#     people = pickle.load(file)
# print(people)
#
# with open('people.json', 'w') as file:
#     json.dump(people, file, indent=10)
#
#
# with open('people.json', 'r') as file:
#     st=json.load(file)
# print(st)
#
#
#
# list_numbers=list(map(int, input("Введіть список цілих: ").split(" ")))
# with open('list_numbers.pkl', 'wb') as file:
#     pickle.dump(list_numbers, file)
#
#
#
# import csv
# with open('student.csv', 'w', newline="", encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Age", "Phone"])
#     writer.writerows(['Max', '34', '213452424'])
#     writer.writerows(['Ben', '12', '212345242'])
#
# with open('student.csv', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     print(reader)
#     for row in reader:
#         print(row)
#
#
# with open('student.csv') as file:
#     reader = csv.DictReader(file)
#     for st in reader:
#         print(st)
#
# with open('student.csv', 'w') as file:
#     field_names=['Name', 'salary']
#     writer = csv.DictWriter(file, fieldnames=field_names)
#     writer.writerow({'name': "Max", 'salary': 10000})


import csv

count =-1
with open('worker.csv', 'w', encoding='utf-8', newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Department","Salary"])
    writer.writerow(["Іван",'IT', 35000])
    writer.writerow(["Анна",'HR', 27000])
    writer.writerow(["Максим","IT", 42000])
    writer.writerow(["Олена", "Sales", 31000])
    writer.writerow(["Петро", "IT", 39000])
    writer.writerow(["Марія", "Marketing", 29500])

with open('worker.csv', encoding='utf-8', newline="") as file:
    reader = csv.reader(file)
    print(reader)
    for row in reader:
        print(row)
        count+=1
print(f"Кількість працівників: {count}")

