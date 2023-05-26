import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unumpy
from scipy.optimize import curve_fit

#Fkt für U_out
def f(p, a, b, c, d):
    return (a*np.sin(np.radians(b*p+c))+d)
#Messdaten 1 ohne Noise
phi1, U_out = np.genfromtxt('content/MesswertePhase.txt', unpack = True)
data1, covariance_matrix1 = curve_fit(f , phi1, U_out, p0=(5, 1, 0, 0))


uncertainties1 = np.sqrt(np.diag(covariance_matrix1))
x = np.linspace(0, 360, 1000)
plt.plot(x, f(x, *data1), 'k-', linewidth = 1.5)
plt.plot(phi1, U_out, 'x', color = 'red', label = r'Messdaten')

plt.legend(loc="best")
plt.xlabel(r'$\phi \,$[°]')
plt.ylabel(r'$U \,[V]$')

plt.savefig('build/U_out.pdf')
#plt.show()

plt.clf()

#Messdaten 2 mit Noise
phi2, U_outnoise = np.genfromtxt('content/MesswertePhaseNoise.txt', unpack = True)
data2, covariance_matrix2 = curve_fit(f , phi2, U_outnoise, p0=(5, 1, 0, 0))


uncertainties2 = np.sqrt(np.diag(covariance_matrix2))
x = np.linspace(0, 360, 1000)
plt.plot(x, f(x, *data2), 'k-', label = r'Curve-Fit')
plt.plot(phi2, U_outnoise, 'rx', label = r'Messdaten')

plt.legend(loc="best")
plt.xlabel(r'$\phi \,$[°]')
plt.ylabel(r'$U \,[V]$')

plt.savefig('build/U_outnoise.pdf')
plt.show()

print("U ohne Noise")
print(*data1)
print(*uncertainties1)
print("U mit Noise")
print(*data2)
print(*uncertainties2)




