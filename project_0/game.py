import numpy as np

def random_predict_min(number:int=1) -> int:
    """Угадываем число за минимальный проход, используя randinit

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    predict_number = 50
    low_range, high_range  = 1,101

    while True:
        count += 1
        
        if number == predict_number:
            break # выход из цикла, если угадали        
        if number < predict_number:
            high_range = predict_number
        else:
            low_range = predict_number
        
        # предполагаемое число в сужаемом диапазоне
        predict_number = np.random.randint(low_range, high_range)
    
    return(count)


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict_min)