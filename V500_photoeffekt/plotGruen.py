import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp
from uncertainties import ufloat
from scipy.stats import linregress

U_gruen, I_gruen = np.genfromtxt('content/messung_gruen.csv', unpack = True, delimiter = ',')


#I_gruen = I_gruen * 10**(-9)

I_gruen = np.sqrt(I_gruen)

start = 0
stop = 0
for i in range(I_gruen.size):
    if I_gruen[i] > 0:
        if start == 0:
            start = i - 1
    if I_gruen[i] > 0.5:
        stop = i
        print(I_gruen[i])
        break


lin_gruen = linregress(U_gruen[start:stop], I_gruen[start:stop])
a1_gruen = ufloat(lin_gruen.slope, lin_gruen.stderr)
b1_gruen = ufloat(lin_gruen.intercept, lin_gruen.intercept_stderr)
a_gruen = lin_gruen.slope
b_gruen = lin_gruen.intercept
U_g_gruen = -b_gruen/a_gruen
x_gruen = np.linspace(U_g_gruen, U_gruen[stop])
print(f'U_g_gruen liegt bei {U_g_gruen}V')
print(f'a1_gruen und fehler: ', a1_gruen)
print(f'b1_gruen und fehler: ', b1_gruen)

plt.plot(U_gruen, I_gruen, 'gx')
plt.plot(x_gruen, a_gruen*x_gruen + b_gruen, 'k-', label = r'Ausgleichsgerade')
plt.xlabel(r'$U \:/\: [V]$')
plt.ylabel(r'$\sqrt{I} \:/\: [\sqrt{nA}]$')
plt.title('Grünes Licht')
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

#plt.show()
plt.savefig('build/plotGruen.pdf')