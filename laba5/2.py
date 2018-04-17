#Создайте двумерный массив размера NxN со значением 1
# на границах и 0 внутри.
import numpy as np
n = int(input())
a = [n,n]
a = np.ones((n,n))

a[0:len(a)-1,len(a)-1] = 0
a[len(a)-1,0:] = 0
a[0,:len(a)-1]=0
a[1:,0:1]=0


print(a)
