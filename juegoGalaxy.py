import random;

nieve="";
''' Se define el rango para las filas'''
for x in range(20):  
    ''' Se define el rango para laas columnas'''
    for i in range(80):
        if random.randint(1, 100) % 8 == 0 :
            if random.randint(1, 100) % 2 == 0 :
                nieve += "*";
            else:
                nieve += "´";
        else:
            nieve += " ";
    print(nieve);
    nieve = "";
