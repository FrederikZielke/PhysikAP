import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp


U_C, f, a = np.genfromtxt('content/MesswerteFrequenz.txt', unpack=True)

L = ufloat(16.87, 0.05) * 0.001
R1 = ufloat(67.2, 0.1)
R2 = ufloat(682, 0.5)
C = ufloat(2.060, 0.003) * 10**(-9)
U0 = 1.5
U_max = 18.3
R = 13
wplus = 29.215
wminus = 22.01
U_krit = 1/np.sqrt(2)*U_max/U0
w_0 = unp.sqrt(1/(L*C))
q = 1/(w_0*R2*C)
b = R/L
T_ex = 2*L/R1

def g(x, a, b):
    return 1

w_res = unp.sqrt(1/(L*C) - (R2**2)/(2*L**2)) * 0.001 / (2*np.pi)
print("Resonanzfrequenz Theorie: ", w_res)
print("Resonanzfrequenz Exp: ", 25.80)
print("kritischer Wert: ", 1/np.sqrt(2)*U_max/U0)
print("Resonanzüberhöhung: ", U_max/U0 - U_krit)
print("Resonanzüberhöhung Theorie: ", q)
print("Breite: ", wplus - wminus)
print("junge fuck man: ", T_ex)

f1 = R2/(2*L) + unp.sqrt(R2**2/(4*L**2) + 1/(L*C)) 
f2 = -R2/(2*L) + unp.sqrt(R2**2/(4*L**2) + 1/(L*C)) 
f1 = f1/(2*np.pi) * 0.001
f2 = f2/(2*np.pi) * 0.001
print("f1: ", f1)
print("f2: ", f2)
print("Breite Theorie: ", f1-f2)
#t = np.linspace(np.min(f),np.max(f),1000)
#params, pcov = curve_fit(g, f, U_C/U0, p0=(10, 0))
#uncertainties = unp.sqrt(np.diag(pcov))
#print(params)
#print(uncertainties)

#plt.plot(t,g(t,*params),'k-', label='Ausgleichskurve')
plt.axhline(y= 1/np.sqrt(2)*U_max/U0, color='r', linestyle='--', label = r'$\frac{1}{\sqrt{2}}\frac{U_C}{U_0}$')
plt.axvline(x= 22.01, color='black', linestyle='--')
plt.axvline(x= 29.215, color='black', linestyle='--')
plt.plot(f, U_C/U0, 'bx', label = 'Messwerte')
plt.xlabel(r'$f\,$[Hz]')
plt.ylabel(r'$\frac{U_C}{U_0}\,$')
plt.legend()
#plt.xlim(f[0]-0.1, f[-1]+1)
plt.xscale('log')

#plt.show()
plt.savefig('build/5c.pdf')
