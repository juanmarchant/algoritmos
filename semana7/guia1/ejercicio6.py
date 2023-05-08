# Ingresar un número y mostrar si el número ingresado es primo o no lo es.
# Un número es primo cuando solo es divisible por uno o por sí mismo,
# por ningún otro número más.



contadorPrimo = 0 
contador = 0

numero = int(input("Ingrese un numero: "))

while contador < numero : 

    contador =  contador + 1
    if numero % contador == 0:
        contadorPrimo = contadorPrimo + 1


if contadorPrimo == 2:
    print(f"el numero {numero} ingresado si es primo")
else:
    print("No es primo")

