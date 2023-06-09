import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy
import math

t_0, t_auf1, t_auf2, t_auf3, t_ab1, t_ab2, t_ab3, R = np.genfromtxt('content/messreihe1.csv', delimiter = ',', unpack = True)

s = ufloat(0.5, 0.1)*10**(-3)
t_auf = np.array([t_auf1, t_auf2, t_auf3])
t_ab = np.array([t_ab1, t_ab2, t_ab3])
t_auf_err = np.std(t_auf, ddof = 1, axis = 0)/np.sqrt(np.size(t_auf))
t_ab_err = np.std(t_ab, ddof = 1, axis = 0)/np.sqrt(np.size(t_ab))
t_auf = np.mean(t_auf, axis = 0)
t_ab = np.mean(t_ab, axis = 0)


t_auf = unumpy.uarray(t_auf, t_auf_err)
t_ab = unumpy.uarray(t_ab, t_ab_err)
print("t_auf", t_auf)
print("t_ab", t_ab)
print("t_0", t_0)
v_auf = s/t_auf
v_ab = s/t_ab
v_0 = s/t_0
print("v_0", v_0)
print("v_auf", v_auf)
print("v_ab", v_ab)
#bedingung 2v_0 = v_ab - v_auf
verhaeltnis = (2*v_0)/(v_ab - v_auf)
print("verhaeltnis", verhaeltnis)

#mask werte zwischen 0.5 und 1.5
mask = (verhaeltnis > 0.5) & (verhaeltnis < 1.5)
print("mask", mask)
verhaeltnis = verhaeltnis[mask]
print("verhaeltnis", verhaeltnis)
v_auf = v_auf[mask]
print("v_auf", v_auf)
v_ab = v_ab[mask]
print("v_ab", v_ab)
print("R", R[mask])
#radius und ladung des tröpchens
rho_o = 886
rho_l = 1.2041
g = 9.81
p = 101325
B = 6.17*10**(-3)*10**(-2)*133.322
d = ufloat(7.6250, 0.0051)*10**(-3)
U = np.array([247.8, 247.8, 247.8, 247.8, 297.4, 297.4, 297.4, 297.4, 297.4, 297.4, 297.4, 297.4])
eta = np.array([1.85, 1.85, 1.85, 1.85, 1.85, 1.86, 1.86, 1.86, 1.86, 1.86, 1.86, 1.86])
E = U/d
eta = unumpy.uarray(eta, 0.05)*10**(-5)

r = unumpy.sqrt((9*eta*(v_ab-v_auf))/(2*g*(rho_o-rho_l)))
print("Radius: ",r)
q = 3*np.pi*eta*unumpy.sqrt((9*eta*(v_ab-v_auf))/(4*g*(rho_o-rho_l)))*(v_ab+v_auf)/E
q = q * (1+(B/(p*r)))**(-1)
print("Ladung: ",q)

eta = eta*(1/(1+B/(r*p)))
print("korrigierte Viskosität: ", eta)

N = np.linspace(1, np.size(q), np.size(q))
plt.errorbar(N, unumpy.nominal_values(q), yerr = unumpy.std_devs(q), fmt = 'b.', mfc = 'red', mec = 'black', mew = 0.5, ecolor = '#ff726f', label = r'$\mathrm{Ladung}$')
plt.xlabel(r'$\mathrm{Messung}$')
plt.ylabel(r'$\mathrm{Ladung}\,q\,/\,\mathrm{C}$')
plt.yticks(np.arange(0, 10*10**(-19), 1.602*10**(-19)))
def float_gcd(a, b, rtol = 1e-10, atol = 0.2*1e-19):
    t = min(abs(a), abs(b))
    while abs(b) > rtol * t + atol:
        a, b = b, a % b
    return a

#iterate through q and use float_gcd to find e_0
e_0 = np.zeros((np.size(q)-1, np.size(q)-1))
e_0_err = np.zeros((np.size(q)-1, np.size(q)-1))
for i in range(0, np.size(q)-1):
    for j in range(0, np.size(q)-1):
        e_0[i][j] = float_gcd(unumpy.nominal_values(q[i]), unumpy.nominal_values(q[j]))
        e_0_err[i][j] = float_gcd(unumpy.std_devs(q[i]), unumpy.std_devs(q[j]))
e_0 = e_0 * 10**(19)
e_0_err = e_0_err * 10**(19)
e_0 = round(np.mean(e_0), 4)
e_0_err = round(np.mean(e_0_err), 4)
e_0 = ufloat(np.mean(e_0), np.mean(e_0_err))*10**(-19)
print("e_0", e_0)
#compute avogadro constant with e_0 and faraday constant
N_A = 1/e_0 * 9.64853321233100184e+04
print("N_A", N_A)
#plt.legend(loc = 'best')
#plt.grid()
#plt.tight_layout()
#plt.savefig('build/plot1.pdf')
#plt.show()