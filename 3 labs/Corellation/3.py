import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

# 1000 random integers between 0 and 50
x = np.random.randint(0, 50, 1000)
# No correlation
x = np.random.randint(0, 50, 1000)
y = np.random.randint(0, 50, 1000)
np.corrcoef(x, y)

plt.scatter(x, y)
plt.show()
