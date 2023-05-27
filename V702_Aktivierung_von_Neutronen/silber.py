import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat

#erste messreihe log
n = np.genfromtxt('content/silber1.csv', delimiter = ',', unpack = True)
n_0 = 1/5 #pro sekunde
n_0 = n_0 * 10
n = n - n_0
n = np.log(n)
n_err = np.sqrt(n)
t = np.linspace(10, 430, 43)
def f(x, a, b):
    return a*x + b

data1, covariance_matrix1 = curve_fit(f, t[:21], n[:21])
uncertainties1 = np.sqrt(np.diag(covariance_matrix1))
plt.plot(t[:21], f(t[:21], *data1), linewidth = 1.5, label = 'Kurzlebiger Zerfall', linestyle = '--', color = '#0096FF')

data2, covariance_matrix2 = curve_fit(f, t[10:], n[10:])
uncertainties2 = np.sqrt(np.diag(covariance_matrix2))
#print("erste",data1, uncertainties1)
#print("zweite",data2, uncertainties2)
plt.plot(t[12:], f(t[12:], *data2), linewidth = 1.5, label = 'Langlebiger Zerfall', linestyle = '--', color = '#0047AB')
#plt.errorbar(x = t, y = n, yerr = n_err, fmt = 'b.', mfc = 'red', mec = 'black', mew = 0.5, ecolor = '#ff726f', label = 'Messdaten mit Fehler')

plt.plot(t, n, 'r.', mfc = 'red', mec = 'black', mew = 0.5, label = 'Messdaten')
plt.xlabel(r'$t\,/$s')
plt.ylabel(r'$ln(N-N_0)$')
a_neu = data1[0] + data2[0]
a_neu2 = ufloat((data1[0] + data2[0]), (uncertainties1[0] + uncertainties2[0]))
T_kurz = np.log(2) / a_neu2
T_lang = np.log(2) / ufloat(data2[0], uncertainties2[0])
print(T_kurz, T_lang)

plt.plot(t[:15], t[:15]*a_neu + data1[1], linewidth = 1.5, label = 'korrigierter kurzlebiger Zerfall', linestyle = '-', color = '#0096FF')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('plots/messung1_silber.pdf')
#plt.show()
#plt.clf()


#zweite messreihe log
n = np.genfromtxt('content/silber2.csv', delimiter = ',', unpack = True)
n = n - n_0
n = np.log(n)
n_err = np.sqrt(n)
t = np.linspace(10, 430, 43)
def f(x, a, b):
    return a*x + b

data1, covariance_matrix1 = curve_fit(f, t[:21], n[:21])
uncertainties1 = np.sqrt(np.diag(covariance_matrix1))
plt.plot(t[:21], f(t[:21], *data1), linewidth = 1.5, label = 'Kurzlebiger Zerfall', linestyle = '--', color = '#0096FF')

data2, covariance_matrix2 = curve_fit(f, t[10:], n[10:])
uncertainties2 = np.sqrt(np.diag(covariance_matrix2))
plt.plot(t[12:], f(t[12:], *data2), linewidth = 1.5, label = 'Langlebiger Zerfall', linestyle = '--', color = '#0047AB')
#
#print("erste",data1, uncertainties1)
#
#print("zweite",data2, uncertainties2)
plt.plot(t, n, 'r.', mfc = 'red', mec = 'black', mew = 0.5, label = 'Messdaten')
plt.xlabel(r'$t\,/$s')
plt.ylabel(r'$ln(N-N_0)$')
a_neu = data1[0] + data2[0]
a_neu2 = ufloat((data1[0] + data2[0]), (uncertainties1[0] + uncertainties2[0]))
T_kurz = np.log(2) / a_neu2
T_lang = np.log(2) / ufloat(data2[0], uncertainties2[0])
print(T_kurz, T_lang)
plt.plot(t[:15], t[:15]*a_neu + data1[1], linewidth = 1.5, label = 'korrigierter kurzlebiger Zerfall', linestyle = '-', color = '#0096FF')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('plots/messung2_silber.pdf')
#plt.show()
#plt.clf()

#erste messreihe exp fit
def g(x, a, b, c, d):
    return (a*np.exp(-b*(x+c)) + d)
n = np.genfromtxt('content/silber1.csv', delimiter = ',', unpack = True)
n_err = np.sqrt(n)
t = np.linspace(10, 430, 43)

data1exp, covariance_matrix1exp = curve_fit(g, t, n, p0 = [0.06, 0.045, -190, 9])
uncertainties1exp = np.sqrt(np.diag(covariance_matrix1exp))
plt.plot(t, g(t, *data1exp), 'k-', linewidth = 1.5, label = 'Fit Zerfallskurve')
#print(data1exp, uncertainties1exp)
#plt.plot(t, n, 'bx')
plt.errorbar(x = t, y = n, yerr = n_err, fmt = 'b.', mfc = 'red', mec = 'black', mew = 0.5, ecolor = '#ff726f', label = 'Messdaten mit Fehler')
plt.xlabel(r'$t\,/$s')
plt.ylabel(r'$N$')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('plots/messung1_silber_expfit.pdf')
#plt.show()
#plt.clf()

#zweite messreihe exp fit
def g(x, a, b, c, d):
    return (a*np.exp(-b*(x+c)) + d)
n = np.genfromtxt('content/silber2.csv', delimiter = ',', unpack = True)
n_err = np.sqrt(n)
t = np.linspace(10, 430, 43)

data1exp, covariance_matrix1exp = curve_fit(g, t, n, p0 = [0.06, 0.045, -190, 9])
uncertainties1exp = np.sqrt(np.diag(covariance_matrix1exp))
plt.plot(t, g(t, *data1exp), 'k-', linewidth = 1.5, label = 'Fit Zerfallskurve')
#print(data1exp, uncertainties1exp)
plt.errorbar(x = t, y = n, yerr = n_err, fmt = 'b.', mfc = 'red', mec = 'black', mew = 0.5, ecolor = '#ff726f', label = 'Messdaten mit Fehler')
plt.xlabel(r'$t\,/$s')
plt.ylabel(r'$N$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('plots/messung2_silber_expfit.pdf')
#plt.show()
#plt.clf()


