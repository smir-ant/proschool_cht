# l = []  # список(list) - изменяемый
# t = ()  # кортеж(tuple) - нельзя менять
#
# # СЛОВАРИ
# d = {}  # пустой словарь
# d["Ботинок"] = "Тяги лютые"  # добавление записи в словарь
# d["Бошмак"] = "Тяги бархатные"
# print(d)
# del d["Ботинок"]  # удаление записи из словаря
# print(d)


# d1 = {
#     "bashmak": "adidas",
#     "bashmak": "nike",
#     5: "пять",
# }
# print(d1["bashmak"])
# for key in d1:  # перебор ключей
#     print(key)
#
# for v in d1.values():  # перебор значений
#     print(v)
#
# for key, val in d1.items():  # (ключ, значение)
#     print("[Ключ]:", key, "[Значение]:", val)


# l = [4, 2, 7]
# del l[1]  # удаление по индексу
# print(l)
#
# del l  # удаление значения



# slov = {
#     "Один": 1,
#     "Два": 2,
#     "Три": 3
# }
#
# values = list(slov.values())
# print(values)
# keys = list(slov.keys())
# print(keys)


# множество -> set
# s = set()  # пустое множество
# s1 = {"A", "B", "C", "A", "D"}
# # 1) ПОВТОРЕНИЯ ИСКЛЮЧЕНЫ
# # 2) нет порядка
# print(s1)


# s1 = ["A", "B", "C", "A", "D"]
# s2 = set(s1)
#
# if len(s1) != len(s2):
#     print(True)


s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

print(s1 | s2)  # то же самое что и s1.union(s2)
print(s1 & s2)  # .intersection()
print(s1 - s2)  # .difference()
print(s1 ^ s2)  # .symmetric_difference()






