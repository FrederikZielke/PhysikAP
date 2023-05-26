import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy as unp

L = ufloat(16.87, 0.05) * 0.001
C = ufloat(2.060, 0.003) * 10**(-9)

R_ap = unp.sqrt(4*L/C)

R_gem = 4.58*10**3

abw = (R_ap/R_gem - 1)

print("gemessen: ", R_gem)
print("theoretisch: ", R_ap)
print("Abweichung: ", abw)