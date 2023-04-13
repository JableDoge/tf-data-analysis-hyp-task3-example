import pandas as pd
import numpy as np

import scipy.stats as stats


chat_id = 707776914 # Ваш chat ID, не меняйте название переменной

def solution(control_npv: np.array, test_npv: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.05
    t_stat, p_val = stats.ttest_ind(control_npv, test_npv, equal_var=True)

    if p_val < alpha:
        t = True
    else:
        t = False   
    return t
