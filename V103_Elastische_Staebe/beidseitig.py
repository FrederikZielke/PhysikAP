import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp

x, D = np.genfromtxt('content/eckig_beidseitig.csv', unpack=True, delimiter=',')
x2, D2 = np.genfromtxt('content/rund_beidseitig.csv', unpack=True, delimiter=',')
L = 0.535#das könnte stuss sein aber haut ca hin
x = x/100
x2 = x2/100
a = x
b = x2


def g(x, L):
    return 3*(L**2)*x - 4*(x**3)

def f(x, L):
    return 4*(x**3) - 12*L*(x**2) + 9*(L**2)*x - L**3

for i in range(0, 11):
    a[i] = g(x[i], L)

for i in range(11, len(x)):
    a[i] = f(x[i], L)

for i in range(1, 13):
    b[i] = g(x2[i], L)

for i in range(13, len(x2)):
    b[i] = f(x2[i], L)

x_plot = np.linspace(np.min(a), np.max(a), 1000)

params, covariance_matrix = np.polyfit(a, D, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print('Koeffizienten und Fehler der Ausgleichsgerade des eckigen Stabs:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')
m_eckig = ufloat(params[0], errors[0])
b_eckig = ufloat(params[1], errors[1])

plt.plot(x_plot, params[0] * x_plot + params[1], label = 'Ausgleichsgerade')
plt.plot(a, D, 'rx', label = 'Messwerte Eckig')
plt.show()

plt.clf()

x2_plot = np.linspace(np.min(b), np.max(b), 1000)

plt.plot(b, D2, 'bx', label = 'Messwerte Rund')
plt.show()