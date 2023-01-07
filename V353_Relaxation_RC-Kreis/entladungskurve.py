import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def f(x,a,b):
    return a*x + b

t, U_C = np.genfromtxt('content/zeitkonstanteMesswerte.txt', unpack=True)


U0 = 4 #Spannung bei t=0

tRange = np.linspace(np.min(t),np.max(t),1000)
params, pcov = curve_fit(f, t, np.log(U_C/U0))
a = params[0]
RC = -1/a
print(RC)
plt.plot(tRange,f(tRange,*params),'k-', label='Ausgleichsgerade')
plt.plot(t,np.log(U_C/U0),'rx', label='Gemessen')
plt.plot(12, -4, color="red", marker = "x")
plt.xlim(0, 12.5)
plt.xlabel(r'$t\,$[ms]')
plt.ylabel(r'ln$\;(\frac{U_C}{U_0})\,$[V]')
plt.legend()
#plt.show()
plt.savefig('build/entladekurve.pdf')
