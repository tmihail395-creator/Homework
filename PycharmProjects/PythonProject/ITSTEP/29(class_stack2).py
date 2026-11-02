# class BankQueue:
#     def __init__(self):
#         self.clients = []
#
#     def add_client(self, client):
#         self.clients.append(client)
#
#     def remove_client(self):
#         if self.is_empty():
#             return None
#         return self.clients.pop(0)
#
#     def is_empty(self):
#         return len(self.clients) == 0
#
#     def size(self):
#         return len(self.clients)
#
#     def next_client(self):
#         if self.is_empty():
#             return None
#         return self.clients[0]
#
#     def show_client(self):
#         if self.is_empty():
#             print("Empty bank Queue")
#         else:
#             for client in self.clients:
#                 print(client)
#
#
# bank = BankQueue()
#
# bank.add_client("client 1")
# bank.add_client("client 2")
# bank.add_client("client 3")
#
# bank.show_client()
#
# print(bank.remove_client())
# print("===========after del ===============")
# bank.show_client()
#
# print(bank.next_client())
from collections import deque


# class PrinterQueue:
#     def __init__(self):
#         self.jobs=[]
#         #корень стака
#     def add_jobs(self, job):
#         self.jobs.append(job)
#
#     def print_next(self):
#         if not self.is_empty():
#             print("Empty queue")
#             return
#         return self.jobs.pop(0)
#
#     def is_empty(self):
#         return len(self.jobs) == 0
#
#     def show_jobs(self):
#         if self.is_empty():
#             print("Empty job Queue")
#         else:
#             for job in self.jobs:
#                 print(job)
#
# jobs_queue = PrinterQueue()
# jobs_queue.add_jobs('doc 1')
# jobs_queue.add_jobs('doc 2')
# jobs_queue.add_jobs('doc 3')
# jobs_queue.print_next()
# jobs_queue.show_jobs()


# class PrintJob:
#     def __init__(self, document, pages, priority):
#         self.document = document
#         self.pages = pages
#         self.priority = priority
#     def __str__(self):
#         return
#
# class PrinterQueue:
#     def __init__(self):
#         self.jobs=[]
#
#     def add_jobs(self, job):
#         if isinstance(job, PrintJob):
#             self.jobs.append(job)
#
#     def print_next(self):
#         if not self.is_empty():
#             print("Empty queue")
#             return
#         highest_priority = 0
#         for i in range(1, len(self.jobs)):
#             if self.jobs[i].priority > self.jobs[highest_priority].priority:
#                 highest_priority = i
#         return self.jobs.pop(highest_priority)
#
#     def is_empty(self):
#         return len(self.jobs) == 0
#
#     def show_jobs(self):
#         if self.is_empty():
#             print("Empty job Queue")
#         else:
#             for job in self.jobs:
#                 print(job)
#
# jobs_queue = PrinterQueue()
# jobs_queue.add_jobs(PrintJob('client2', 1, 1))
# jobs_queue.add_jobs(PrintJob('client1', 2, 1))
# jobs_queue.add_jobs(PrintJob('client1', 3, 3))
# print()
# jobs_queue.add_jobs()




# class CircularQueue:
#     def __init__(self, maxsize):
#         self.maxsize = maxsize
#         self.queue = [None] * maxsize
#         self.front = 0
#         self.rear = 0
#         self.count = 0
#
#     def is_empty(self):
#         return self.count ==0
#
#     def is_full(self):
#         return self.count == self.maxsize
#
#     def enqueue(self, value):
#         if self.is_full():
#             print("queue is full")
#             return
#         self.queue[self.rear] = value
#         self.rear=(self.rear+1)%self.maxsize
#         self.count += 1
#
#     def dequeue(self):
#         if self.is_empty():
#             print("queue is empty")
#             return
#
#         value = self.queue[self.front]
#         self.queue[self.front] = None
#         self.front = (self.front+1)%self.maxsize
#         self.count -= 1
#         return value


# class Deque:
#     def __init__(self):
#         self.items = []
#     def is_empty(self):
#         return self.items == []
#     def add_front(self, item):
#         self.items.insert(0, item)
#     def add_back(self, item):
#         self.items.append(item)
#     def remove_front(self):
#         if self.is_empty():
#             print("Deque is empty")
#             return
#         return self.items.pop(0)
#     def remove_back(self):
#         if self.is_empty():
#             print("Deque is empty")
#             return
#         return self.items.pop(0)
#     def show(self):
#         print(self.items)
#
# deq = Deque()
# deq.add_back("Client 1")
# deq.add_back("Client 2")
# deq.add_front("wip client")
# deq.remove_front()
# deq.show()


class PassLog:
    def __init__(self, password, login, user):
        self.password = password
        self.login = login
        self.user = user
        self.safe=[]
    def add(self):
        if self.password and self.login:
            self.safe.append([self.password, self.login])
        else:
            print("Password or login is invalid")
    def add_new(self):
        person=input("Enter your password and login: ").strip().split(', ')
        if person not in self.safe:
            self.safe.append(person)
            print(f"You create account!")
        else:
            print("You was logged last time, welcome to account!")
    def remove_person(self):
        person=input("Enter password and login to delete user: ").strip().split(', ')
        if person in self.safe:
            self.safe.remove(person)
            print(f"You remove account!")
        else:
            print(f"{person} was not found.\n\tRejected!")
    def check_person(self):
        person=input("Enter password and login to check account: ").strip().split(', ')
        if person in self.safe:
            print(f"{person} was found.\n\tData\nPassword: {person}\nLogin:{person}")
        else:
            print(f"{person} was not found.\n\tRejected!")
    def change_data(self):
        person = input("Enter your password and login: ").strip().split(', ')
        if person in self.safe:
            print("Welcome to account!")
            change=input("Enter new password and login to change account: ").strip().split(', ')
            self.safe.remove(person)
            self.safe.append(change)
        else:
            print(f"{person} was not found.\n\tRejected!")
