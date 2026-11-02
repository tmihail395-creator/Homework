# dict1={'dod': "1242488",
#        'son': '654722',}
# print(dict1)
# print(type(dict1))
# print(dict1['dod'])
# print(dict1['son'])
#
# student={"name": 'bober',
#         'age': 15,
#         'countre': "Poland"}
# print(f'Student name: {student["name"]}')
# #изменения с проверкой
# if 'age' in student:
#     student['age']=16
# print(student)
#
# #новые елементы
# student['city']='Wroclaw'
# print(student)



# student={"name": 'bober',
#         'age': 15,
#         'countre': "Poland"}
# student['Petty']='Sanya'
# student['Money']='Much'
# student['Skoko']='mnogo:', 3546345
# print(len(student))
#
#
# print(dict(zip([13, 2, 'gfsdfs'],[4, 2, 'sad'])))
#
# student.pop('Petty')
# print(student)
#
# print(student.keys())
#
# for key, value in student.items():
#     print(key, value)
#
# print(student.get('Petty'))

#case 1
# users=[
#     {'name':"Sasha", 'age':20,'login': '32FDhe234jifjw8'},
#     {'name':"Jonny", 'age':30,'login': '86yG78fdsf'},
#     {'name':"Sasha", 'age':50,'login': 'weds234Sddfs'},
# ]
# founding1=input("Який тип бажаєте знайти?\n")
# founding2=input("Що бажаєте знайти?\n")
# if founding1=="age":
#     founding2=int(founding2)
# elemFound=False
# for elem in users:
#     if elem.get(founding1)==founding2:
#         print(f"Element is found!")
#         for key, value in elem.items():
#             print(key, ":", value)
#         elemFound=True
#         break
# if not elemFound:
#     print(f"Element is not found!")

#case 2
# filmDict={
#     'originalTitle': 'Puthon',
#     'creator': 'Gvido',
#     'rate': 9,
#     'description':'Film about Python',
#     'year': [1991, 1992]
# }
#
# for key,value in filmDict.items():
#     print(f"{key}: {value}")
# sortedFilm=sorted(filmDict.items(), key=lambda x: x[0])
# # print(sortedFilm)
# for element in sortedFilm:
#     print(element)
#
#
# keyList=list(filmDict.keys())
# print(keyList)
#
# sortedKeys=sorted(keyList)
# print(sortedKeys)
#
#
# for key in sortedKeys:
#     print(key, filmDict[key])



# countyAndCapital = {
#     "Ukraine" : "Kyiv",
#     "Danmark" : "Kopenhagen",
# }
# def show_menu():
#     print("="*25)
#     print()
#
# def addCountry(nameCountry, capitalCity):
#     if nameCountry not in countyAndCapital:
#         countyAndCapital[nameCountry] = capitalCity
# def removeCountry(nameCountry):
#     if nameCountry not in countyAndCapital:
#         del countyAndCapital[nameCountry]
#         print(f"Країну {nameCountry} видалено.")
#     else:
#         print(f"Країни {nameCountry} немає в словнику.")
# def findCapital(nameCountry):
#     if nameCountry in countyAndCapital:
#         return countyAndCapital[nameCountry]
#     else:
#         return "Країну не знайдено"
# def updateCapital(nameCountry, newCapitalCity):
#     if nameCountry in countyAndCapital:
#         countyAndCapital[nameCountry] = newCapitalCity
#         print(f"Столицю для {nameCountry} змінено на {newCapitalCity}.")
#     else:
#         print(f"Країни {nameCountry} немає в словнику. Спочатку додайте її через addCountry.")


countyAndCapital = {
    "Ukraine": "Kyiv",
    "Danmark": "Kopenhagen",
}


def show_menu():
    print("\n" + "=" * 30)
    print("      МЕНЮ КЕРУВАННЯ")
    print("=" * 30)
    print("1. Показати всі країни та столиці")
    print("2. Додати країну")
    print("3. Видалити країну")
    print("4. Пошук столиці")
    print("5. Змінити столицю")
    print("0. Вихід")
    print("=" * 30)


def printAll():
    print("\nПоточний словник:")
    for country, capital in countyAndCapital.items():
        print(f"  {country} -> {capital}")


def addCountry(nameCountry, capitalCity):
    if nameCountry not in countyAndCapital:
        countyAndCapital[nameCountry] = capitalCity
        print(f"Успішно: Країну {nameCountry} додано.")
    else:
        print(f"Помилка: Країна {nameCountry} вже є у словнику.")


def removeCountry(nameCountry):
    # ВИПРАВЛЕНО: міняємо 'not in' на 'in'
    if nameCountry in countyAndCapital:
        del countyAndCapital[nameCountry]
        print(f"Успішно: Країну {nameCountry} видалено.")
    else:
        print(f"Помилка: Країни {nameCountry} немає в словнику.")


def findCapital(nameCountry):
    if nameCountry in countyAndCapital:
        return countyAndCapital[nameCountry]
    else:
        return "Країну не знайдено"


def updateCapital(nameCountry, newCapitalCity):
    if nameCountry in countyAndCapital:
        countyAndCapital[nameCountry] = newCapitalCity
        print(f"Успішно: Столицю для {nameCountry} змінено на {newCapitalCity}.")
    else:
        print(f"Помилка: Країни {nameCountry} немає в словнику.")


# --- Головний цикл програми ---
while True:
    show_menu()
    choice = input("Оберіть дію (0-5): ").strip()

    if choice == "1":
        printAll()

    elif choice == "2":
        country = input("Введіть назву країни: ").strip()
        capital = input("Введіть столицю: ").strip()
        addCountry(country, capital)

    elif choice == "3":
        country = input("Введіть назву країни для видалення: ").strip()
        removeCountry(country)

    elif choice == "4":
        country = input("Яку країну шукаємо? ").strip()
        result = findCapital(country)
        print(f"Результат: {result}")

    elif choice == "5":
        country = input("Введіть назву країни: ").strip()
        new_capital = input("Введіть нову столицю: ").strip()
        updateCapital(country, new_capital)

    elif choice == "0":
        print("Програму завершено. Бувай!")
        break

    else:
        print("Некоректне введення. Спробуйте ще раз.")








































