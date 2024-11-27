import numpy as np
import pandas as pd

def calculate_expectation_variance(data):
    """
    Рассчитать математическое ожидание и дисперсию по данным таблицы.
    data: DataFrame с колонками 'X' и 'P', где:
        - X: значения случайной величины
        - P: вероятности, соответствующие этим значениям
    Возвращает математическое ожидание и дисперсию.
    """
    # Математическое ожидание
    expectation = np.sum(data['X'] * data['P'])

    # Дисперсия
    variance = np.sum((data['X'] ** 2) * data['P']) - expectation ** 2

    return expectation, variance


# Пример 1
data_1 = pd.DataFrame({
    'X': [-1, 0, 1, 2],
    'P': [0.2, 0.1, 0.3, 0.4]
})

# Пример 2
data_2 = pd.DataFrame({
    'X': [2, 3, 5],
    'P': [0.1, 0.6, 0.3]
})

# Расчет для Примера 1
expectation_1, variance_1 = calculate_expectation_variance(data_1)

# Расчет для Примера 2
expectation_2, variance_2 = calculate_expectation_variance(data_2)

print(f"Пример 1: M[X] = {expectation_1}, D[X] = {variance_1}")
print(f"Пример 2: M[X] = {expectation_2}, D[X] = {variance_2}")
