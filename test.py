import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-100,100,1000)
plt.plot(X, [x**2 for x in X])
plt.show()
