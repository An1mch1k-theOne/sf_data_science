'''Игра угадай число '''
import numpy as np

number = np.random.randint(1, 100)

# Количество попыток
count = 0

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100: "))
    
    if predict_number > number:
        print("Ваше число больше, чем загаданное.")
        
    elif predict_number < number:
        print("Ваше число меньше, чем загаданное.")
        
    elif predict_number == number:
        print(f"Вы угадали число {number} за {count} попыток!")
        break