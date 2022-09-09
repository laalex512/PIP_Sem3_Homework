# # Task 22
# # Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# # Пример:
# # - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint

# n = 5
# lst = [0]*n
# sum = 0
# for i in range(n):
#     lst[i] = randint(0, 10)
#     if (i % 2 != 0):
#         sum += lst[i]
# print(lst)
# print(sum)


# Task 23
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint


# n = int(input("Insert coun of list: "))
# initList = [0]*n
# for i in range(n):
#     initList[i] = randint(0, 10)
# print(initList)
# resultList = []
# for i in range(round(n/2+0.25)):
#     resultList.append(initList[i]*initList[n-1-i])
# print(resultList)
