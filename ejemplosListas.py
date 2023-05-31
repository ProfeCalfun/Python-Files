lista_a=[15,20,67];#Se crea una lista_a
lista_b=[45,30]#Se crea la lista_b
print(f"La lista es: {lista_a}");
#print(lista_a[0]);
#print(lista_a[1]);
#print(lista_a[2]);
#print(lista_a[3]);
#print(lista_a[-2]);
lista_a.extend(lista_b);#Extiende una lista
lista_a.insert(4,99);#Inserta el valor 99 en la posición 4
lista_a.remove(45);#Elimina el valor indicado (45). Si no lo encuentra, lanza un error.
lista_a.pop(0);#Elimina el valor en la posición cero. Si está vacío, elimina le último elemento insertado.
print(f"La lista nueva es: {lista_a}");