#Дано N, M. Сгенерируйте N рандомных чисел используя нормальное распределение.
# Разбейте их на на M равных частей. Постройте гистограмму, найдите медиану,
# моду и среднее значения, покажите их на графике. Пример: N=1000, M=40. Результат:

import numpy as np

N = 3
lst = np.random.randn(N)

print("\nRaw data:", lst)
lst.sort()
print("Sorted data:", lst)


def mean(list):
    return float(sum(list)/len(list))


def median(list):
    median_pos = (len(list)+1)/2
    if median_pos == int(median_pos):
        median_pos = int(median_pos-1)
        return list[median_pos]
    else:
        med_avg = []
        med_avg.append(list[int(median_pos-1.5)])
        med_avg.append(list[int(median_pos-.5)])
        return mean(med_avg)



print("Mean:", mean(lst))
print("Median:", median(lst))
