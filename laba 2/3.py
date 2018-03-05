#Вводятся целые числа a и b. Гарантируется, что a не превосходит b
a,b = [int(input())for i in range(2)]

c = a+a%2
for i in range(c,b +1,2):
    print (i)
