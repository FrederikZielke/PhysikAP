import matplotlib.pyplot as plt
import numpy as np
from uncertainties import unumpy as unp
from uncertainties import ufloat
from scipy.stats import linregress

U_lila, I_lila = np.genfromtxt('content/messung_lila.csv', unpack = True, delimiter = ',')

#I_lila = I_lila * 10**(-9)

I_lila = np.sqrt(I_lila)

start = 0
stop = 0
for i in range(I_lila.size):
    if I_lila[i] > 0:
        if start == 0:
            start = i - 1
    if I_lila[i] > 0.7:
        stop = i
        print(I_lila[i])
        break



lin_lila = linregress(U_lila[start:stop], I_lila[start:stop])
a1_lila = ufloat(lin_lila.slope, lin_lila.stderr)
b1_lila = ufloat(lin_lila.intercept, lin_lila.intercept_stderr)
a_lila = lin_lila.slope
b_lila = lin_lila.intercept
U_g_lila = -b1_lila/a1_lila
x_lila = np.linspace(U_g_lila.n, U_lila[stop])
print(f'U_g_lila liegt bei {U_g_lila}V')
print(f'a1_lila und fehler: ', a1_lila)
print(f'b1_lila und fehler: ', b1_lila)

plt.plot(U_lila, I_lila, 'mx', label = r'Messwerte')
plt.plot(x_lila, (a_lila*x_lila+b_lila), color = 'black', label = r'Ausgleichsgerade')
#plt.plot(x_plot_lila, params[0]*x_plot_lila + params[1], 'k-', label='Lineare Regression')
plt.xlabel(r'$U \:/\: [V]$')
plt.ylabel(r'$\sqrt{I} \:/\: [\sqrt{nA}]$')
plt.title('Violettes Licht')
plt.legend(loc='best')
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.grid(which='major', linestyle='-', linewidth='0.5', color='black')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)

#plt.show()
plt.savefig('build/plotLila.pdf')