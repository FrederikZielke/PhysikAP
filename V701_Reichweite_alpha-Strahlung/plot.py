import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.stats import norm
from scipy.stats import poisson

def P(k, mu):
    return (mu**k * np.exp(-mu)) / np.math.factorial(k)

dateien = [1,2]
R = np.zeros(len(dateien))
for i in dateien:
    p, N, nr = np.genfromtxt(f'content/messung{i}.csv', delimiter = ',', unpack = True)#dran denken messung1 wieder zu messung{i} zu ändern

    p0 = 1013.25 # mbar
    x0 = 5.5e-2 # m
    # p in effektive länge umrechnen
    x = x0 * p / p0
    N = N / 120
    # create a linear regression for 200 < N < 13000
    
    # create a mask for the values in N that are in the range 200 < N < 13000
    if i == 1:
        mask = (N > 1) & (N < 105)
    else:
        mask = (N > 0) & (N < 150)
    
    # create a linear regression for the values in N that are in the range 200 < N < 13000
    params, covariance = np.polyfit(x[mask], N[mask], deg = 1, cov = True)
    errors = np.sqrt(np.diag(covariance))

    # calculate the slope and the intercept of the linear regression
    m = ufloat(params[0], errors[0])
    b = ufloat(params[1], errors[1])
    y = ufloat(max(N/2),0)
    R_m = (y - b)/m
    R[i-1] = R_m.n

    R_m *= 1e3
    # print the slope and the intercept of the linear regression
    print(f'Ausgleichsgerade für die mittlere Reichweite {i}:')
    print(f'm = {m}')
    print(f'b = {b}')
    print(f'mittlere Reichweite {R_m}mm:')
    print(f'Energie der mittleren Reichweite = {(R_m/3.1) ** (2/3)}')
    # create a linspace for the linear regression
    x_lin = np.linspace(min(x[mask]), max(x[mask]), 1000)

    # Energie berechnen
    E = np.zeros(len(nr))
    E[0] = 4
    for j in range(1, len(nr)):
        E[j] = (nr[j]/nr[0]) * E[0]

    if i == 1:
        mask = (x > 0.001) & (x < 0.025)
    else:
        mask = (E > 0.5)

    # create a linear regression for x and E
    params, covariance = np.polyfit(x[mask], E[mask], deg = 1, cov = True)
    errors = np.sqrt(np.diag(covariance))

    # calculate the slope and the intercept of the linear regression
    m_e = ufloat(params[0], errors[0])
    b_e = ufloat(params[1], errors[1])

    # print the slope and the intercept of the linear regression
    print(f'Ausgleichsgerade der Energie {i}:')
    print(f'm = {m_e}')
    print(f'b = {b_e}')
    # R_m = 3.1*E_alpha ** (3/2) <=> E_alpha = (R_m/3.1) ** (2/3)
    # Das mit der Energie ist glaube ich nicht richtig
    R_m *= 1e-3
    print(f'E R_m mit Lin Reg = {m_e * R_m + b_e} MeV')

    # create a linspace for the linear regression
    x_lin_Energie = np.linspace(min(x[mask]), max(x[mask]), 1000)

    # create 3 subplots. 3 rows, 1 column. plot (p, N) in the first subplot and (p, nr) in the second subplot an N in a histogram in the third subplot
    #fig, ax = plt.subplots(2, 1, figsize = (10, 10))
    plt.plot(x, N, 'kx', label = 'Messwerte')
    plt.plot(x_lin, m.n * x_lin + b.n, 'r-', label = 'Lineare Regression')
    plt.axhline(y.n, color = 'b', linestyle = '-.', label = 'Plateauhalbierende')
    plt.xlabel(r'Effektive Reichweite $x \,/\, \mathrm{m}$')
    plt.ylabel(r'$N \,/\, \mathrm{s}^{-1}$')
    plt.legend(loc = 'best')
    plt.grid()

    plt.tight_layout()
    plt.savefig(f'build/plot{i}.pdf')
    plt.clf()

    plt.plot(x, E, 'kx', label = 'Messwerte')
    plt.plot(x_lin_Energie, m_e.n * x_lin_Energie + b_e.n, 'r-', label = 'Lineare Regression')
    plt.xlabel(r'$x \,/\, \mathrm{m}$')
    plt.ylabel(r'Energie $E \,/\, \mathrm{MeV}$')
    plt.legend(loc = 'best')
    plt.grid()

    plt.tight_layout()
    plt.savefig(f'build/plot{i}_Energie.pdf')
    plt.clf()
print(f'Abweichung der mittleren Reichweiten: {np.std(R)}')

N = np.genfromtxt('content/statistik.csv', delimiter = ',', unpack = True)
N = N/10

# calculate the expectet value of N
E = np.mean(N)

# calculate the variance of N
V = np.var(N)
print(f'Mittelwert: {E}')
print(f'Varianz: {V}')

x = np.linspace(min(N), max(N), 10000)
#xp = np.arange(1625, 1925, 1)
xp = np.arange(int(min(N) - 1), int(max(N)) + 2, 1)
gauss = norm.pdf(x, np.mean(N), np.std(N))
pois = poisson.pmf(xp, E)

fig, ax = plt.subplots(1, 1, figsize = (10, 10))
ax.hist(N, bins = 10, label = 'Messwerte', density = True)
ax.plot(x , gauss, 'k', label = 'Gaußverteilung')
ax.plot(xp, pois, label = 'Poissonverteilung')
ax.set_xlabel(r'$N\,/\,\mathrm{s}^{-1}$')
ax.set_ylabel(r'relative Häufigkeit')
ax.legend(loc = 'best')

fig.tight_layout()
fig.savefig('build/hist.pdf')
