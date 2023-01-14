import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp

U_C, f, a, b = np.genfromtxt('content/FrequenzMitb.txt', unpack=True)

phi = a/b * np.pi * 2

plt.plot(f, phi, "bx")
theta = np.arange(0 , 2 * np.pi+np.pi/2, step=(np.pi / 2))
plt.yticks(theta, ['0', 'π/2', 'π', '3π/2', '2π'])
#plt.xscale('log')

#plt.show()
plt.savefig('build/5d.pdf')