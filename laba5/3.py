import numpy as np
a = np.arange(12)
a[(3 < a) & (a <= 10)] *= -1
print(a)
