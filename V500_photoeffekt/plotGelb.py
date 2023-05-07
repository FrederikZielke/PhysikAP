import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp
from uncertainties import ufloat
from scipy.stats import linregress

U_gelb, I_gelb = np.genfromtxt('content/messung_gelb.csv', unpack = True, delimiter = ',')

I_gelb = np.sqrt(I_gelb)

start = 0
stop = 0
for i in range(I_gelb.size):
    if I_gelb[i] > 0:
        if start == 0:
            start = i 
    if I_gelb[i] > 0.7:
        stop = i 
        break

lin_gelb = linregress(U_gelb[start:stop], I_gelb[start:stop])
a1_gelb = ufloat(lin_gelb.slope, lin_gelb.stderr)
b1_gelb = ufloat(lin_gelb.intercept, lin_gelb.intercept_stderr)
a_gelb = lin_gelb.slope
b_gelb = lin_gelb.intercept
U_g_gelb = -b_gelb/a_gelb
x_gelb = np.linspace(U_g_gelb, U_gelb[stop])
print(f'U_g_gelb liegt bei {U_g_gelb}V')

plt.plot(U_gelb, I_gelb, 'yx')
plt.plot(x_gelb, a_gelb*x_gelb + b_gelb, 'k-', label = r'Ausgleichsgerade')
plt.xlabel(r'$U \:/\: [V]$')
plt.ylabel(r'$\sqrt{I} \:/\: [\sqrt{nA}]$')
plt.title('Gelbes Licht')
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

plt.savefig('build/plotGelb.pdf')
plt.show()
plt.clf()