import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp
import scipy.constants as const

# import data from A4.csv
alpha, alpha2_gruen, alpha2_rot = np.genfromtxt('content/A4.csv', delimiter=',', unpack=True)

# convert to unp array
alpha_unp = unp.uarray(alpha, 1)
alpha2_gruen_unp = unp.uarray(alpha2_gruen, 1)
alpha2_rot_unp = unp.uarray(alpha2_rot, 1)

# convert to radians
alpha_rad = unp.radians(alpha_unp)
alpha2_gruen_rad = unp.radians(alpha2_gruen_unp)
alpha2_rot_rad = unp.radians(alpha2_rot_unp)

# Brechungsindex Kronglas
n = 1.55

# gamma prisma
gamma = 60
gamma = unp.radians(gamma)

# calculate beta1
beta1_gruen_rad = unp.arcsin(unp.sin(alpha_rad) / n)
beta1_rot_rad = unp.arcsin(unp.sin(alpha_rad) / n)

# calculate beta2
beta2_gruen_rad = gamma - beta1_gruen_rad
beta2_rot_rad = gamma - beta1_rot_rad

# calculate delta
delta_gruen = (alpha_rad + alpha2_gruen_rad) - (beta1_gruen_rad + beta2_gruen_rad)
delta_rot = (alpha_rad + alpha2_rot_rad) - (beta1_rot_rad + beta2_rot_rad)

# convert to degrees
delta_gruen = unp.degrees(delta_gruen)
delta_rot = unp.degrees(delta_rot)
beta1_gruen = unp.degrees(beta1_gruen_rad)
beta2_gruen = unp.degrees(beta2_gruen_rad)
beta1_rot = unp.degrees(beta1_rot_rad)
beta2_rot = unp.degrees(beta2_rot_rad)


print('gruen')
for i in range(len(beta1_gruen)):
    print(f'{alpha_unp[i]} & {alpha2_gruen[i]} & {beta1_gruen[i]} & {beta2_gruen[i]} & {delta_gruen[i]} ')


print('rot')
for i in range(len(beta1_rot)):
    print(f'{alpha_unp[i]} & {alpha2_rot[i]} & {beta1_rot[i]} & {beta2_rot[i]} & {delta_rot[i]} ')



# ab jetzt der ganze Gitterquatsch
# import data from A5.csv
k, phi_gruen, phi_rot, d_nutzlos = np.genfromtxt('content/A5.csv', delimiter=',', unpack=True)

# convert to unp array
phi_gruen_unp = unp.uarray(phi_gruen, 1)
phi_rot_unp = unp.uarray(phi_rot, 1)

# convert to radians
phi_gruen_rad = unp.radians(phi_gruen_unp)
phi_rot_rad = unp.radians(phi_rot_unp)

help = np.zeros(len(phi_gruen_rad))
lambda_gruen = unp.uarray(help, 0)
lambda_rot = unp.uarray(help, 0)

d = [1.67, 3.33, 10]
#convert d to micrometer
d = [i * 10**(-6) for i in d]
# calculate wavelength
print('k:    d:       phi:       lambda:')
#for i in range(len(d)):
#    for j in range(0,2):
#        if k[j] != 0:
#            print(f'{k[j]} & {d[i]} & {phi_gruen_rad[j]} & {d[i] * unp.sin(phi_gruen_rad[j]) / k[j]}')
for i in range(0,2):
    if k[i] != 0:
        print(f'{k[i]} & {d[0]} & {unp.degrees(phi_gruen_rad[i])} & {d[0] * unp.sin(phi_gruen_rad[i]) / k[i]}')

for i in range(2,6):
    if k[i] != 0:
        print(f'{k[i]} & {d[1]} & {unp.degrees(phi_gruen_rad[i])} & {d[1] * unp.sin(phi_gruen_rad[i]) / k[i]}')

for i in range(6,17):
    if k[i] != 0:
        print(f'{k[i]} & {d[2]} & {unp.degrees(phi_gruen_rad[i])} & {d[2] * unp.sin(phi_gruen_rad[i]) / k[i]}')

for i in range(len(lambda_gruen)):
    if k[i] != 0:
        if phi_gruen_rad[i] != 0:
            if d_nutzlos[i] == 600:
                lambda_gruen[i] = d[0] * unp.sin(phi_gruen_rad[i]) / k[i]
            elif d_nutzlos[i] == 300:
                lambda_gruen[i] = d[1] * unp.sin(phi_gruen_rad[i]) / k[i]
            elif d_nutzlos[i] == 100:
                lambda_gruen[i] = d[2] * unp.sin(phi_gruen_rad[i]) / k[i]

for i in range(len(lambda_gruen)):
    print(f'{k[i]} & {lambda_gruen[i]}')
count = 0
mittelwert = ufloat(0,0)
for i in range(len(lambda_gruen)):
    if lambda_gruen[i] != 0:
        mittelwert += lambda_gruen[i]
        count += 1
print(f'count: {count}')
mittelwert = mittelwert / 14
# convert to nanometer
mittelwert = mittelwert * 10**9
print(f'mittelwert: {mittelwert}')
print(f'Prozentuale Abweichung: {((mittelwert - 532) / 532) * 100}')
    
for i in range(len(lambda_rot)):
    if k[i] != 0:
        if phi_rot_rad[i] != 0:
            if d_nutzlos[i] == 600:
                lambda_rot[i] = d[0] * unp.sin(phi_rot_rad[i]) / k[i]
            elif d_nutzlos[i] == 300:
                lambda_rot[i] = d[1] * unp.sin(phi_rot_rad[i]) / k[i]
            elif d_nutzlos[i] == 100:
                lambda_rot[i] = d[2] * unp.sin(phi_rot_rad[i]) / k[i]

for i in range(len(lambda_rot)):
    print(f'{k[i]} & {lambda_rot[i]}')
mittelwert = ufloat(0,0)
count = 0
for i in range(len(lambda_rot)):
    if lambda_rot[i] != 0:
        mittelwert += lambda_rot[i]
        count += 1
print(f'count: {count}')
mittelwert = mittelwert / 14
# convert to nanometer
mittelwert = mittelwert * 10**9
print(f'mittelwert: {mittelwert}')
print(f'Abweichung in %: {((mittelwert - 635) / 635) * 100}')