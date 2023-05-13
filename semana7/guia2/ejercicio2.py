# Ingresar N números y mostrar:
        # a) Total de números primos ingresados
        # b) Total de números mayores a 10 y menores a 50.
        # c) Promedio de números entre 50 y 70.



cantidadNumeros = int(input("Cuantos numeros quiere ingresar?: "))

contador = 0 
totalPrimos = 0
totalNumeros10Menores50 = 0
totalNumeros50Y70 = 0
sumaNumeros50Y70 = 0

while contador < cantidadNumeros:
    contador = contador + 1

    numero = int(input("Ingrese un numero: "))

    contadorCasos = 0
    contadorPrimo = 0

    while contadorPrimo < numero:

        contadorPrimo = contadorPrimo + 1
        if numero % contadorPrimo == 0:
            contadorCasos = contadorCasos + 1

    if contadorCasos == 2:
        totalPrimos = totalPrimos + 1

    if numero > 10 and numero < 50:
        totalNumeros10Menores50 = totalNumeros10Menores50 + 1

    
    if numero >= 50 and numero <= 70:
        totalNumeros50Y70 = totalNumeros50Y70 + 1
        sumaNumeros50Y70 = numero + sumaNumeros50Y70


    
if totalPrimos != 0:
    print(f"De los {cantidadNumeros}, {totalPrimos} son primos")
else:
    print("De los numeros ingresados, ningun es primo")
    
if totalNumeros10Menores50 != 0:
    print(f"El total de numeros mayores a 10 y menores a 50 es: {totalNumeros10Menores50}")
else:
    print("No se ingresaron numeros mayores a 10 y menores a 50")

if totalNumeros50Y70 != 0:
    promedio = sumaNumeros50Y70 / totalNumeros10Menores50
    print(f"El promedio entre los numero de 50 a 70 es: {sumaNumeros50Y70}")
else:
    print("No se ingresaron numero entre 50 y 70")



