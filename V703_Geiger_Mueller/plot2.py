import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
from uncertainties import unumpy as unp
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

U, I, N = np.genfromtxt('content/messung2.csv', unpack = True, delimiter = ',')

#Bestimmung der Ladungsträger
e = 1.602*10**(-19)
I = I*10**(-6)

N_u = unp.uarray(N, np.sqrt(N))

Z = I/(e*N_u)
plt.errorbar(yerr=stds(Z/10**10), x = noms(I*10**(6)), y = noms(Z/10**11), label='Messdaten mit Fehler', fmt = "x", ecolor = 'red', markersize = 5, color = 'blue')
plt.legend(loc = 2)
plt.xlabel(r'$I\,$[A]')
plt.ylabel(r'$Z\,$/$\,10^{11}$')
#plt.show()
plt.savefig('build/strom.pdf')