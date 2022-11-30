import matplotlib.pyplot as plt
import numpy as np

t, T1, T2, pa, pb, N, = np.genfromtxt('messwerte.txt', unpack = True)

plt.subplots(constrained_layout = True)

plt.subplot(2, 2, 1)
plt.plot(t, T1, 'rd', label = r'Gekühltes Becken')
plt.plot(t, T2, 'gx', label = r'Erwärmtes Becken')
plt.legend(loc="best")
plt.xlabel(r'$t \,[$s$]$')
plt.ylabel(r'$T \,[°$C$]$')
plt.title(r"Temperaturen")

plt.subplot(2, 2, 2)
plt.plot(t, pa, '.b', label = r'$p_a$')
plt.plot(t, pb, '.r', label = r'$p_b$')
plt.legend(loc="best")
plt.xlabel(r'$t \,[$s$]$')
plt.ylabel(r"$p \,[$bar$]$")
plt.title(r'Druck')

plt.subplot(2, 2, 3)
plt.plot(T1, pa, '*', label = r'Kalt')
plt.plot(T2, pb, 'h', label = r'Warm')
plt.legend(loc="best")
plt.xlabel(r'$T \,[°$C$]$')
plt.ylabel(r"$p \,[$bar$]$")
plt.title(r'p/T')

params1, covariance_matrix1 = np.polyfit(t, T1, deg=1, cov=True)

errors1 = np.sqrt(np.diag(covariance_matrix1))

for name1, value1, error1 in zip('ab', params1, errors1):
    print(f'{name1} = {value1:.3f} ± {error1:.3f}')



x_plot = np.linspace(np.min(t), np.max(t))

plt.subplot(2, 2, 4)
plt.plot(t, T1, '.', label="Messwerte")
plt.plot(
    x_plot,
    params1[0] * x_plot + params1[1],
    label='Lineare Regression',
    linewidth=3,
)

plt.show()