import numpy as np
n = 3
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = [[x[i] for x in a] for i in range(n)]
for z in a:
    print(z)
for j in range(n - 1, -1, -1):
    for i in a:
        print(i[j], end=" ")
    print()
