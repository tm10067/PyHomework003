# 1. Задайте рандомно список из чисел размером N, где N число с клавиатуры. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

N = int(input("введите длину списка: "))
list = []
for i in range(N):
    list.append(randint(1,10))
print(list)
list_odd = []
for j in range(0, len(list), 2):
    list_odd.append(list[j]) 
print(list_odd)
print(sum(list_odd))
