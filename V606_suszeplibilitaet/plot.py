import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp
from scipy import constants as sc

#f, U = np.genfromtxt("content/guetekurve.csv", delimiter = ",", unpack = True)
#U_E = 1
#U_A = U
#def fit1(x):
#    return 1/100*x - 1068/5
#x1 = np.linspace(21600, 21800, 100)
#plt.plot(x1, fit1(x1), color = 'red')
#def fit2(x):
#    return -1/125*x + 359/2
#x2 = np.linspace(21890, 22135, 100)
#plt.plot(x1, fit1(x1), color = 'red', label = "Hilfsgeraden")
#plt.plot(x2, fit2(x2), color = 'red')
#plt.hlines(y = 1/np.sqrt(2)*4.6, xmin = 21850-2000, xmax = 21850+2000, color = 'black', linestyles = 'dotted', label = r"$\frac{1}{\sqrt{2}}U_{max}$")
#plt.plot(f, U_A/U_E, 'bx', label = 'Gütekurve')
#plt.ylabel(r'$\frac{U_A}{U_E}$')
#plt.xlabel(r'$f\,$[Hz]')
#plt.legend(loc = 'best')
#plt.savefig('build/guetekurve.pdf')
#plt.show()

f1 = ufloat(21685, 1)
f2 = ufloat(22031, 1)
f0 = 21850

Q = f0 / (f2-f1)
#print(Q)
F = 86.6 * 10**(-6)
m = [14.38, 18.48, 14.08]
m_err = 0.01
m_r = unp.uarray(m, m_err)
l = [16.3, 14.5, 17.3]
l_err = 0.1
l_r = unp.uarray(l, l_err)/100
rho = np.array([7.8, 7.24, 7.40])*10**(6)
quer = m_r/(l_r*rho)
m_mol = np.array([373.00, 336.48, 362.50])
N = (2 * sc.N_A * rho) / m_mol

S = np.array([2.5, 1.5, 3.5])
L = np.array([5, 6, 0])
J = np.array([7.5, 4.5, 3.5])
g_j = (3*J*(J+1)+(S*(S+1)-L*(L+1)))/(2*J*(J+1))
T = ufloat(293.15, 1)
chi = (N*sc.mu_0 * (sc.physical_constants["Bohr magneton"][0])**2 * (g_j)**2 * J * (J+1))/(3*sc.k*T)
#print(m_mol)
#print(N)
#print(g_j)
#print(chi)
R_dy_ohne = unp.uarray([520, 483, 506],[10, 10, 10]) * 5 * 10**(-3)
R_dy_mit = unp.uarray([195, 182, 195],[10, 10, 10]) * 5 * 10**(-3)
R_nd_ohne = unp.uarray([520, 504, 485],[10, 10, 10]) * 5 * 10**(-3)
R_nd_mit = unp.uarray([464, 470, 475],[10, 10, 10]) * 5 * 10**(-3)
R_gd_ohne = unp.uarray([502, 484, 507],[10, 10, 10]) * 5 * 10**(-3)
R_gd_mit = unp.uarray([348, 349, 345],[10, 10, 10]) * 5 * 10**(-3)

delta_dy = R_dy_ohne - R_dy_mit
delta_nd = R_nd_ohne - R_nd_mit
delta_gd = R_gd_ohne - R_gd_mit

mean_dy = np.mean(delta_dy)
mean_nd = np.mean(delta_nd)
mean_gd = np.mean(delta_gd)
mean_dy_ohne = np.mean(R_dy_ohne)
mean_nd_ohne = np.mean(R_nd_ohne)
mean_gd_ohne = np.mean(R_gd_ohne)

chi_dy = (2 * mean_dy * F)/(998 * quer[0])
chi_nd = (2 * mean_nd * F)/(998 * quer[1])
chi_gd = (2 * mean_gd * F)/(998 * quer[2])

#print(R_dy_ohne)
#print(R_dy_mit)
#print(delta_dy)
#print("-------------------")
#print(R_nd_ohne)
#print(R_nd_mit)
#print(delta_nd)
#print("-------------------")
#print(R_gd_ohne)
#print(R_gd_mit)
#print(delta_gd)
#print("-------------------")
#print(mean_dy)
#print(quer[0])
print(chi_dy)
print("-------------------")
#print(mean_nd)
#print(quer[1])
print(chi_nd)
print("-------------------")
#print(mean_gd)
#print(quer[2])
print(chi_gd)
print("-------------------")
print(chi)