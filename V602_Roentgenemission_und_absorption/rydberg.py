import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

E = np.array([8978.82, 13480.57, 17727.23, 16060.79])
Z = np.array([30, 35, 40, 38])

def f(x, a, b):
    return a*x + b

params, pcov = curve_fit(f, Z, np.sqrt(E))
uncertainties = np.sqrt(np.diag(pcov))
x = np.linspace(np.min(Z), np.max(Z), 100)
plt.plot(Z, np.sqrt(E), "bx", label="Absorptionsenergie")
plt.plot(x,f(x,*params),'k-', label='Ausgleichsgerade')
plt.ylabel(r'$\sqrt{E\,[eV]}$')
plt.xlabel(r'$Z$')
plt.legend()
#plt.show()
#plt.savefig('build/rydberg.pdf')
print(params[0], params[1])
print(uncertainties[0], uncertainties[1])