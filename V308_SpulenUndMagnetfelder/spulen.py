import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unumpy
from scipy.optimize import curve_fit

#Messwerte lange und kurze Spule
#Messwerte lange Spule
x1, B1 = np.genfromtxt('content/MagnetfeldLang.txt', unpack = True)
#Messwerte kurze Spule
x2, B2 = np.genfromtxt('content/MagnetfeldKurz.txt', unpack = True)

plt.grid()
plt.plot(x1, B1, 'x', color = 'red', label = r'Messdaten')
plt.xlabel(r'$x \,$[cm]')
plt.ylabel(r'$B \,$[mT]')
plt.hlines(y=2.2, xmin=-1, xmax=6.5, color='black', linestyle='-', label ='Theorie')
plt.legend(loc="best")
plt.savefig('build/langeSpule.pdf')
plt.show()

plt.clf()
plt.grid()
plt.xlabel(r'$x \,$[cm]')
plt.ylabel(r'$B \,$[mT]')
plt.plot(x2, B2, 'x', color = 'blue', label = r'Messdaten')

plt.savefig('build/kurzeSpule.pdf')
#plt.show()