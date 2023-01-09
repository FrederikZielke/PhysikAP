import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def f(x, a):
    return -np.arctan(-2*np.pi*x*a)

v, U_C, a, b = np.genfromtxt('content/phasenMesswerte.txt', unpack=True)
U0 = 2.9

phi = 2*np.pi*(a/b)
tRange = np.linspace(np.min(v),np.max(v),1000)
params, pcov = curve_fit(f, v, phi, p0 = 2)

uncertainties = np.sqrt(np.diag(pcov))
print(params)
print(uncertainties)
plt.plot(tRange,f(tRange,*params),'k-', label='Ausgleichskurve')
plt.plot(v, phi,'rx', label='Gemessen')
plt.xscale('log')

plt.xlabel(r'$f\,$[Hz]')
plt.ylabel(r'$\phi\,$[rad]')
plt.legend()
#plt.show()
plt.savefig('build/phasen.pdf')