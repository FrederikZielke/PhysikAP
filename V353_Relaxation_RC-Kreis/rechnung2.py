import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def f(x,a):
    return 1/(np.sqrt(1+(2*np.pi*x*a)**2))

v, U_C, a, b = np.genfromtxt('content/phasenMesswerte.txt', unpack=True)
U0 = 2.9
tRange = np.linspace(np.min(v),np.max(v),1000)
params, pcov = curve_fit(f, v, U_C/U0, p0 = 2)

print(params)

plt.plot(tRange,f(tRange,*params),'k-', label='Ausgleichskurve')
plt.plot(v, U_C/U0,'rx', label='Gemessen')
plt.xscale('log')

plt.xlabel(r'$f\,$[Hz]')
plt.ylabel(r'$(\frac{U_C}{U_0})\,$[V]')
plt.legend()
#plt.show()
plt.savefig('build/spannungsplot.pdf')