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


# Task 24
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# from random import randint


# n = 6
# initList = [0]*n
# for i in range(n):
#     initList[i] = randint(0, 1000)/100
# print(initList)
# fractList = [0]*n
# for i in range(n):
#     fractList[i] = round(initList[i] % 1, 3)
# print(max(fractList)+min(fractList))


# Task 25
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# result = ""
# n = int(input("Insert N: "))

# # Функция
# result2 = bin(n)
# print(result2.split("b")[1])

# # Алгоритм
# if n == 0:
#     print(n)
# while (n > 0):
#     result = str(n % 2) + result
#     n = n//2
# print(result)


# Task 26
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


# k = int(input("Inset k: "))

# fibonacciList = [0]*(k*2+1)
# fibonacciList[k] = 0
# fibonacciList[k+1] = 1

# for i in range(k+2, len(fibonacciList)):
#     fibonacciList[i] = fibonacciList[i-2]+fibonacciList[i-1]

# for i in range(k, -1, -1):
#     fibonacciList[i] = fibonacciList[i+2]-fibonacciList[i+1]

# print(fibonacciList)
