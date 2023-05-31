import numpy as np
import random as rdm

print("----Números Aleatorios Arrays-----\n");
arregloNum4=np.arange(10);
for i in range(len(arregloNum4)):
    numAleatorios=rdm.randint(0,100);
    print(f"El num aleatorio es: {numAleatorios}");
    arregloNum4[i]=numAleatorios;
    print(f"Se agregó en la pos: {[i]} el num: {numAleatorios}");
arregloCopy=arregloNum4[:].copy();#Se copia el arreglo
maximo=arregloCopy.max();
minimo=arregloCopy.min();
promedio=arregloCopy.mean();
suma=arregloCopy.sum();
print(f"El arreglo es:{arregloCopy}")
print(f"El número máximo es: {maximo}");
print(f"El número mínimo es: {minimo}");
print(f"El promedio es: {promedio}");
print(f"La suma es: {suma}");


