# students = ['Anna', 'Bill', 'Max']
#
# print(students)
#
# # name = input("Enter name - ")
# # students.append(name)
# print(students)
#
# file_name = 'students.txt'
# # file = open(file_name, 'w', encoding='utf-8')
# # for st in students:
# #     file.write(st + '\n')
# # file.close()
#
# student = {
#     'name': "Max",
#     'age': 15,
#     'grade': 11
# }
#
# # file = open(file_name, 'w', encoding='utf-8')
# # for key, value in student.items():
# #     file.write(f"{key} : {value}\n")
# #
# # file.close()
#
# file = open('students.txt', 'r', encoding='utf-8')
# # data = file.read(5)
# # data2 = file.read(10)
# # print(data2)
# data = file.readline()
# allLines = file.readlines()
# print(data)
# print(allLines)
# file.close()
#
# # режими роботи з файлом  w, r, a, b, x
#
# file = open(file_name, 'a', encoding="utf-8")
# file.seek(0, 0)
# print(file.tell())
# file.write('Ben\n')
# file.close()

# #1
# file = open("output.txt", "w", encoding="utf-8")
# file.write("Hello, world!")
# file.close()
#
# #2
# file = open("output.txt", "r", encoding="utf-8")
# content = file.read()
# print(content)
# file.close()
#
# #3
# source = open("data.txt", "r", encoding="utf-8")
# content = source.read()
# source.close()
# destination = open("backup.txt", "w", encoding="utf-8")
# destination.write(content)
# destination.close()
#
# #4
# file = open("data.txt", "r", encoding="utf-8")
# lines = file.readlines()
# print(len(lines))
# file.close()
dotka="data.txt"
file = open(dotka, "w", encoding="utf-8")
content = file.read()

lines_count = len(content.splitlines())
words_count = len(content.split())
chars_count = len(content)

summary_file = open("summary.txt", "w", encoding="utf-8")
summary_file.write(f"Рядків: {lines_count}\n")
summary_file.write(f"Слів: {words_count}\n")
summary_file.write(f"Символів: {chars_count}\n")
summary_file.close()
