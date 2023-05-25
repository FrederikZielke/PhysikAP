from uncertainties import ufloat
from uncertainties.unumpy import sin
from scipy.stats import sem
import numpy as np


x = np.genfromtxt("fallzeitKugelKlein.txt", unpack=True)

print(np.mean(x))

print(np.std(x, ddof=1) / np.sqrt(np.size(x)))




