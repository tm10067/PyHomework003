# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# 45 -> 101101
# 3 -> 11
# 2 -> 10
# print(f"Число {num} в двоичной системе это {binum})

number = int(input("введите число: "))
number_dec = number
number_bin = 0
position = 0
while number_dec >= 1:
    if number_dec % 2 != 0:
        number_bin += (number_dec % 2) * 10 ** position
    number_dec = number_dec // 2
    position += 1
print(f'Число {number} в двоичной системе равно {number_bin}')

print(bin(number))