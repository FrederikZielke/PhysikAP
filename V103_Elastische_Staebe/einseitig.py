import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp

x, D = np.genfromtxt('content/eckig_einseitig.csv', unpack=True, delimiter=',')

def g(x, L):
    return L*(x**2) - (x**3)/3

def f(x,a,b):
    return a*x + b

x = x/100
L = 0.535#das könnte stuss sein aber haut ca hin
a = g(x, L)
#D = D*10**(-6)

x_plot = np.linspace(np.min(a), np.max(a), 1000)

params, covariance_matrix = np.polyfit(a, D, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print('Koeffizienten und Fehler der Ausgleichsgerade des eckigen Stabs:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')
m_eckig = ufloat(params[0], errors[0])
b_eckig = ufloat(params[1], errors[1])



plt.plot(x_plot, params[0] * x_plot + params[1], label = 'Ausgleichsgerade')
plt.plot(a, D, 'rx', label = 'Messwerte')
plt.xlabel(r'$L\cdot x^2 - \frac{x^3}{3}\:[\mathrm{m}^3]$')
plt.ylabel(r'$D\:[\mathrm{μm}]$')
plt.title('Eckiger Stab')
plt.grid()
plt.legend(loc = 'best')
plt.savefig('build/eckig_einseitig.pdf')
plt.show()
plt.clf()

x2, D2 = np.genfromtxt('content/rund_einseitig.csv', unpack=True, delimiter=',')
x2 = x2/100
a2 = g(x2, L)

x_plot = np.linspace(np.min(a2), np.max(a2), 1000)

params, covariance_matrix = np.polyfit(a2, D2, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print('Koeffizienten und Fehler der Ausgleichsgerade des runden Stabs:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.3f} ± {error:.3f}')
m_rund = ufloat(params[0], errors[0])
b_rund = ufloat(params[1], errors[1])

plt.plot(x_plot, params[0] * x_plot + params[1], label = 'Ausgleichsgerade')
plt.plot(a2, D2, 'rx', label = 'Messwerte')
plt.xlabel(r'$L\cdot x^2 - \frac{x^3}{3}\:[\mathrm{m}^3]$')
plt.ylabel(r'$D\:[\mathrm{μm}]$')
plt.title('Runder Stab')
plt.grid()
plt.legend(loc = 'best')
plt.savefig('build/rund_einseitig.pdf')
plt.show()
plt.clf()

#Berechnung Elastiizitätsmodul
