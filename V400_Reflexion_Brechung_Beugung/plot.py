import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

x = np.genfromtxt('content/.csv', delimiter = ',', unpack = True)

#Fit
def f(x):
    return x
t = np.linspace(0, 100, 100)
data, covariance_matrix = curve_fit(f, )
uncertainties = np.sqrt(np.diag(covariance_matrix))
plt.plot(t, f(t, *data), linewidth = 1.5, label = '', linestyle = '--', color = '#0096FF')

plt.plot(t, x, 'r.', mfc = 'red', mec = 'black', mew = 0.5, label = 'Messdaten')
plt.xlabel(r'$t\,/$s')
plt.ylabel(r'$ln(N-N_0)$')

plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('plots/.pdf')
#plt.show()
#plt.clf()