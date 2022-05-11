"""Game predict number. Version 3."""
import numpy as np
from numpy import random

#number = random.randint(1,101) # загадываем число

def predict_number_game(number: int=1) -> int:
    """Угадываем число методом золотого сечения

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_number = 1
    max_number = 100
    
    while True:
        count+=1
        predict_number = 1 #проверяем число 1, чтобы избежать зацикленности
        if predict_number == number:
            print(f'Число {predict_number} найдено за 1 попытку')
            break 
        
        predict_number = round(min_number + (max_number - min_number)/1.618) #метод золотого сечения
        if predict_number == number:
            print(f'Число {predict_number} найдено за {count} попыток')
            break 

        elif predict_number > number:
            max_number = predict_number
            #print(max_number)
            
        elif predict_number < number:
            min_number = predict_number
            #print(min_number)
            
    return(count)

def score_game(predict_number_game) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_number_game (_type_): функция угадывания 

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))   #загадали список чискл
    print(random_array)
    for number in random_array:
        count_ls.append(predict_number_game(number))
    
    score = int(np.mean(count_ls)) #находим среднее число попыток
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return(score)

if __name__ == '__main__':
    #RUN
    score_game(predict_number_game)

#predict_number_game(100)