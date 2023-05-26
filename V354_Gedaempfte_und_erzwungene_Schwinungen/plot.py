import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp

#oszillierende Spannung
def g(x, a, b, c):
    return np.sin(b*x+c)*np.exp(-x*a)*U0

#Einhüllende oben
def g1(x, a, b):
    return a*np.exp(-b*x)

#Einhüllende unten
def g2(x, a, b):
    return a*np.exp(b*x)

U_C1, t1 = np.genfromtxt('content/daempfungswiederstandOben.txt', unpack=True)
U_C2, t2 = np.genfromtxt('content/daempfungswiederstandUnten.txt', unpack=True)
U_C, t = np.genfromtxt('content/daempfungswiderstand.txt', unpack=True)

t = t * 10**(-3)
t1 = t1 * 10**(-3)
t2 = t2 * 10**(-3)

L = ufloat(16.87, 0.05) * 0.001
U0 = 1.5 #keine Ahnung wofür ich das brauche
x = np.linspace(np.min(t),np.max(t),1000)
params, pcov = curve_fit(g, t, U_C, p0 = (0.4, 20, 0.4))
params1, pcov1 = curve_fit(g1, t1, U_C1, p0 = (1,1))
params2, pcov2 = curve_fit(g2, t2, U_C2, p0 = (1,1))
uncertainties1 = np.sqrt(np.diag(pcov1))
uncertainties = np.sqrt(np.diag(pcov))
print("Einhüllende: ", params1)
print("Einhüllende Fehler: ",uncertainties1)
print("Schwingung: ",params)
print("Schwingung Fehler: ",uncertainties)

mu = ufloat(params1[1], uncertainties1[1])
R_eff = L*mu*2
print(R_eff)

T_ex = 1/(2*np.pi*mu)
print(T_ex)

#plt.plot(f, U_C2, 'bx')
plt.plot(x,g(x,*params),'k-', label='Ausgleichskurve')
plt.plot(x,g1(x,*params1),'r--', label='Einhüllende')
plt.plot(x,g2(x,*params2),'r--')
plt.plot(t, U_C, 'bx', label = 'Messwerte')
plt.xlabel(r'$t\,$[s]')
plt.ylabel(r'$U_C\,$[V]')
plt.legend()
plt.xlim(t[0]-0.0001, t[-1]+0.0001)

#plt.show()
plt.savefig('build/abklingverhalten.pdf')