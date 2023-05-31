import random
 
listaNumeros = []
print("")
print("Ingrese sus 5 números de la suerte")
for i in range(5):
    num=int(input("Ingrese número: "))
    listaNumeros.append(num)
 
print("")
print("Usted ingresó los siguientes números: ", listaNumeros)
 
lista = []
for turno in range(1,6) :
    flag = True
    while flag :
        aleatorio = random.randint(1,10)
        if lista.count(aleatorio) == 0 :
            lista.append(aleatorio)
            flag = False
print("")
print("")
print("Los números sorteados en la ronda fueron: ")
print(lista)
print("")
contador = 0
for x in listaNumeros:
    if lista.count(x) == 1:
        contador += 1
        print(f"Le achuntaste a {x}")
if contador == 5 :
    print("Hoy es su día de suerte. Ha ganado ¡!!!")
    for i in range(10):
        print("Eres una ganador!!!!!!!!!!")
        break
else:
    print("Lo siento, pero no has ganado en esta ronda")
