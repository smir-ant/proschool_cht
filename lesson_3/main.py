# import random
#
# number = random.randint(4, 23)  # random + integer
# print(number)
#
# l = [1, 2, 3]
# random.shuffle(l)  # shuffle - случ. перемешать
# print(l)
#
# l = [1, 2, 3]
# print(random.choice(l))  # choice - случ. выбор

# ==================
from time import sleep, time
from random import randint

# print(3)
# sleep(0.99)
# print(2)
# sleep(1.01)
# print(1)

# Быстрый стрелок
#
# t = randint(2, 5)  # время ожидания случ. (от 2 до 5)
# sleep(t)  # случ. ожидание
# start = time()  # фиксируем время
# input("ВЫСТРЕЛ!")  # time will tick while enter not pressed
# end = time()
# dif = end - start
# print(dif)
#
# if dif == 0.0:
#     print("Ни-ни 🚫")
# elif dif >= 0.4:
#     print("Грустно 😔")
# else:
#     print("Четко 😎")






# ЦИКЛЫ.
# WHILE -> пока <условие>
# x = 5
# while x > 0:
#     print("Антон")
    # x = x - 1

while True:  # бесконечный цикл
    name = input("Введи никнейм:")
    if name[0].isdigit():  # 0-9
        continue  # перезапуск
    else:  # это не число -> все ок
        print("Ок, пойдет")
        break  # выход из цикла

"15".isdigit()

