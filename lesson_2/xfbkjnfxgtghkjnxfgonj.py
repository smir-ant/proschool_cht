# print(5 / 0)
# if 4 == 3
# x = ["А", 1, True]
# print(x[3])

# try:
#     x = int(input("Введи число: "))
# except ValueError:
#     print("Не хочу")
# else:  # что делать если ошибок не было
#     try:
#         result = 5 / x
#     except ZeroDivisionError:
#         print("Низя")
# finally:  # сработает в любом случае
#     print("Я поработал")

# try:
#     x = int(input("Введи число: "))
#     result = 5 / x
# except Exception:  # Exception - общий класс ошибок
#     print("Ну ты балбес, конечно")

name = input("Ник:")
try:
    if name == "Антон":
        raise ZeroDivisionError("Ты сделал такую же тупость, ка ки деление на ноль 🚫")  # поднять исключение
except ZeroDivisionError as error_msg:
    print("Что-то пошло не по плану.", error_msg)
