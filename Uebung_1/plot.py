import matplotlib.pyplot as plt
import numpy as np

d, N = np.genfromtxt("data.txt", unpack=True)

plt.figure(constrained_layout=True)

plt.subplot(1, 2, 1)
plt.plot(d, N, ".")
plt.xlabel(r"d [cm]")
plt.ylabel(r"N [1/60s]")

plt.subplot(1, 2, 2)
plt.plot(d, N, ".")
plt.xlabel(r"d [cm]")
plt.ylabel(r"N [1/60s]")
plt.yscale("log")

plt.savefig("Uebung_1.pdf")
