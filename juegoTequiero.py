import random
 
print("")
print("Amorímetro")
print("Piensa en una persona que tu quieres saber si te quiere o no.(Presione enter para continuar)")
input()
veces = random.randint(4,20)
 
nivel_de_amor = 0
for vez in range(veces):
    dado =  random.randint(1,20)
    print("Me quiere mucho")
    nivel_de_amor = 3
    input()
    if dado%3 == 0 and vez >= 4 :
        break;
    
    dado =  random.randint(1,20)
    print("Me quiere poquito")
    nivel_de_amor = 2
    input()
    if dado%3 == 0  and vez >= 4:
        break;
  
    dado =  random.randint(1,20)
    print("Me quiere nada")
    nivel_de_amor = 1    
    input()
    if dado%3 == 0  and vez >= 4 :        
       break
        
if nivel_de_amor == 3:
    for i in range(10):
        print("Felicidades, ¡¡¡Te Quieren Mucho!!!")
        for j in range(3):
            print("               Mucho!!!")
elif nivel_de_amor == 2:
    print("Te quieren poquito, por decir algo. Peor es nada ;-)   . . .  XD")
    for i in range(10):
        print("Tal vez tengas que hacer más...")
else:
    print("Lo siento amigo(a), no te quieren nada. Buscate otra(o) mejor ;-(")
    for i in range(10):
        print("  FK")
 
print("")
