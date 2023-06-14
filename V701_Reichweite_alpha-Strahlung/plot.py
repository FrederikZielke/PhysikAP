import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

p, N, nr = np.genfromtxt('content/messung1.csv', delimiter = ',', unpack = True)

p0 = 1013.25 # mbar
x0 = 5.5e-2 # m
# p in effektive länge umrechnen
x = x0 * p / p0


# create 3 subplots. 3 rows, 1 column. plot (p, N) in the first subplot and (p, nr) in the second subplot an N in a histogram in the third subplot
fig, ax = plt.subplots(2, 1, figsize = (10, 10))
ax[0].plot(x, N, 'kx', label = 'Messwerte')
ax[0].set_xlabel(r'$x \,/\, \mathrm{m}$')
ax[0].set_ylabel(r'$N$')
ax[0].legend(loc = 'best')
ax[0].grid()

ax[1].plot(x, nr, 'kx', label = 'Messwerte')
ax[1].set_xlabel(r'$x \,/\, \mathrm{m}$')
ax[1].set_ylabel(r'$N_\mathrm{R}$')
ax[1].legend(loc = 'best')
ax[1].grid()



fig.tight_layout()
fig.savefig('build/plot1.pdf')

plt.clf()

N = np.genfromtxt('content/statistik.csv', delimiter = ',', unpack = True)

fig, ax = plt.subplots(1, 1, figsize = (10, 10))
ax.hist(N, bins = 10, label = 'Messwerte')
ax.set_xlabel(r'$N$')
ax.set_ylabel(r'$\mathrm{Häufigkeit}$')
ax.legend(loc = 'best')

fig.tight_layout()
fig.savefig('build/hist.pdf')