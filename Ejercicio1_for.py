contarMayores=0;
contarMenores=0;
contarCeros=0;
print("\n-----Sistema de Números----\n");
for n in range(5):
    num=int(input("Ingrese un número entero,por favor: "));
    if num>0:
        contarMayores=contarMayores+1;
    elif num<0:
        contarMenores=contarMenores+1;
    else:
        contarCeros=contarCeros+1;
print(f"\nLa cantidad de número mayores a cero es:{contarMayores}");
print(f"La cantidad de número menores a cero es:{contarMenores}");
print(f"La cantidad de número iguales a cero es:{contarCeros}");
