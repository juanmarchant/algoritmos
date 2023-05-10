# Se necesita enseñar a multiplicar a niños de enseñanza básica.
# Para tal fin, se necesita crear un programa en Python que permita ingresar un número
# (validar que el número ingresado este comprendido entre 1 y 12).
# A partir de este número, mostrar la tabla de multiplicar.

import os

print("===== TABLAS 1-12 =====")
r = 's'

while r == 's':

    while True:
        try:
            tablaMultiplicar = int(input("Ingrese un numero del 1-12: "))
            if tablaMultiplicar < 0:
                print("El numero ingresado es negativo, porfavor intentalo con un numero postivo")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, recuerda un caracter valido del 1-12")

    contador = 0

    while contador < 12:
        contador = contador + 1
        print(f"{tablaMultiplicar} * {contador} =  {tablaMultiplicar * contador}")

    while True:
        try:
            r = input("Quieres volver a ingresar otro numero? (s/n): ").lower()
            if r != 's' and r != 'n':
                print("Ingresa alguna de las opciones (s: si | n: no): ")
            else:
                os.system("cls")
                break

        except ValueError:
            print("Error, caracter no valido.. recuerda ingresar (s: si | n: no): ")





