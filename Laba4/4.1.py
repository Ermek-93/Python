import random
import matplotlib.pyplot as plot
import matplotlib as lib

coin = []

for i in range(1,1000):
    rand = random.randint(1,100)
    if (rand>=30):
        coin.append(0)
    else:
        coin.append(1)

labels = ['Reshka','Orel']
values = [0]*2

for i in range(len(coin)):
    if(coin[i]==0):
        values[0] += 1
    else:
        values[1] += 1

fig1, ax1 = plot.subplots()
ax1.pie(values,labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  
plot.show()

