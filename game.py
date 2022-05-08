"""Game - predict number"""
import numpy as np

number = np.random.randint(1,1000) # загадываем число

#количество попыток
count = 0

while True:
    count +=1
    predict_number = int(input('Введите число '))
                         
    if predict_number > number:
        print('Число должно быть меньше')
    elif predict_number < number:
        print('Число должно быть больше')
    else:
        print('Вы отгадали число за {} попыток!!! Это число {}.' .format(count, number))
        break #конец игры и выход из цикла 
