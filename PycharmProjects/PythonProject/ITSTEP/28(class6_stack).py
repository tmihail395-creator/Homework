stack=[]
# stack.append(10)
# stack.append(20)
# stack.append(30)
#
# print(stack)
#
# value=stack.pop()
# print(value)
# print(stack)

# stack.append("A")
# stack.append("B")
# stack.append("C")
#
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
#
# print(f"last element: {stack[-1]}")





# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
#
# print(stack.peek())
# print(stack.pop())
# print(stack.peek())
#
# stack=Stack()
# try:
#     stack.pop()
# except IndexError:
#     print("IndexError")
#
# book_stack=Stack()
# book_stack.push("Harry Potter")
# book_stack.push("The Hobbit")
# book_stack.push("Dune")
#
# print(book_stack.peek())
# print(book_stack)
# print(book_stack.pop())
class Stack:
    def __init__(self):
        self.items = []
        self.max_length = 5
    def __str__(self):
        return str(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def max_size(self):
        return self.max_length
    def is_full(self):
        return self.size() == self.max_length
    def clear(self):
        self.items.clear()
stack = Stack()
# while True:
#     choice = int(input("Оберіть операцію: \n"
#                        "1. Додати ціле значення\n"
#                        "2. Виштовхнути значення\n"
#                        "3. Кількість елементів\n"
#                        "4. Перевірити, чи порожній стек\n"
#                        "5. Перевірити, чи повний стек\n"
#                        "6. Очистити стек\n"
#                        "7. Переглянути верхній елемент\n"
#                        "8. Показати стек\n"
#                        "0. Вихід\n"
#                        "----->"))
#     if choice == 1:
#         full = int(input("Ваше ціле число: "))
#         stack.push(full)
#         print(stack)
#     elif choice == 2:
#         print(f"Stack виштовхує: {stack.pop()}")
#     elif choice == 3:
#         print("Кількість елементів:", stack.size())
#     elif choice == 4:
#         print("Stack порожній:", stack.is_empty())
#     elif choice == 5:
#         print("Стек повний:", stack.is_full())
#     elif choice == 6:
#         stack.clear()
#         print("Стек очищено.")
#     elif choice == 7:
#         print("Верхній елемент:", stack.peek())
#     elif choice == 8:
#         print("Стек:", stack)
#     elif choice == 0:
#         break


class Player:
    def __init__(self, name):
        self.name = name
        self.x=0
        self.y=0

        self.history=Stack()
    def show_position(self):
        print(f"{self.name}: ({self.x},{self.y})")
    def move(self, dx, dy):
        self.history.push({self.x,  self.y})
        self.x += dx
        self.y += dy
        print(f"{self.name}: moved")
        self.show_position()
    def undo_move(self):
        old_position=self.history.pop()
        if old_position is None:
            print("No more moves")
            return
        self.x, self.y = old_position
        print("last move canceled!")
        self.show_position()


player = Player("Qwert")
player.show_position()
player.undo_move()
player.move(4, 8)
player.move(2, 5)
player.move(6, 7)
print("-------undo------")
player.undo_move()




class BracketChecker:
    def __init__(self):
        self.stack =Stack()
    def check(self, text):
        pairs ={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for symbol in text:
            if symbol in pairs.values():
                self.stack.push(symbol)
            elif symbol in pairs.keys():
                if self.stack.is_empty():
                    print(f"Error! Extra closing parenthesis: {symbol}!")
                    return False
                elif self.stack.peek() != pairs[symbol]:
                    print(f"Error! Bracket: {symbol} not for {self.stack.peek()}!")
                    return False
                self.stack.pop()
        if not self.stack.is_empty():
            print(f"Error! The bracket {self.stack.peek()} does not close the pair!")
            return False
        return True

checker = BracketChecker()
text = input("Enter a text: ")
if checker.check(text):
    print("Bracket correct!")
else:
    print("Bracket incorrect!")