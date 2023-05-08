print("--------Ejercicio secuencia----------\n");
num=int(input("Ingrese un número entero: "));

for i in range(num,0,-1):
    num=num-1;
    for j in range(num,0,-1):
        print(j,end=" ");
    print("");
