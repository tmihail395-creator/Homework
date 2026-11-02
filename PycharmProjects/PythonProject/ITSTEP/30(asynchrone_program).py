#в программе есть 1 процесс и 1 поток
#в программе можно создать больше одного потока
#но у каждой свой ресурс



import threading
import time
# print("test1")
# print("test2")
#
# print(threading.current_thread().name)
#
# def work():
#     print(f"Start work: {threading.current_thread().name}")
#     time.sleep(2)
#     print(f"End work{threading.current_thread().name}")
#
# thread=threading.Thread(target=work)
# thread.start()
# thread.join()





# def download(filename):
#     print("start")
#     print("downloading ", filename)
#     time.sleep(3)
#     print("finish")
#
# thread = threading.Thread(target=download, args=("download.txt",))
# thread.start()
# thread.join()
#
# start=time.perf_counter()
# download("test.txt")
# download("test.txt")
# download("test.txt")
#
# print(time.perf_counter()-start)
#
# t1=threading.Thread(target=download, args=("text.txt",))
# t2=threading.Thread(target=download, args=("photo.jpg",))
# t3=threading.Thread(target=download, args=("audio.mp4",))
#
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
#
# print("End working program")





# balance=1000
# lock=threading.Lock()
# def withdraw(name, amount):
#     global balance
#     with lock:
#     #with lock помогает расделить потоки
#         print("Check balance")
#         if amount <= balance:
#             time.sleep(1)
#             balance -= amount
#             print(name, "get", amount)
#         else:
#             print(name, 'not enough money')
#
# t1=threading.Thread(target=withdraw, args=("Anya", 100))
# t2=threading.Thread(target=withdraw, args=("Misha", 1000))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print(balance)

from queue import Queue

# tasks=Queue()

# tasks.put("photo.ipg")
# tasks.put("music.mp3")
# tasks.put("music.mp4")
#
# while not tasks.empty():
#     task=tasks.get()
#     print(task)
#     tasks.task_done()
#
# print("Waiting...")
# tasks.join()
# print("All tasks done")


# def worker():
#     while True:
#         task=tasks.get()
#         print("start task", task)
#         time.sleep(2)
#         print("end task", task)
#         tasks.task_done()
#
#
# thread=threading.Thread(target=worker)
# thread.start()9
#
# tasks.put("photo.ipg")
# tasks.put("music.mp3")
# tasks.put("music.mp4")
# print("all tasks added")
#
# tasks.join()

from multiprocessing import Process
import os
#
# def work():
#     print("p id", os.getpid())
#
# if __name__ == "__main__":
#     print("p id", os.getpid())
#     p1=Process(target=work)
#     p2=Process(target=work)
#     time.sleep(30)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()


#2
nums=list(input("Nums: ").split(", "))

def sum_n(nums):
    print(f'Sum numbers: {int(sum(map(int, nums)))}')

def ser_n(nums):
    count=len(nums)
    max_n=int(sum(map(int, nums)))
    ser=max_n/count
    print(f'Min number: {ser}')

p1=threading.Thread(target=sum_n,args=(nums,))
p2=threading.Thread(target=ser_n,args=(nums,))

p1.start()
p2.start()
p1.join()
p2.join()




