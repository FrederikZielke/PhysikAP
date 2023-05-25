import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy.stats import linregress

U, I, N = np.genfromtxt('content/messung1.csv', unpack = True, delimiter = ',')

N_err = unp.sqrt(N)

plt.errorbar(x = U, y = N, yerr = N_err, fmt = 'x', ecolor='red', color = 'blue', markersize = 5, elinewidth = 1, label = 'Messwerte mit Fehler')

lin = linregress(U[3:-3], N[3:-3])
a1 = ufloat(lin.slope, lin.stderr)
b1 = ufloat(lin.intercept, lin.intercept_stderr)
a = lin.slope
b = lin.intercept

x = np.linspace(300, 750, 1000)
plt.plot(x, (a*x+b), color = 'black', label = 'Ausgleichsgerade')
plt.legend(loc='best')
plt.xlabel(r'$U\,$[V]')
plt.ylabel(r'$N\,$/$\,\frac{Imp}{60s}$')
plt.savefig('build/kennlinie.pdf')
#plt.show()
#print(a1, b1)
#Bestimmung der Totzeit

N_1 = ufloat(93859, np.sqrt(93859))
N_2 = ufloat(147003, np.sqrt(147003))
N_12 = ufloat(223808, np.sqrt(223808))
N_1 = N_1/120
N_2 = N_2/120
N_12 = N_12/120

T = (N_1 + N_2 - N_12)/((N_12)**2 - (N_1)**2 - (N_2)**2)

print(N_1, N_2, N_12, T)


