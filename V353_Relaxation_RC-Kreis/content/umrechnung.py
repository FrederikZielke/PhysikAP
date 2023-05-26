import numpy as np


t, u = np.genfromtxt('zeitkonstanteMesswerte.txt', unpack=True)
t /= 2

np.savetxt(
    'zeitkonstanteMesswerte2.txt',
    np.column_stack([t, u]),
    fmt=['%.1f', '%.2f'],
    delimiter='\t',
    header='t [ms]\t U[V]',
)