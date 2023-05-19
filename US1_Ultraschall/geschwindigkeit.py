import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp
from uncertainties import ufloat
from scipy.stats import linregress

# Daten einlesen
n, t = np.genfromtxt('content/LaufzeitMessung.csv', delimiter=',', unpack=True)
ax, bx, d = np.genfromtxt('content/SchieblehreMessung.csv', delimiter=',', unpack=True)

# Daten umrechnen
ax *= 1e-3
bx *= 1e-3
d *= 1e-3

# t from microseconds to seconds
t *= 1e-6

bx[9] = bx[10]


# t gegen bx plotten
plt.plot( t, bx[2:10], 'kx', label='Messwerte')
plt.xlabel(r'$t \:/\: $[s]')
plt.ylabel(r'$x \:/\: $[m]')


# lineare Regression
params, covariance_matrix = np.polyfit(t, bx[2:10], deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

# Werte ausgeben
print('Steigung: ', params[0], '±', errors[0])
print('y-Achsenabschnitt: ', params[1], '±', errors[1])

# Regression plotten
x_plot = np.linspace(0, max(t))
plt.plot(x_plot, params[0] * x_plot + params[1], 'r-', label='Lineare Regression')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/AcrylGeschwindigkeit.pdf')
#plt.show()