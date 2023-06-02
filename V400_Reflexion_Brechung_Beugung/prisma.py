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
    print(f'{alpha_unp[i]} & {alpha2_gruen[i]} & {beta1_gruen[i]} & {beta2_gruen[i]} & {delta_gruen[i]} \\\\')


print('rot')
for i in range(len(beta1_rot)):
    print(f'{alpha_unp[i]} & {alpha2_rot[i]} & {beta1_rot[i]} & {beta2_rot[i]} & {delta_rot[i]} \\\\')