import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp
from uncertainties import ufloat
from scipy.stats import linregress

#Reihenfolge: lila, gelb, gruen, rot
U_g = np.array([-1.094547466957642, -1.3964305019281946, -0.6106345998605471, -0.6930460614610847])
lambda_lila = np.array([405,434,435,436,492])
lambda_gelb = np.array([577,579])
lambda_gruen = 546*10**(-9)
lambda_rot = 623*10**(-9)
lambda_gelb = lambda_gelb*10**(-9)
lambda_lila = lambda_lila*10**(-9)

f_lila = 2.99792458e8/lambda_lila
f_gelb = 2.99792458e8/lambda_gelb
f_gruen = 2.99792458e8/lambda_gruen
f_rot = 2.99792458e8/lambda_rot

#lin = linregress([f_lila[0], f_gelb[0],f_gruen,f_rot],[U_g[0],U_g[1],U_g[2],U_g[3]])
lin = linregress([f_lila[0], f_gruen],[U_g[0],U_g[2]])
a = lin.slope
b = lin.intercept
x = np.linspace(f_lila[0], f_rot)

plt.plot(x, a*x + b, 'k-', label = r'Ausgleichsgerade')
print(a)

plt.plot(f_lila[0], U_g[0], 'mx', label = r'Messwerte')
#plt.plot(f_lila[1], U_g[0], 'mx')
#plt.plot(f_lila[2], U_g[0], 'mx')
#plt.plot(f_lila[3], U_g[0], 'mx')
#plt.plot(f_lila[4], U_g[0], 'mx')
plt.plot(f_gelb[0], U_g[1], 'yx')
#plt.plot(f_gelb[1], U_g[1], 'yx')
plt.plot(f_gruen, U_g[2], 'gx')
plt.plot(f_rot, U_g[3], 'rx')
plt.xlabel(r'$U \:/\: [V]$')
plt.ylabel(r'$f \:/\: [Hz]$')

plt.savefig('build/frequenz.pdf')
plt.show()