#Найти ранг случайной матрицы.

import numpy as np
Z = np.random.uniform(1,3,(3,3))
rank = np.linalg.matrix_rank(Z)
print(Z)
print(rank)
