import matplotlib.pyplot as plt
import numpy as np

f, U = np.genfromtxt("content/guetekurve.csv", delimiter = ",", unpack = True)

plt.plot(f, U, 'bx')
plt.show()
