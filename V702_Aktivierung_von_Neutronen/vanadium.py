import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

n = np.genfromtxt('content/vanadium.csv', delimiter = ',', unpack = True)
n_0 = 1/5 #pro sekunde
n_0 = n_0 * 30
#n = n - n_0
n_err = np.sqrt(n)
t = np.linspace(30, 30*30, 30)

def g(x, a, b, c, d):
    return (a*np.exp(-b*(x+c)) + d)

data1exp, covariance_matrix1exp = curve_fit(g, t, n, p0 = [0.017, 0.023, -380, 15.8])
uncertainties1exp = np.sqrt(np.diag(covariance_matrix1exp))
#print(data1exp, uncertainties1exp)
plt.plot(t, g(t, *data1exp), 'k-', linewidth = 1.5, label = 'Fit Zerfallskurve')

plt.errorbar(x = t, y = n, yerr = n_err, fmt = 'b.', mfc = 'red', mec = 'black', mew = 0.5, ecolor = '#ff726f', label = 'Messdaten mit Fehler')

plt.xlabel(r'$t\,/$s')
plt.ylabel(r'$N$')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('plots/vanadium_exp.pdf')
#plt.show()
#plt.clf()

n = n - n_0
n_error = np.sqrt(n)
n = np.log(n)
def f(x, a, b):
    return a*x + b

data1, covariance_matrix1 = curve_fit(f, t, n)
uncertainties1 = np.sqrt(np.diag(covariance_matrix1))
#print(data1, uncertainties1)
lam = ufloat(data1[0], uncertainties1[0])
T = np.log(2) / lam
print(T)
plt.plot(t, f(t, *data1), linewidth = 1.5, label = 'Ausgleichsgerade', linestyle = '--', color = '#0096FF')
plt.plot(t, n, 'r.', mfc = 'red', mec = 'black', mew = 0.5, label = 'Messdaten')

plt.xlabel(r'$t\,/$s')
plt.ylabel(r'$ln(N-N_0)$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('plots/vanadium.pdf')
#plt.show()
#plt.clf()