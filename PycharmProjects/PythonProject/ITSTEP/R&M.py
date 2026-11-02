#v1
# while True:
#     import random
#     ask=input("Для чего я создан?\n"
#               "")
#     answer = random.choice(["....", "Боже мой...", "Блять да ты издеваешься", "Ооххх бляять"])
#     if ask:
#         i = 0
#         time = 0
#         while i == time:
#             time = random.randint(10000, 10000000)
#             for i in range(1, time):
#                 if i == time:
#                     break
#         print(answer)


with open("ram.txt", "w", encoding="utf-8") as f:

    while True:
        import random
        ask=input("Для чего я создан?\n"
                  "")
        answer = random.choice(["....", "Боже мой...", "Блять да ты издеваешься", "Ооххх бляять"])
        if ask:
            i = 0
            time = 0
            while i == time:
                time = random.randint(10000, 10000000)
                for i in range(1, time):
                    if i == time:
                        break
            print(answer)
