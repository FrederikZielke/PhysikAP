import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def g(x, a, b, c):
    return np.sin(b*x+c)*np.exp(-x*a)*U0

def g1(x, a, b):
    return a*np.exp(b*x)

def g2(x, a, b):
    return a*np.exp(b*x)

U_C1, f1 = np.genfromtxt('content/daempfungswiederstandOben.txt', unpack=True)
U_C2, f2 = np.genfromtxt('content/daempfungswiederstandUnten.txt', unpack=True)
U_C, f = np.genfromtxt('content/daempfungswiderstand.txt', unpack=True)


U0 = 1.5
t = np.linspace(np.min(f),np.max(f),1000)
params, pcov = curve_fit(g, f, U_C, p0 = (0.4, 20, 0.4))
params1, pcov1 = curve_fit(g1, f1, U_C1, p0 = (1,1))
params2, pcov2 = curve_fit(g2, f2, U_C2, p0 = (1,1))
uncertainties = np.sqrt(np.diag(pcov))
#print(params)
#print(uncertainties)


#plt.plot(f, U_C2, 'bx')
plt.plot(t,g(t,*params),'k-', label='Ausgleichskurve')
plt.plot(t,g1(t,*params1),'r--', label='Einhüllende')
plt.plot(t,g2(t,*params2),'r--')
plt.plot(f, U_C, 'bx', label = 'Messwerte')
plt.xlabel(r'$f\,$[Hz]')
plt.ylabel(r'$U_C\,$[V]')
plt.legend()
plt.xlim(f[0]-0.1, f[-1]+1)

plt.show()