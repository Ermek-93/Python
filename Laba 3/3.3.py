import numpy as np

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[3, 3, 3], [2, 2, 2], [1, 1, 1]]

def printM(a):
    for i in range(len(a)):
        print(a[i])


#транспонированная матрица
def trans(a):
    for i in range(len(a)):
     for j in range(0,i):
         tmp = a[i][j]
         a[i][j]=a[j][i]
         a[j][i]=tmp
    return printM(a)


print("Транспонированная матрица")
trans(m)


