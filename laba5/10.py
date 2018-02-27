import numpy as np
a = np.random.random(10)
a[a.argmax()] = 0
print(a)
