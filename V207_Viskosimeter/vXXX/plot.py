import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unumpy


m = ufloat(4.4531, 0)
r = ufloat(15.59, 0.01)
rho = (4 * m)/(3 * np.pi * r ** 3)
print(rho)


plt.rcParams['figure.figsize'] = (10, 8)
plt.rcParams['font.size'] = 16

x, y = np.genfromtxt('content/fallzeitSteigendeTemperatur.txt', unpack=True)

plt.plot(x, y, 'k.', label="Daten")

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
