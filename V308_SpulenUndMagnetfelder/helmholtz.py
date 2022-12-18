import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unumpy
from scipy.optimize import curve_fit

#Messwerte Helmholtzspule
#Messwerte d = 6cm
B1, x1 = np.genfromtxt('content/helmholtz6.txt', unpack = True)
#Messwerte d = 12cm
B2, x2 = np.genfromtxt('content/helmholtz12.txt', unpack = True)
#Messwerte d = 23.85cm
B3, x3 = np.genfromtxt('content/helmholtz23.txt', unpack = True)
plt.grid()
plt.plot(x1, B1, 'x', color = 'red', label = r'Messdaten d=6 [cm]')

plt.legend(loc="best")
plt.xlabel(r'$x \,$[cm]')
plt.ylabel(r'$B \,$[mT]')

plt.savefig('build/helmholtz6.pdf')
#plt.show()

plt.clf()
plt.grid()
plt.plot(x2, B2, 'x', color = 'blue', label = r'Messdaten d=12 [cm]')
plt.legend(loc="best")
plt.xlabel(r'$x \,$[cm]')
plt.ylabel(r'$B \,$[mT]')

plt.savefig('build/helmholtz12.pdf')
#plt.show()

plt.clf()
plt.grid()
plt.plot(x3, B3, 'x', color = 'green', label = r'Messdaten d=23.85 [cm]')
plt.legend(loc="best")
plt.xlabel(r'$x \,$[cm]')
plt.ylabel(r'$B \,$[mT]')

plt.savefig('build/helmholtz23.pdf')
#plt.show()
