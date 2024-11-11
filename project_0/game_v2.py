'''Игра "Угадай число"
Компьютер сам загадывает и сам угадывает число'''

import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000
    подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

def fast_predict(number: int = 1) -> int:
    """Угадываем число меньше, чем за 20 попыток, в среднем за 5 попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    low = 1
    high = 100
    
    while True:
        count += 1
        
        # Предполагаемое число - среднее между low и high
        predict_number = (low + high) // 2  
        
        if number == predict_number:
            break
        elif number < predict_number:
            high = predict_number - 1
        else:
            low = predict_number + 1
            
    return count

# if __name__ == '__main___': #Для импорта

# RUN
# score_game(random_predict)
score_game(fast_predict)