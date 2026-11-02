#1
# from datetime import datetime
# class ServerRequest:
#     def __init__(self):
#         self.requests = []
#         self.stats_queue=[]
#     def add_request(self, user, priority, message):
#         priority = int(priority)
#         data=(priority,user, message)
#         self.requests.append(data)
#         self.requests.sort()
#         print(f"↓ From user: {user}, priority: {priority} ↓\nMessage: {message}")
#     def process_request(self):
#         if self.is_empty():
#             print("You don't have any requests")
#             return None
#         priority, user, message =self.requests.pop(0)
#         current_time = datetime.now().strftime("%H:%M:%S")
#         self.stats_queue.append((user, current_time))
#         print(f"The server processed the request from {user}")
#     def is_empty(self):
#         return len(self.requests) == 0
#     def size(self):
#         return len(self.requests)
#     def show_requests(self):
#         if self.is_empty():
#             print("You don't have any requests")
#         else:
#             for req in self.requests:
#                 print(f"From user: {req[1]}, priority: {req[0]}, message: {req[2]}")
#     def show_stats_queue(self):
#         if self.is_empty():
#             print("No stats available yet")
#         else:
#             for user, time in self.stats_queue:
#                 print(f"From user: {user}, time: {time}")
#
# server = ServerRequest()
# server.add_request("John", 2, "Hello chatGPT please check my homework for errors ")
# server.add_request("Pork", 1, "Frr... ugh... nh... furr...")
# server.show_requests()
# server.process_request()
# server.show_stats_queue()



#2
# from datetime import datetime
# import random
# class Pier:
#     def __init__(self):
#         self.peoples = []
#         self.boats = []
#         self.time = []
#         self.max_queue = 0
#     def add_passenger(self, time_str):
#         dt = datetime.strptime(time_str, "%H:%M")
#         self.peoples.append(dt)
#     def add_boat(self, time_str, stop_type="regular"):
#         dt = datetime.strptime(time_str, "%H:%M")
#         if stop_type == "terminal":
#             free_seats = random.randint(40, 60)
#         else:
#             free_seats = random.randint(0, 15)
#         self.boats.append((dt, stop_type, free_seats))
#     def process_simulation(self):
#         self.peoples.sort()
#         self.boats.sort()
#         for boat_time, stop_type, seats in self.boats:
#             present_passengers = [p for p in self.peoples if p <= boat_time]
#             if len(present_passengers) > self.max_queue:
#                 self.max_queue = len(present_passengers)
#             taken_seats = min(seats, len(present_passengers))
#             for _ in range(taken_seats):
#                 p_time = self.peoples.pop(0)
#                 wait_time = (boat_time - p_time).total_seconds() / 60
#                 self.time.append(wait_time)
#             print(
#                 f"[{boat_time.strftime('%H:%M')}] Boat ({stop_type}). Seats: {seats}, "
#                 f"Taken: {taken_seats}, Left: {len(self.peoples)}"
#             )
#     def show_results(self, N):
#         avg_wait = sum(self.time) / len(self.time) if self.time else 0
#         print(f"\n1. Average waiting time: {avg_wait:.1f} min.")
#         print(f"2. Max queue: {self.max_queue} people.")
#         if self.max_queue <= N:
#             print(f"3. Result: Interval is SUFFICIENT (Queue <= N={N})")
#         else:
#             print(f"3. Result: Interval is INSUFFICIENT (Queue > N={N})")
#
# random.seed(42)
# pier = Pier()
# for minute in range(0, 20, 2):
#     pier.add_passenger(f"08:{minute:02d}")
# for minute in range(0, 40, 10):
#     pier.add_passenger(f"13:{minute:02d}")
# pier.add_boat("08:10", stop_type="regular")
# pier.add_boat("08:20", stop_type="terminal")
# pier.add_boat("13:30", stop_type="regular")
# pier.process_simulation()
# pier.show_results(N=5)



#3
# class Dictionary:
#     def __init__(self):
#         self.words = {}
#     def add_word(self, word, tr):
#         if word == "" or tr == "":
#             return False
#         if word not in self.words:
#             self.words[word] = {"tr": [], "count": 0}
#         self.words[word]["tr"].append(tr)
#         return True
#     def search(self, word):
#         if word not in self.words:
#             return None
#         self.words[word]["count"] += 1
#         return self.words[word]["tr"]
#     def add_translation(self, word, tr):
#         if word not in self.words or tr == "":
#             return False
#         self.words[word]["tr"].append(tr)  # push
#         return True
#     def change_translation(self, word, tr):
#         if word not in self.words or tr == "":
#             return False
#         self.words[word]["tr"][-1] = tr
#         return True
#     def delete_translation(self, word):
#         if word not in self.words or len(self.words[word]["tr"]) < 2:
#             return None
#         return self.words[word]["tr"].pop()
#     def change_word(self, old, new):
#         if old not in self.words or new == "" or new in self.words:
#             return False
#         self.words[new] = self.words.pop(old)
#         return True
#     def delete_word(self, word):
#         if word not in self.words:
#             return False
#         del self.words[word]
#         return True
#     def top(self, popular):
#         items = sorted(self.words.items(), key=get_count, reverse=popular)
#         return items[:10]
# def get_count(item):
#     return item[1]["count"]
# d = Dictionary()
# for w, t in [("apple", "яблоко"), ("book", "книга"), ("book", "бронировать"),
#              ("run", "бежать"), ("run", "бег"), ("cat", "кошка"), ("dog", "собака")]:
#     d.add_word(w, t)
# while True:
#     print("\n1 Заполнить  \n2 Найти  \n3 Добавить перевод  \n4 Изменить перевод")
#     print("5 Удалить перевод  \n6 Добавить слово  \n7 Изменить слово  \n8 Удалить слово")
#     print("9 Топ-10 популярных  \n10 Топ-10 непопулярных  \n11 Выход")
#     choice = input("Выбор: ").strip()
#     if choice == "1":
#         while True:
#             w = input("Слово (Enter - закончить): ").strip().lower()
#             if w == "":
#                 break
#             if not d.add_word(w, input("Перевод: ").strip().lower()):
#                 print("Нужен перевод!")
#     elif choice == "6":
#         w = input("Новое слово: ").strip().lower()
#         if w in d.words:
#             print("Такое слово уже есть.")
#         elif not d.add_word(w, input("Перевод: ").strip().lower()):
#             print("Слово и перевод не должны быть пустыми.")
#     elif choice in ("2", "3", "4", "5", "7", "8"):
#         w = input("Слово: ").strip().lower()
#         if w not in d.words:
#             print("Такого слова нет.")
#         elif choice == "2":
#             print("Переводы:", ", ".join(d.search(w)))
#         elif choice == "3":
#             d.add_translation(w, input("Новый перевод: ").strip().lower())
#         elif choice == "4":
#             d.change_translation(w, input("Новый вариант (заменит верхний): ").strip().lower())
#         elif choice == "5":
#             removed = d.delete_translation(w)
#             if removed is None:
#                 print("Это последний перевод, удалите слово целиком (пункт 8).")
#             else:
#                 print("Удалён:", removed)
#         elif choice == "7":
#             if not d.change_word(w, input("Новое написание: ").strip().lower()):
#                 print("Пусто или такое слово уже есть.")
#         elif choice == "8":
#             d.delete_word(w)
#             print("Слово удалено.")
#     elif choice in ("9", "10"):
#         for word, data in d.top(choice == "9"):
#             print(word, "-", data["count"])
#     elif choice == "11":
#         break
#     else:
#         print("Введите число от 1 до 11.")



#4
class TaxInspectorate:
    def __init__(self):
        self.db = {
            "1001": {
                "name": "Иванов Иван Иванович", "city": "Днепр",
                "fines": [
                    {"type": "Просрочка декларации", "amount": 500.0, "desc": "Подана на 10 дней позже срока"},
                    {"type": "Неуплата налога", "amount": 1500.0, "desc": "Не уплачен налог за 2025 год"}
                ]
            },
            "1002": {
                "name": "Петрова Мария Сергеевна", "city": "Киев",
                "fines": [{"type": "Неуплата налога", "amount": 1200.0, "desc": "Не уплачен налог на имущество"}]
            },
            "1003": {"name": "Сидоренко Олег Петрович", "city": "Днепр", "fines": []}
        }
    def _read_txt(self, pmt):
        while True:
            val = input(pmt).strip()
            if val: return val
            print("Ошибка: строка не должна быть пустой.")
    def _read_num(self, pmt, max_v, is_flt=False):
        while True:
            val = input(pmt).strip().replace(",", ".")
            try:
                num = float(val) if is_flt else int(val)
                if num >= 0 and (is_flt or num <= max_v): return num
            except ValueError:
                pass
            print(f"Ошибка: введите корректное число (от 0 до {max_v if not is_flt else 'максимума'}).")
    def _get_code(self):
        code = self._read_txt("Введите код человека: ")
        if code in self.db: return code
        print(f"Человека с кодом {code} нет в базе.")
        return ""

    def _print_p(self, code):
        p = self.db[code]
        print(f"\nКод: {code}\nФИО: {p['name']}\nГород: {p['city']}")
        if not p["fines"]:
            print("Штрафов нет.")
            return
        print("Штрафы:")
        for i, f in enumerate(p["fines"], 1):
            print(f"  {i}. {f['type']} - {f['amount']} грн ({f['desc']})")
        print(f"  Итого: {sum(f['amount'] for f in p['fines'])} грн")
    def find(self, mode):
        val = self._read_txt(["Код для поиска: ", "Тип штрафа: ", "Город: "][mode]).lower()
        found = False
        for code, p in self.db.items():
            if (mode == 0 and code == val) or \
                    (mode == 1 and any(val in f["type"].lower() for f in p["fines"])) or \
                    (mode == 2 and p["city"].lower() == val):
                self._print_p(code)
                found = True
        if not found: print("Ничего не найдено.")
    def add_person(self):
        code = self._read_txt("Новый уникальный код: ")
        if code in self.db: return print("Такой код уже есть!")
        self.db[code] = {"name": self._read_txt("ФИО: "), "city": self._read_txt("Город: "), "fines": []}
        print("Человек добавлен.")
    def add_fine(self):
        if code := self._get_code():
            self.db[code]["fines"].append({
                "type": self._read_txt("Тип штрафа: "),
                "amount": self._read_num("Сумма: ", 0, True),
                "desc": self._read_txt("Описание: ")
            })
            print("Штраф добавлен.")
    def delete_fine(self):
        if (code := self._get_code()) and self.db[code]["fines"]:
            self._print_p(code)
            idx = self._read_num("Номер штрафа для удаления (0 - отмена): ", len(self.db[code]["fines"]))
            if idx:
                self.db[code]["fines"].pop(idx - 1)
                print("Штраф удалён.")
    def edit(self, target_fine=False):
        if not (code := self._get_code()): return
        fines = self.db[code]["fines"]
        if target_fine and not fines: return print("У этого человека нет штрафов.")
        self._print_p(code)
        if target_fine:
            idx = self._read_num("Номер штрафа для изменения (0 - отмена): ", len(fines))
            if not idx: return
            fine = fines[idx - 1]
            ch = self._read_num("1 - тип, 2 - сумма, 3 - описание, 0 - отмена\nВыбор: ", 3)
            if ch == 1:
                fine["type"] = self._read_txt("Новый тип: ")
            elif ch == 2:
                fine["amount"] = self._read_num("Новая сумма: ", 0, True)
            elif ch == 3:
                fine["desc"] = self._read_txt("Новое описание: ")
        else:
            ch = self._read_num("1 - изменить ФИО, 2 - изменить город, 0 - отмена\nВыбор: ", 2)
            if ch == 1:
                self.db[code]["name"] = self._read_txt("Новое ФИО: ")
            elif ch == 2:
                self.db[code]["city"] = self._read_txt("Новый город: ")
        if ch: print("Данные изменены.")
    def run(self):
        menu = (
            "\n===== БАЗА ШТРАФОВ НАЛОГОВОЙ ИНСПЕКЦИИ =====\n"
            "1. Показать всю базу\n2. Поиск по коду\n3. Поиск по типу штрафа\n"
            "4. Поиск по городу\n5. Добавить человека\n6. Добавить штраф\n"
            "7. Удалить штраф\n8. Изменить данные человека\n9. Изменить штраф\n10. Выход"
        )
        while True:
            print(menu)
            ch = input("Выберите пункт (1-10): ").strip()
            if ch == "1":
                if not self.db: print("База пуста.")
                for c in self.db: self._print_p(c)
            elif ch in ("2", "3", "4"):
                self.find(int(ch) - 2)
            elif ch == "5":
                self.add_person()
            elif ch == "6":
                self.add_fine()
            elif ch == "7":
                self.delete_fine()
            elif ch == "8":
                self.edit(target_fine=False)
            elif ch == "9":
                self.edit(target_fine=True)
            elif ch == "10":
                return print("До свидания!")
            else:
                print("Ошибка: введите число от 1 до 10.")
if __name__ == "__main__":
    TaxInspectorate().run()




