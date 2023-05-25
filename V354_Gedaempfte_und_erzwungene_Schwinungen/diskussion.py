import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp

U_C, f, a, b = np.genfromtxt('content/FrequenzMitb.txt', unpack=True)

phi = a/b * np.pi

plt.plot(f, phi, "bx", label = r'$\frac{Messwerte}{2}$')
theta = np.arange(0 , 2 * np.pi+np.pi/2, step=(np.pi / 2))
plt.yticks(theta, ['0', 'π/2', 'π', '3π/2', '2π'])
plt.xlim(10-0.5, 30+0.5)
plt.axvline(x = 25.80, color='r', linestyle='--', label = r'Resonanzfrequenz')
plt.axvline(x = 22.01, color='black', linestyle='--', label = r'f1')
plt.axvline(x = 29.215 , color='black', linestyle='--', label = r'f2')
plt.ylim(0, np.pi)
plt.xlabel(r'$f\,$[Hz]')
plt.ylabel(r'$\frac{\phi}{2}$')
plt.legend()
#plt.xscale('log')
plt.savefig('build/diskussion.pdf')
#plt.show()