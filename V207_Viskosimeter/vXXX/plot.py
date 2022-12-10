import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unumpy
#plt.rc('text', usetex=True)
#plt.rc('text.latex', preamble=r'\usepackage{siunitx}')


T, t= np.genfromtxt('./content/fallzeitSteigendeTemperatur.txt', unpack = True)
T = T + 273.15
T = 1/T
K = 1.673*(10**-5)
rohK = 2.393
rohFl = 0.998467
#eta = K * (rohK - rohFk) * t

def f(x):
    return K * (rohK - rohFl) * x

eta = f(t)
eta = np.log(eta)
print('viskositaet bei 56 grad:')
print(f(26.53))

params, covariance_matrix = np.polyfit(T, eta, deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')



x_plot = np.linspace(np.min(T), np.max(T))

plt.plot(T, eta, 'k.', label="Messwerte")
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    label='Lineare Regression',
    linewidth=3,
)
plt.legend(loc="best")



plt.plot(T, eta, 'k.')
plt.xlabel(r'$\frac{1}{T}$ in $[K^{-1}]$')
plt.ylabel(r'$ln\left(\frac{\eta}{\unit{Pa \cdot s}}\right)$')
#plt.yscale('log')
plt.show()



#plt.plot(T, , 'k.')
#plt.yscale('log')
#plt.show()
#
# = np.log()

#linregress(T, )


#plt.subplot(1, 2, 1)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
#plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
#plt.legend(loc='best')

#x, y = np.genfromtxt('content/fallzeitSteigendeTemperatur.txt', unpack=True)
#
#plt.plot(x, y, 'k.', label="Daten")

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
