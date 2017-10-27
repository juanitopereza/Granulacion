import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
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
