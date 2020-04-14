import matplotlib.pyplot as plt
import numpy as np
import math

def sigmoidal(x):
    return 1 /(1+(math.e**-x))

x = np.linspace(-6, 6, 300)

plt.plot(x,sigmoidal(x),color='red')

plt.title('Función Sigmoidal')
plt.grid()
plt.show()