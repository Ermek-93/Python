import numpy as np

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[3, 3, 3], [2, 2, 2], [1, 1, 1]]

def printM(a):
    for i in range(len(a)):
        print(a[i])

#Функция сложения двух матриц
def slozhenie(a,b):
    for i in range(len(a)):
        for j in range(len(a)):
           a[i][j]+= b[i][j]
    return printM(a)

print("Результат сложения двух матриц")
slozhenie(m,n)




