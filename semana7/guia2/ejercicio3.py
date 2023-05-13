# Realizar un ejercicio que pida el ingreso de N números, mostrar:
    #  Cuantos números ingresados son positivos
    #  Cuantos son negativos
    #  Cuantos son ceros
    #  La suma de los positivos mayores a 20
    #  La multiplicación de los negativos menores a -100
    #  El promedio de los números pares ingresados
    #  El mayor de todos
    #  El menor de todos


cantidadNumeros = int(input("Cuantos numeros quiere ingresar?: "))

contador = 0

totalPositivos = 0
totalNegativos = 0
totalCeros = 0
sumaPositivosMayor20 = 0
multiplicacionMenoresNegativo100 = 1
sumaPares = 0
numeroMayor = 0
numeroMenor = 0
contadorPares = 0
while contador < cantidadNumeros:

    contador = contador + 1

    numero = int(input("Ingresa un numero: "))

    if contador == 1:
        numeroMayor = numero
        numeroMenor = numero
    else:
        if numero > numeroMayor:
            numeroMayor = numero
        
        if numero < numeroMenor:
            numeroMenor = numero

    if numero > 0:
        totalPositivos = totalPositivos + 1
        if numero > 20:
            sumaPositivosMayor20 = sumaPositivosMayor20 + numero
    else:
        totalNegativos = totalNegativos + 1

        if numero < -100:
            multiplicacionMenoresNegativo100 = multiplicacionMenoresNegativo100 * numero
    
    if numero % 2 == 0:
        contadorPares = contadorPares + 1
        sumaPares = numero + sumaPares

    if numero == 0:
        totalCeros = totalCeros + 1

if totalPositivos != 0:
    print(f"De los {cantidadNumeros} numeros ingresados, {totalPositivos} son positivos")
else:
    print("No se ingresaron numeros positivos")

if totalNegativos != 0:
    print(f"De los {cantidadNumeros} numeros ingresados, {totalNegativos} son negativos")
else:
    print("No se ingresaron numeros negativos")

if totalCeros != 0:
    print(f"De los {cantidadNumeros} numeros ingresados, {totalCeros} son ceros")
else:
    print("No se ingresaron ceros")

print(f"El numero mayor es: {numeroMayor} y el numero menor es {numeroMenor}")

if sumaPositivosMayor20 !=0:
    print(f"La suma de los numeros mayores a 20 es: {sumaPositivosMayor20}")
else:
    print("No se ingresaron numeros mayores a 20")

if multiplicacionMenoresNegativo100 != 1:
    print(f"La multiplicacion de los numeros menores a -100 es: {multiplicacionMenoresNegativo100}") 
else:
    print("No se ingresaron numeros menores a -100")

if contadorPares != 0:
    promedioPares = sumaPares / contadorPares
    print(f"El promedio entre los numeros pares ingresados es: {promedioPares}")
else:
    print("No se ingresaron numeros pares")


