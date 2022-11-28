import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unumpy

def linregress(x, y):
    assert len(x) == len(y)

    x, y = np.array(x), np.array(y)

    N = len(y)
    Delta = N * np.sum(x ** 2) - (np.sum(x)) ** 2

    A = (N * np.sum(x * y) - np.sum(x) * np.sum(y)) / Delta
    B = (np.sum(x ** 2) * np.sum(y) - np.sum(x) * np.sum(x * y)) / Delta

    sigma_y = np.sqrt(np.sum((y - A * x - B) ** 2) / (N - 2))

    A_error = sigma_y * np.sqrt(N / Delta)
    B_error = sigma_y * np.sqrt(np.sum(x ** 2) / Delta)

    return A, A_error, B, B_error


m = ufloat(4.4531, 0)
r = ufloat(15.59, 0.01)
rho = (4 * m)/(3 * np.pi * r ** 3)
print(rho)

eta, T, T2= np.genfromtxt('./content/fallzeitSteigendeTemperatur.txt', unpack = True)
T = 1/T
T2 = 1/T2
plt.plot(T, eta, 'k.')
plt.plot(T2, eta, 'k.')
plt.yscale('log')
plt.show()

eta = np.log(eta)

linregress(T, eta)
#plt.subplot(1, 2, 1)
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \mathbin{/} \unit{\ohm}$')
#plt.ylabel(r'$y \mathbin{/} \unit{\micro\joule}$')
#plt.legend(loc='best')

x, y = np.genfromtxt('content/fallzeitSteigendeTemperatur.txt', unpack=True)

plt.plot(x, y, 'k.', label="Daten")

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')
