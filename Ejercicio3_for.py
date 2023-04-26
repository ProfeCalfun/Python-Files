print("\n--------Sistema Tabla de Multiplicar-------\n");
num=int(input("Ingrese un número entero, por favor: \n"));
print(f"\n----Tabla de multiplicar del {num}----");
for n in range(1,13):
    resultado=num*n;
    print(f"\t{num} x {n} = {resultado}");