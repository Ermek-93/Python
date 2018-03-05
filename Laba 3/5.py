import numpy as np
import matplotlib.pyplot as plt
import math
x = np.linspace(-5,5,100)
y =[]
#y = np.linspace(-5,5,100)
for i in range(len(x)):
    y.append(abs(x[i]))
fig, ax = plt.subplots()
ax.plot(x,y,color="blue")
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.show()
