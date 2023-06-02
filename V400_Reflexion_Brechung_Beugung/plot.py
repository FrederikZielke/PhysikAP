import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp
import scipy.constants as const

# Daten einlesen aus A2u3.csv
alpha, beta = np.genfromtxt('content/A2u3.csv', delimiter=',', unpack=True)

def strahlenversatz(alpha, beta, d):
    return d*(unp.sin(alpha - beta) / unp.cos(beta))

def beta_calc(alpha, n):
    return unp.arcsin(unp.sin(alpha)/n)

alpha_unp = unp.uarray(alpha, 1)
beta_unp = unp.uarray(beta, 1)

# Convert degrees to radians
alpha_rad = unp.radians(alpha_unp)
beta_rad = unp.radians(beta_unp)



# Calculate sin(alpha)/sin(beta)
result = unp.sin(alpha_rad) / unp.sin(beta_rad)
#round result to 3 digits
result_nominal = unp.nominal_values(result)
result_std_dev = unp.std_devs(result)
result_rounded = [np.round(nominal, 2) for nominal in result_nominal]
std_dev_rounded = [np.round(std, 2) for std in result_std_dev]


#print('brechungsindex ohne fehler',result)
for i in range(len(result_rounded)):
    print(f'{result_rounded[i]} \pm {std_dev_rounded[i]}')

# calculate the mean value of the refractive index and error

mean = np.mean(result_rounded)
std_dev = np.std(result_rounded, ddof=1)
print(f'Mittelwert: {mean} \pm {std_dev}')
print("Abweichung vom Literaturwert %",np.abs((mean-1.49)/1.49*100))

# calculate the speed of light in the medium with uncertainty
c = const.c
n = ufloat(mean, std_dev)
v = c/n
print(f'Geschwindigkeit: {v}')

# calculate the strahlenversatz
d = 5.85e-2
beta_rad_calc = beta_calc(alpha_rad, n)
# convert to degrees
beta_calc_print = unp.degrees(beta_rad_calc)

print('Strahlenversatz mit gemessenem Beta:')
for i in range(len(alpha)):
    print(f'{(strahlenversatz(alpha_rad[i], beta_rad[i], d))}', '&&', beta_calc_print[i], '&&',strahlenversatz(alpha_rad[i], beta_rad_calc[i], d), '\\\\')


# calculate the strahlenversatz with calculated beta
#print('Strahlenversatz mit berechnetem Beta:')

#for i in range(len(alpha)):
#    print(f'{(strahlenversatz(alpha_rad[i], beta_rad_calc[i], d))}')