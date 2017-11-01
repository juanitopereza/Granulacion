import numpy as np
import matplotlib.pyplot as plt

#%%
def find_nearest(array,value):
    idx = np.argsort(np.abs(array-value))[0:2]
    return idx
#%%
NIR = np.loadtxt("spnir.dat")
VIS = np.loadtxt("spvis.dat")

NIR[:,0] = (1.0/NIR[:,0] )*1e8
#%%
horiz = np.ones(len(NIR[:,0]))

fig = plt.figure(figsize = (15,15))

plt.plot(NIR[:,0], NIR[:,1], c="r")
plt.plot(NIR[:,0], horiz)
plt.xlim(6219,6232)
plt.title("Espectro corregido")
plt.xlabel(u"$Número\ de\ onda\ cm^{-1}$")
plt.show()
#%%

# limites de la region de la linea en Angstroms
lambda_min = 5528.0
lambda_max = 5528.8

# porcentaje de desecho antes del continuo
des = 10.0

#NUmero de puntos para definir la bisectriz
N_partes = 40

region = NIR[(NIR[:,0] > lambda_min) & (NIR[:,0] < lambda_max)]

minimo = min(region[:,1])
L_min = region[:,0][region[:,1] == min(region[:,1])]
tope = 1.0 - (des/100.0*(1.00 - minimo))

region_izq = region[region[:,0] < L_min]
region_der = region[region[:,0] > L_min]

#%%
bisectriz = np.zeros((N_partes,2))

bisectriz[0,1] = minimo
bisectriz[0,0] = L_min

pasos = np.linspace(minimo,tope,N_partes)

bisectriz[:,1] = pasos

for i in range(1,N_partes):

    izquierda = region_izq[:,0:2][find_nearest(region_izq[:,1],pasos[i])]
    x_izq = izquierda[0,0]+(pasos[i]-izquierda[0,1])*(izquierda[1,0]-izquierda[0,0])/(izquierda[1,1]-izquierda[0,1])

    derecha = region_der[:,0:2][find_nearest(region_der[:,1],pasos[i])]
    x_der = derecha[0,0]+(pasos[i]-derecha[0,1])*(derecha[1,0]-derecha[0,0])/(derecha[1,1]-derecha[0,1])

    bisectriz[i,0] = (x_izq + x_der)/2.0


#%%
n_points_extrapol = 5

m,b = np.polyfit(bisectriz[1:n_points_extrapol+1,0],bisectriz[1:n_points_extrapol+1,1],1)

core = (minimo-b)/m

x = np.linspace(lambda_min,lambda_max)

#%%
line = np.ones(len(region[:,0]))*tope

fig = plt.figure(figsize = (15,15))

plt.plot(region[:,0], line, c="r")
plt.scatter(region[:,0], region[:,1], s=5)
plt.scatter(L_min,minimo)
plt.scatter(bisectriz[:,0], bisectriz[:,1], c="r")
plt.scatter(core,minimo)
#plt.plot(x,m*x+b)
plt.ticklabel_format(useOffset=False)
#plt.xlim(5528.350,5528.355)
#plt.ylim(0.1,1.1)
plt.xlabel(u"$Longitud\ de\ onda\ [\AA]$")

plt.savefig("core_5puntos.pdf")


plt.show()
