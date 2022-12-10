import matplotlib.pyplot as plt
import numpy as np
from uncertainties import ufloat
import uncertainties.unumpy as unumpy

r_klein = ufloat(0.7795, 0.001)
r_gross = ufloat(0.7875, 0.001)
m_klein = ufloat(4.4531, 0)
m_gross = ufloat(4.8953, 0)
k_klein = ufloat(0.00007640, 0)
t_gross = ufloat(53.121, 0.149)
t_klein = ufloat(13.016, 0.018)
roh_wasser = ufloat(0.998467, 0)


roh_klein = (3*m_klein)/(4*np.pi*(r_klein)**3)
roh_gross = (3*m_gross)/(4*np.pi*(r_gross)**3)

print(roh_klein)
print(roh_gross)

eta = k_klein * (roh_klein - roh_wasser) * t_klein 
print(eta)


k_gross = (eta)/((roh_gross - roh_wasser) * t_gross)

print(k_gross)

eta2 = k_gross * (roh_gross - roh_wasser) * 26.85

v_max = 0.05 / 26.85
v_min = 0.05 / 53.79

reynold_min = (v_min * r_gross * 0.01 * 2 * roh_gross * 1000) / eta
reynold_max = (v_max * 2 * r_gross * roh_gross * 1000) / (eta2*100)
print(reynold_min)
print(reynold_max)

