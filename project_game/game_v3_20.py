"""Игра угадай число
Компьютер сам загадывает и сам угадывает число, меньше чем за 20 попыток
"""
import numpy as np
number = np.random.randint(1, 101) # загадываем рандомное число, используя генератор рандомных чисел


def random_predict(number) -> int:
    """Компьютер угадывает рандомное число

    Args:
        number (int, optional): Загаданное число.
        
    Returns:
        int: Число попыток
    """
    
    count = 0
    mn = 1
    mx = 100
    

    while True:
        count += 1
        md = round((mn + mx)/2)
        
        if md > number:
            mx = md
        elif md < number:
            mn = md
        else:
            print(f'Компьютер угадал загаданное число за {count} попыток. Это число {number}')
            break # конец игры и выход из цикла
        
    return(count)

print(f'Количество попыток: {random_predict(number)}')