import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unumpy

#Messdaten
t, T2, T1, pa, pb, N, = np.genfromtxt('content/messwerte.txt', unpack = True)

#5e
pb = pb + 1
T1 = 1/T1
pb = np.log(pb)
T1[0] = T1[1]
pb[0] = pb[1]

#linreg
params, covariance_matrix = np.polyfit(T1, pb, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')

x_plot = np.linspace(np.min(T1), np.max(T1))

plt.grid()
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=3,
)

plt.plot(T1, pb, 'rx', label='Messdaten')

plt.legend(loc="best")
plt.xlabel(r'$1/T_1 \,$[1/°C]')
plt.ylabel(r'$ln\left(\frac{p_b}{bar}\right)$')

plt.savefig('build/dampfdruck.pdf')
#plt.show()