import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unumpy
from scipy.optimize import curve_fit

#Fkt für U_out
def f(x, a, b, c):
    return (a/x**b + c)
#Messdaten 1 ohne Noise
r, U = np.genfromtxt('content/MesswerteDiode2.txt', unpack = True)
data, covariance_matrix = curve_fit(f , r, U, p0=(1, 2, 0))

uncertainties = np.sqrt(np.diag(covariance_matrix))
x = np.linspace(0, 150, 1000)
plt.ylim(U[-1], U[0]+0.1)
plt.plot(x, f(x, *data), 'k-', linewidth = 1.5)
plt.plot(r, U, 'x', color = '#FF00FF', label = r'Messdaten')

plt.legend(loc="best")
plt.xlabel(r'$r \,[cm]$')
plt.ylabel(r'$U \,[V]$')

plt.savefig('build/diode1.pdf')
#plt.show()

plt.xlim(40, 150)
plt.ylim(0, 0.2)
plt.savefig('build/diode2')
plt.show()