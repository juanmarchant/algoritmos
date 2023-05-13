# Ingresar un numero y mostrar si el numero ingresado es Perfecto o no lo es.
# Un numero es perfecto cuando la suma de sus divisores (sin contar el mismo numero) da como resultado el mismo numero:
# Ej 6 es perfecto, sus divisores son 1, 2, 3, 6, si sumo 1+2+3=6 6=6

numero = int(input("Ingrese un numero: "))

contador = 0
sumaDivisores = 0

while contador < numero-1:
    contador = contador + 1
    
    if numero % contador == 0:
        sumaDivisores = contador + sumaDivisores

if sumaDivisores == numero:
    print(f"El numero {numero} es perfecto")
else:
    print(f"El numero {numero} no es perfecto")

