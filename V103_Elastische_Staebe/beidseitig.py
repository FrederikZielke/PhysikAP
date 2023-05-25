import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp

xe1, De1 = np.genfromtxt('content/eckig_beidseitig1.csv', unpack=True, delimiter=',')
xe2, De2 = np.genfromtxt('content/eckig_beidseitig2.csv', unpack=True, delimiter=',')
xr1, Dr1 = np.genfromtxt('content/rund_beidseitig1.csv', unpack=True, delimiter=',')
xr2, Dr2 = np.genfromtxt('content/rund_beidseitig2.csv', unpack=True, delimiter=',')
L = 0.535#das könnte stuss sein aber haut ca hin
xe1 = xe1/100
xe2 = xe2/100
xr1 = xr1/100
xr2 = xr2/100
ae1 = xe1
ae2 = xe2
ar1 = xr1
ar2 = xr2

#De1 *= 10**(-6)
#De2 *= 10**(-6)
#Dr1 *= 10**(-6)
#Dr2 *= 10**(-6)


def g(x, L):
    return 3*(L**2)*x - 4*(x**3)

def f(x, L):
    return 4*(x**3) - 12*L*(x**2) + 9*(L**2)*x - L**3

for i in range(0, len(xe1)):
    ae1[i] = g(xe1[i], L)

for i in range(0, len(xe2)):
    ae2[i] = f(xe2[i], L)

for i in range(0, len(xr1)):
    ar1[i] = g(xr1[i], L)

for i in range(0, len(xr2)):
    ar2[i] = f(xr2[i], L)

x_plot_e1 = np.linspace(np.min(ae1), np.max(ae1), 1000)

params_e1, covariance_matrix_e1 = np.polyfit(ae1, De1, deg=1, cov=True)
errors_e1 = np.sqrt(np.diag(covariance_matrix_e1))

print('Koeffizienten und Fehler der Ausgleichsgerade des eckigen Stabs zwischen Einspannung und Gewicht:')
for name, value, error in zip('ab', params_e1, errors_e1):
    print(f'{name} = {value:.9f} ± {error:.9f}')
m_e1 = ufloat(params_e1[0], errors_e1[0])
b_e1 = ufloat(params_e1[1], errors_e1[1])

plt.plot(x_plot_e1, params_e1[0] * x_plot_e1 + params_e1[1], label = 'Ausgleichsgerade')
plt.plot(ae1, De1, 'rx', label = 'Messwerte Eckig')
plt.xlabel(r'$3L^2x - 4x^3 \:[\mathrm{m}^3]$')
plt.ylabel(r'$D\:[\mathrm{μm}]$')
plt.legend(loc="best")
plt.title('Eckiger Stab zwischen Einspannung und Gewicht.')
plt.grid()
#plt.show()

plt.savefig('build/beidseitig_e1.pdf')
plt.clf()

x_plot_e2 = np.linspace(np.min(ae2), np.max(ae2), 1000)

params_e2, covariance_matrix_e2 = np.polyfit(ae2, De2, deg=1, cov=True)
errors_e2 = np.sqrt(np.diag(covariance_matrix_e2))

print('Koeffizienten und Fehler der Ausgleichsgerade des eckigen Stabs zwischen Stabende und Gewicht:')
for name, value, error in zip('ab', params_e2, errors_e2):
    print(f'{name} = {value:.9f} ± {error:.9f}')
m_e2 = ufloat(params_e2[0], errors_e2[0])
b_e2 = ufloat(params_e2[1], errors_e2[1])

plt.plot(x_plot_e2, params_e2[0] * x_plot_e2 + params_e2[1], label = 'Ausgleichsgerade')
plt.plot(ae2, De2, 'rx', label = 'Messwerte Eckig')
plt.xlabel(r'$4x^3 - 12Lx^2 + 9L^2x - L^3 \:[\mathrm{m}^3]$')
plt.ylabel(r'$D\:[\mathrm{μm}]$')
plt.legend(loc="best")
plt.title('Eckiger Stab zwischen Stabende und Gewicht.')
plt.grid()
#plt.show()

plt.savefig('build/beidseitig_e2.pdf')
plt.clf()

x_plot_r1 = np.linspace(np.min(ar1), np.max(ar1), 1000)

params_r1, covariance_matrix_r1 = np.polyfit(ar1, Dr1, deg=1, cov=True)
errors_r1 = np.sqrt(np.diag(covariance_matrix_r1))

print('Koeffizienten und Fehler der Ausgleichsgerade des runden Stabs zwischen Einspannung und Gewicht:')
for name, value, error in zip('ab', params_r1, errors_r1):
    print(f'{name} = {value:.9f} ± {error:.9f}')
m_r1 = ufloat(params_r1[0], errors_r1[0])
b_r1 = ufloat(params_r1[1], errors_r1[1])

plt.plot(x_plot_r1, params_r1[0] * x_plot_r1 + params_r1[1], label = 'Ausgleichsgerade')
plt.plot(ar1, Dr1, 'rx', label = 'Messwerte Rund')
plt.xlabel(r'$3L^2x - 4x^3 \:[\mathrm{m}^3]$')
plt.ylabel(r'$D\:[\mathrm{μm}]$')
plt.legend(loc="best")
plt.title('Runder Stab zwischen Einspannung und Gewicht.')
plt.grid()
#plt.xlim(np.min(x_plot_r1), np.max(x_plot_r1))
#plt.ylim(np.min(params_r1[0] * x_plot_r1 + params_r1[1]), np.max(Dr1))
#plt.show()

plt.savefig('build/beidseitig_r1.pdf')
plt.clf()

x_plot_r2 = np.linspace(np.min(ar2), np.max(ar2), 1000)

params_r2, covariance_matrix_r2 = np.polyfit(ar2, Dr2, deg=1, cov=True)
errors_r2 = np.sqrt(np.diag(covariance_matrix_r2))

print('Koeffizienten und Fehler der Ausgleichsgerade des runden Stabs zwischen Stabende und Gewicht:')
for name, value, error in zip('ab', params_r2, errors_r2):
    print(f'{name} = {value:.9f} ± {error:.9f}')
m_r2 = ufloat(params_r2[0], errors_r2[0])
b_r2 = ufloat(params_r2[1], errors_r2[1])

plt.plot(x_plot_r2, params_r2[0] * x_plot_r2 + params_r2[1], label = 'Ausgleichsgerade')
plt.plot(ar2, Dr2, 'rx', label = 'Messwerte Rund')
plt.xlabel(r'$4x^3 - 12Lx^2 + 9L^2x - L^3 \:[\mathrm{m}^3]$ ')
plt.ylabel(r'$D\:[\mathrm{μm}]$')
plt.legend(loc="best")
plt.title('Runder Stab zwischen Stabende und Gewicht.')
plt.grid()
#plt.show()

plt.savefig('build/beidseitig_r2.pdf')
plt.clf()

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
Ee1 = (m_1000 + m_halter) * g / (48 * m_e1 * I_e)
Ee2 = (m_1000 + m_halter) * g / (48 * m_e2 * I_e)
Er1 = (m_1000 + m_halter) * g / (48 * m_r1 * I_r)
Er2 = (m_1000 + m_halter) * g / (48 * m_r2 * I_r)

print('Ee1 = ', Ee1)
print('Ee2 = ', Ee2)
print('Er1 = ', Er1)
print('Er2 = ', Er2)
print("{0:.9f}".format(m_r2))