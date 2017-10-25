import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%%

NIR = np.loadtxt("spnir.dat")
VIS = np.loadtxt("spvis.dat")
#%%

fig = plt.figure(figsize = (15,15))

plt.plot(NIR[:,0], NIR[:,1], c="r")

horiz = np.ones(len(NIR[:,0]))
plt.plot(NIR[:,0], horiz)
plt.xlim(16026,16030)
plt.title("Espectro corregido")
plt.xlabel(u"$Número\ de\ onda\ cm^{-1}$")
plt.show()

#%%

# limites de la region de la linea
lambda_min = 16026.0
lambda_max = 16030.0

# porcentaje de desecho antes del continuo
des = 10.0

#tolerancia para encontrar alturas en la linea
tol = 0.01

N_partes = 20

region = NIR[(NIR[:,0] > lambda_min) & (NIR[:,0] < lambda_max)]

minimo = min(region[:,1])
L_min = region[:,0][region[:,1] == min(region[:,1])]
tope = 1.0 - (des/100.0*(1.00 - minimo))

h = (tope - minimo)/N_partes

bisectriz = np.zeros((N_partes,2))

bisectriz[:,1] = np.linspace(minimo,tope,N_partes)
bisectriz[0,0] = region[:,0][region[:,1] == min(region[:,1])]



for i in range(1,N_partes):

    #print(region[:,0][abs(bisectriz[i,1] - region[:,1]) <= tol])
    cercanos = region[:,0][abs(bisectriz[i,1] - region[:,1]) <= tol]
    izquierda = np.mean(cercanos[cercanos < L_min])
    derecha = np.mean(cercanos[cercanos > L_min])
    bisectriz[i,0] = (izquierda + derecha)/2.0

#%%
#p = np.polyfit(region[:,0], region[:,1], 2)
#p
#z = np.poly1d(p)
#x = np.linspace(region[:,0][0],region[:,0][-1])
#plt.plot(x, z(x), c="g")

line = np.ones(len(region[:,0]))*tope

fig = plt.figure(figsize = (15,15))

plt.plot(region[:,0], line, c="r")
plt.scatter(region[:,0], region[:,1], s=2)
plt.scatter(L_min,minimo)
plt.scatter(bisectriz[:,0], bisectriz[:,1], c="r")
plt.xlabel(u"$Número\ de\ onda\ cm^{-1}$")

plt.savefig("bisectriz.pdf")


plt.show()

#%%

DAT = pd.read_fwf("table2", header=None)#, dtype="str")
#%%

DAT.columns = ["0", "1", "2", "3", "intensi", "long", "6", "7", "8", "9", "10", "11", "12", "13", "14"]

DAT

DAT_1 = DAT.apply(pd.to_numeric, errors="coerce")
DAT_1



type(DAT_1["intensi"][14])



filtrado = DAT_1[DAT_1['intensi'].apply(lambda x: type(x) in [int, np.int64, float, np.float64])]
DAT
filtrado
#%%

fig = plt.figure(figsize = (15,15))

plt.scatter(DAT_1["long"], DAT_1["intensi"], s=10)
plt.show()


#%%

LAMB = pd.read_fwf("Nave_wavelengths.txt", sikprows=9)#, dtype="str")



LAMB.columns = ["Wavelengths"]

long_nave = np.array(LAMB["Wavelengths"][3:]).astype(np.float)
long_nave

mag = np.ones(len(long_nave))

#%%

fig = plt.figure(figsize = (15,15))

plt.scatter(long_nave, mag, marker="|", s=10000)
#plt.xlim(6000,7000)
plt.xlabel(u"$Longitud\ de\ onda\ [\AA]$")
plt.title(u"$Líneas\ de\ FE\ I$")
plt.show()
