import numpy as np
from uncertainties import unumpy as unp
from uncertainties import ufloat

# Messwerte einlesen aus A-Scan_Acryl.csv
a, b, n = np.genfromtxt('content/A-scan_Acryl.csv', delimiter=',', unpack=True)

h = ufloat(79.76, 0.04)
ausgleich = ufloat(-3, 1.4)

# UArrays
af = unp.uarray(a, np.zeros(len(a)))
bf = unp.uarray(b, np.zeros(len(b)))

# Berechnung der Durchmesser
d = h -af -bf -ausgleich
print(d)
g = a + b
print(g)
print('A-Scan:')

for i in range(len(a)):
    print(f'{n[i]} & {a[i]} & {b[i]} & {h  - af[i] - bf[i] - ausgleich}')

for i in range(len(af)):
    print(f'Durchmesser Loch {i+3} = {h - af[i] - bf[i]- ausgleich}')



print('B-Scan:')

# Messwerte einlesen aus dem B-Scan
n2, a, b , afalsch= np.genfromtxt('content/B-scan_Acryl.csv', delimiter=',', unpack=True)

af2 = unp.uarray(a, np.zeros(len(a)))
bf2 = unp.uarray(b, np.zeros(len(b)))
afalschf = unp.uarray(afalsch, np.zeros(len(afalsch)))

for i in range(len(af2)):
    print(f'Durchmesser Loch {i+3} = {h  - af2[i] - bf2[i] - ausgleich}')

d = h -af2 -bf2 -ausgleich
print(d)
g = a + b
print(g)
for i in range(len(a)):
    print(f'{n[i]} & {a[i]} & {b[i]} & {h  - af2[i] - bf2[i] - ausgleich}')

# daten einlesen SchieblehreMessung.csv
schieblehreA, schieblehreB, schieblehreD = np.genfromtxt('content/SchieblehreMessung.csv', delimiter=',', unpack=True)
#print(f'lochnr: {schieblehreD}')
schieblehreD[9] = schieblehreD[10]
af[7] = af[8]
bf[7] = bf[8]


# Prozentuale Abweichung der Durchmesser
print(f'Loch & A-Scan & B-Scan')
for i in range(len(a)):
    print(f'{n[i]} & {((h - af[i] - bf[i]- ausgleich - schieblehreD[i+2])/schieblehreD[i+2])} & {((h  - af2[i] - bf2[i] - ausgleich - schieblehreD[i+2])/schieblehreD[i+2])}')
