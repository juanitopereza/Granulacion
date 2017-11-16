import numpy as np
import matplotlib.pyplot as plt
from os import listdir
#%%
def find_nearest(array,value):
    idx = np.argsort(np.abs(array-value))[0:2]
    return idx
#%%
mibisec = {}
archivos = listdir("./lineas")

NAVE = np.loadtxt("lineas_NAVE.txt")

c = 299792458.0 # CODATA
grav_red = 625.0 # redshift gravitacional


for cosa in archivos:
    mibisec[cosa] = np.loadtxt("./lineas/{}".format(cosa))
    linea_nave = NAVE[find_nearest(NAVE,mibisec[cosa][1][0])][0]
    mibisec[cosa][:,0] = c*(mibisec[cosa][:,0] - linea_nave)/linea_nave - grav_red
len(mibisec)
#%%

plt.figure(figsize=(15,15))

for cosa in archivos:
    plt.scatter(mibisec[cosa][0,0],mibisec[cosa][0,1])
    plt.plot(mibisec[cosa][2:,0],mibisec[cosa][2:,1])

plt.xlim(-1000,1000)
plt.ticklabel_format(useOffset=False)
plt.xlabel("$Velocidad\ [m/s]$")
plt.ylabel("$F/F_c$")

#plt.savefig("plots.pdf")
plt.show()
