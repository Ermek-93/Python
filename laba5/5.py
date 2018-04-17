#Дан рандомно заполненный массив и значение Z.
# Найти в этом массиве ближайшее к Z значение.

import numpy as np
a = np.arange(10)
b = np.random.uniform(0,10)
index = (np.abs(a-b)).argmin()
print(a)
print(b)
print(a[index])
