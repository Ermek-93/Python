import numpy as np
q = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def printM(a):
    for i in range(len(a)):
        print(a[i])

#умножения на число
def umnoznaChislo(a,x = int(input(print("Число на которое надо умножить")))):
    for i in range(len(a)):
     for j in range(len(a)):
        a[i][j]*=x
    return printM(a)

print("Результат")
umnoznaChislo(q)

