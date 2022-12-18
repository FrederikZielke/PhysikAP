import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from uncertainties import ufloat
import uncertainties.unumpy as unumpy
from scipy.optimize import curve_fit
#Radius Ringspule
r = 0.135
#Messwerte Neukurve
B1, I1 = np.genfromtxt('content/hysterese1.txt', unpack = True)
#Messwerte absteigende Hysteresekurve
B2, I2 = np.genfromtxt('content/hysterese2.txt', unpack = True)
#Messwerte aufsteigende Hysteresekurve
B3, I3 = np.genfromtxt('content/hysterese3.txt', unpack = True)
#modifizierte Messwerte
#Messwerte Neukurve
B1m, I1m = np.genfromtxt('content/hysterese1.txt', unpack = True)
#Messwerte absteigende Hysteresekurve
B2m, I2m = np.genfromtxt('content/hysterese2m.txt', unpack = True)
#Messwerte aufsteigende Hysteresekurve
B3m, I3m = np.genfromtxt('content/hysterese3m.txt', unpack = True)

I1 = I1 * 595/(2*np.pi*r)
I2 = I2 * 595/(2*np.pi*r)
I3 = I3 * 595/(2*np.pi*r)
I1m = I1m * 595/(2*np.pi*r)
I2m = I2m * 595/(2*np.pi*r)
I3m = I3m * 595/(2*np.pi*r)

poly = np.polyfit(I1m, B1m, 5)
plt.plot(I1, B1, 'x', color = 'black', label = r'Messdaten', markersize = 3)
polyfit = np.poly1d(poly)
plt.plot(I1m, polyfit(I1m), color = 'red', linewidth = 0.75, label = r'Neukurve')

poly2 = np.polyfit(I2m, B2m, 30)
plt.plot(I2, B2, 'x', color = 'black', markersize = 3)
polyfit2 = np.poly1d(poly2)
plt.plot(I2m, polyfit2(I2m), color = 'blue', linewidth = 0.75, label = r'absteigende Hysteresekurve')

poly3 = np.polyfit(I3m, B3m, 30)
plt.plot(I3, B3, 'x', color = 'black', markersize = 3)
polyfit3 = np.poly1d(poly3)
plt.plot(I3m, polyfit3(I3m), color = 'green', linewidth = 0.75, label = r'aufsteigende Hysteresekurve')
def g(x, a, b, c, d, e, f):
    return a*x**5+b*x**4+c*x**3+d*x**2+e*x+f
def f(x, a, b, c, d, e):
    return 1/(4*np.pi*10**(-7))*(a*x**4 + b*x**3 + c*x**2 + d*x + e)*10**(-3)

print(f(3800, polyfit[5], polyfit[4], polyfit[3], polyfit[2], polyfit[1]))
#print(g(2.5, -0.06298, 1.652, -14.62, 40.27, 109, 4.428))

plt.grid()
plt.ylim(-800, 800)
plt.annotate(r'Sättigungsmagnetisierung', 
        xy = (7070, 725),
        xycoords='data',
        xytext=(-80, +20),
        textcoords='offset points', 
        fontsize=10,
        arrowprops=dict(facecolor='black',arrowstyle="->")
)
plt.annotate(r'Remanenz', 
        xy = (0, 139),
        xycoords='data',
        xytext=(-50, +20),
        textcoords='offset points', 
        fontsize=10,
        arrowprops=dict(facecolor='black',arrowstyle="->")
)
plt.annotate(r'Koerzitivfeldstärke', 
        xy = (-350, 0),
        xytext=(-120, +5),
        textcoords='offset points', 
        fontsize=10,
        arrowprops=dict(facecolor='black',arrowstyle="->")
)

plt.legend(loc="best")
plt.xlabel(r'$H \,$[A/m]')
plt.ylabel(r'$B \,$[mT]')

plt.savefig('build/hysterese.pdf')
#plt.show()