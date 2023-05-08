# Ingresar un número y mostrar los divisores del número ingresado.

numero = int(input("Ingrese un numero: "))

contador = 0

while contador < numero :
    contador = contador + 1

    if numero % contador == 0:
        print(contador)

