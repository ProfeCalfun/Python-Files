print("----Tabla de Multiplicar----\n");
listaMultiplicar=[];
num=int(input("Ingrese un número del 1 al 10: "));
for x in range(1,11):
    resultado=num*x;
    listaMultiplicar.append(resultado);
    print(f"{num} * {x} = {resultado}");
print(f"La lista es: {listaMultiplicar}");

