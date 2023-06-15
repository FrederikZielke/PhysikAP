import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from scipy.stats import norm
from scipy.stats import poisson

def P(k, mu):
    return (mu**k * np.exp(-mu)) / np.math.factorial(k)

dateien = [1,2]
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
    y = ufloat(max(N[mask]/2),0)

    # print the slope and the intercept of the linear regression
    print(f'Ausgleichsgerade {i}:')
    print(f'm = {m}')
    print(f'b = {b}')
    print(f'mittlere Reichweite {(y - b)/m}m:')
    # create a linspace for the linear regression
    x_lin = np.linspace(min(x[mask]), max(x[mask]), 1000)

    # create 3 subplots. 3 rows, 1 column. plot (p, N) in the first subplot and (p, nr) in the second subplot an N in a histogram in the third subplot
    fig, ax = plt.subplots(2, 1, figsize = (10, 10))
    ax[0].plot(x, N, 'kx', label = 'Messwerte')
    ax[0].plot(x_lin, m.n * x_lin + b.n, 'r-', label = 'Lineare Regression')
    ax[0].axhline(y.n, color = 'b', linestyle = '-.')
    ax[0].set_xlabel(r'Effektive Reichweite $x \,/\, \mathrm{m}$')
    ax[0].set_ylabel(r'$N \,/\, \mathrm{s}^{-1}$')
    ax[0].legend(loc = 'best')
    ax[0].grid()

    ax[1].plot(x, nr, 'kx', label = 'Messwerte')
    ax[1].set_xlabel(r'$x \,/\, \mathrm{m}$')
    ax[1].set_ylabel(r'$N_\mathrm{R}$')
    ax[1].legend(loc = 'best')
    ax[1].grid()



    fig.tight_layout()
    fig.savefig(f'build/plot{i}.pdf')

plt.clf()

N = np.genfromtxt('content/statistik.csv', delimiter = ',', unpack = True)
N = N/10

# calculate the expectet value of N
E = np.mean(N)

x = np.linspace(min(N), max(N), 10000)
#xp = np.arange(1625, 1925, 1)
xp = np.arange(int(min(N) - 1), int(max(N)) + 2, 1)
gauss = norm.pdf(x, np.mean(N), np.std(N))
pois = poisson.pmf(xp, E)

fig, ax = plt.subplots(1, 1, figsize = (10, 10))
ax.hist(N, bins = 10, label = 'Messwerte', density = True)
ax.plot(x , gauss, 'k', label = 'Gaußverteilung')
ax.plot(xp, pois, label = 'Poissonverteilung')
ax.set_xlabel(r'$N$')
ax.set_ylabel(r'$\mathrm{Häufigkeit}$')
ax.legend(loc = 'best')

fig.tight_layout()
fig.savefig('build/hist.pdf')
