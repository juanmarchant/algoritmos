# Ingresar n números y mostrar: 
# Todos los números que sean divisibles por 11
# El promedio de los números impares.
# El mayor de todos

cantidadNumeros = int(input("Ingrese la cantidad de numeros"))

sumaImpares = 0
contadorImpares = 0

contador = 0
numeroMayor = 0

while contador < cantidadNumeros:
    
    numero = int(input("Ingrese un numero: "))
    
    if contador == 0:
        numeroMayor = numero    
    
    if numero > numeroMayor:
        numeroMayor = numero

    if numero % 11 == 0:
        print(f"El numero {numero} es divisible por 11")
    
    if numero % 2 != 0:
        sumaImpares = sumaImpares + numero
        contadorImpares = contadorImpares + 1
    
    contador = contador + 1


if contadorImpares > 0:
    promedioImpares = sumaImpares / contadorImpares
    print("El promedio de los impares es: ", promedioImpares)
else:
    print("No se ingresaron impares")

print("El numero mayor es", numeroMayor)



