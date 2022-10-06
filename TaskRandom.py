# Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

import time

def random(min, max):
    num = time.time()
    rnd = round((num * 10 - int(num * 10)) * (max - min) + min, 2)
    return rnd

print(random(1,100))

# ПРИМЕЧАНИЯ: 
# 1) для событий происходящих одновременно никакого рандома не будет.
# 2) при достаточно быстром повторении может быть заметна тенденция к росту значений 
# от минимума к максимуму (для этого домножаем время на 10, чтобы десятые быстрее прокручивались).