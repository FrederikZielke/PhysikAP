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

x2, D2 = np.genfromtxt('content/rund_einseitig.csv', unpack=True, delimiter=',')
x2 = x2/100
a2 = g(x2, L)
#D2 *= 10**(-6)

x_plot = np.linspace(np.min(a), np.max(a), 1000)

params, covariance_matrix = np.polyfit(a, D, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print('Koeffizienten und Fehler der Ausgleichsgerade des eckigen Stabs:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.9f} ± {error:.9f}')
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

x_plot = np.linspace(np.min(a2), np.max(a2), 1000)

params, covariance_matrix = np.polyfit(a2, D2, deg=1, cov=True)
errors = np.sqrt(np.diag(covariance_matrix))

print('Koeffizienten und Fehler der Ausgleichsgerade des runden Stabs:')
for name, value, error in zip('ab', params, errors):
    print(f'{name} = {value:.9f} ± {error:.9f}')
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
#plt.show()
plt.clf()

#Berechnung Elastiizitätsmodul
g = ufloat(9.81, 0)

m_halter = ufloat(50.1, 0.1)
m_500 = ufloat(499.4, 0.1)
m_1000 = ufloat(1001.9, 0.1)
m_halter, m_500, m_1000 = m_halter/1000, m_500/1000, m_1000/1000

d_e = ufloat(1, 0.005)
l_e = ufloat(60, 0.1)
m_e = ufloat(502.5, 0.1)
d_e /= 100
l_e /= 100
m_e /= 1000

d_r = ufloat(1, 0.005)
l_r = ufloat(59.1, 0.1)
m_r = ufloat(390.1, 0.1)
d_r /= 100
l_r /= 100
m_r /= 1000
r_r = d_r/2

I_e = (1/12)*(d_e**4)
I_r = (1/4)*np.pi*(r_r**4)

print(r'Flächenträgheitsmoment des eckigen Stabs: I_e =', I_e)
print(r'Flächenträgheitsmoment des runden Stabs: I_r =', I_r)

# E = m * g / (2 * a * I)
Ee = (m_500 + m_halter) * g / (2 * m_eckig * I_e)
Er = (m_500 + m_halter) * g / (2 * m_rund * I_r)

print('Ee = ', Ee)
print('Er = ', Er)

#was ist die Stoffdichte?
# ρ = m / V
roh_e = m_e / (d_e**2 * l_e)
roh_r = m_r / (np.pi * (r_r**2) * l_r)

print('roh_e = ', roh_e)# = (8.37+/-0.08)e+03
print('roh_r = ', roh_r)# = (8.40+/-0.09)e+03