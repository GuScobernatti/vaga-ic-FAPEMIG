import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


def rolling_mean(corrente, time):
    return corrente.rolling(window=10, min_periods=1).mean()


def feature1(rolling_mean_corrente, time, corrente):
    f1 = np.max(rolling_mean_corrente)
    limit = 0.02 * f1
    findIndex_f1 = np.argmax(rolling_mean_corrente > limit)
    f1_time = time[findIndex_f1]
    corrente_f1 = corrente[findIndex_f1]
    return findIndex_f1, f1_time, corrente_f1


def feature2(rolling_mean_corrente, time, corrente, findIndex_f1, findIndex_f6):
    limitValues = rolling_mean_corrente[findIndex_f1:findIndex_f6]
    max_value = np.max(rolling_mean_corrente)
    peaks, _ = find_peaks(
        limitValues, height=0.4 * max_value, prominence=0.05 * max_value
    )

    if len(peaks) > 0:
        findIndex_f2 = peaks[0] + findIndex_f1
        f2_time = time[findIndex_f2]
        corrente_f2 = corrente[findIndex_f2]
        return findIndex_f2, f2_time, corrente_f2
    else:
        return None, None, None


def feature3(rolling_mean_corrente, time, corrente, findIndex_f2, findIndex_f4):
    if findIndex_f2 is None or findIndex_f2 >= findIndex_f4:
        return None, None

    limitValues = rolling_mean_corrente[findIndex_f2:findIndex_f4]

    if len(limitValues) == 0:
        return None, None

    findInext_f3 = np.argmin(limitValues) + findIndex_f2
    f3_time = time[findInext_f3]
    corrente_f3 = corrente[findInext_f3]
    return f3_time, corrente_f3


def feature4(rolling_mean_corrente, time, corrente):
    findIndex_f4 = np.argmax(rolling_mean_corrente)
    f4_time = time[findIndex_f4]
    corrente_f4 = corrente[findIndex_f4]
    return findIndex_f4, f4_time, corrente_f4


def feature5(rolling_mean_corrente, time, corrente, findIndex_f4, findIndex_f6):
    f5 = np.max(rolling_mean_corrente)
    limit = 0.90 * f5

    limitValues = rolling_mean_corrente[findIndex_f4:findIndex_f6]
    findIndex_f5 = np.argmax(limitValues < limit) + findIndex_f4
    f5_time = time[findIndex_f5]
    corrente_f5 = corrente[findIndex_f5]
    return f5_time, corrente_f5


def feature6(rolling_mean_corrente, time, corrente):
    f6 = np.max(rolling_mean_corrente)
    limit = 0.02 * f6

    max_index = np.argmax(rolling_mean_corrente)
    valuesAfter_max_index = rolling_mean_corrente[max_index:]

    findIndex_f6 = np.argmax(valuesAfter_max_index < limit) + max_index
    f6_time = time[findIndex_f6]
    corrente_f6 = corrente[findIndex_f6]
    return findIndex_f6, f6_time, corrente_f6
