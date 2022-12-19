# -*- coding: cp1251 -*-
import numpy as np

def random_predict(number:int=1) -> int:
    """�������� ��������� �����

    Args:
        number (int, optional): ���������� �����. Defaults to 1.

    Returns:
        int: ����� �������
    """
    
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # �������������� �����
        if number == predict_number:
            break # ����� �� �����, ���� �������
    return(count)

def score_game(random_predict) -> int:
    """�� ����� ���������� ������� � ������� �� 1000 �������� ��������� ��� ��������

    Args:
        random_predict ([type]): ������� ����������

    Returns:
        int: ������� ���������� �������
    """

    count_ls = [] # ������ ��� ���������� ���������� �������
    np.random.seed(1) # ��������� ��� ��� �����������������
    random_array = np.random.randint(1, 101, size=(1000)) # �������� ������ �����

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # ������� ������� ���������� �������

    print(f'��� �������� ��������� ����� � ������� ��: {score} �������')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
#