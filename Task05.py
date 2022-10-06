# 5. Задайте число - размер списка. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

N = int(input("введите количество индексов: "))

def fibo(x):
    result = 0
    if x == 0:
        result = 0
    elif abs(x) == 1:
        result = 1
    elif x > 1:
        result += fibo(x - 1) + fibo(x - 2)
    elif x < -1:
        result += fibo(x + 2) - fibo(x + 1)
    return result

list_fibo = []
for i in range(-N, N + 1):
    list_fibo.append(fibo(i))
print(list_fibo)
