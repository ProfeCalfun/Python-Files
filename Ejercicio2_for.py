contarVocales=0;
contarConsonantes=0;
print("\n-------Sistema Contador de vocales y consonantes---------\n");
for n in range(1,11):
    letra=input(f"{n}.- Ingrese una letra, por favor: ");
    if (letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u'):
        contarVocales+=1;
    else:
        contarConsonantes+=1;
print(f"\nCantidad de consonantes: {contarConsonantes} ");
print(f"Cantidad de vocales: {contarVocales}");
