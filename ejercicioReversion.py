# Obtener el número del usuario manualmente 
num = int (input ('Ingrese su número favorito:')) 
# Iniciar valor a nulo 
test_num = 0;

for i in range(5): 
    rest = num% 10;
    test_num = (test_num * 10) + rest;
    num = num // 10;
# # Mostrar el resultado 
    print ('El número inverso es: {}',(test_num));