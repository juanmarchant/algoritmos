# Ingresar n números y mostrar la suma de los números mayores a 30 ingresados

sumaTotal = 0
cantidadNumeros = int(input("Cuantos numeros quiere ingresar ?: "))
acumulador = 0

while acumulador < cantidadNumeros:

    numero = int(input("Ingrese un numero: "))

    if numero > 30:
        sumaTotal = sumaTotal + numero

    acumulador = acumulador + 1

print("La suma total de los numeros mayores a 30 es: ", sumaTotal)
