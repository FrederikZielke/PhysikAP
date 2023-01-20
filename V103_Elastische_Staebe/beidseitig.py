import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp

x, D = np.genfromtxt('content/eckig_beidseitig.csv', unpack=True, delimiter=',')
x2, D2 = np.genfromtxt('content/rund_beidseitig.csv', unpack=True, delimiter=',')

plt.plot(x, D, 'rx', label = 'Messwerte Eckig')
plt.plot(x2, D2, 'bx', label = 'Messwerte Rund')
plt.show()