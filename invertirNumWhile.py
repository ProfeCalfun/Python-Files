# Obtener el número del usuario manualmente 
num = int (input ('Ingrese su número favorito:')) 
# Iniciar valor a nulo 
test_num = 0;
resultado=0;
i=1;
while i <= 3: 
    resto1=num%10;
    resultado=(resultado*10)+resto1;
    num=int(num/10);
    i+=1;
    print(resultado);
