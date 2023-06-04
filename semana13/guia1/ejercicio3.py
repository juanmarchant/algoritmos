# Llene un arreglo de largo N con notas, una vez lleno:
# •	Calcular el promedio de aprobados y el promedio de los reprobados
# •	Muestre la cantidad de aprobados y reprobados.

import os

while True:
    try:
        largoArray = int(input("Ingrese el largo de el arreglo: "))
        if largoArray <= 0:
            print("Ingrese un valor mayor a 0")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, caracter no valido")

matrizNota = []

for i in range(largoArray):
    while True:
        try:
            nota = float(input("Ingresa la nota (ej: 7.0)"))
            if nota <= 0:
                print("Ingresa una nota mayor a 0")
            else:
                matrizNota.append(nota)
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")

sumAprobados = 0
sumReprobados = 0
matrizAprobado = [ number for number in matrizNota if number >= 4.0]

for number in matrizAprobado:
    sumAprobados += number

matrizReprobado = [number for number in matrizNota if number < 4.0]

for number in matrizReprobado:
    sumReprobados += number

print(f"La cantidad de aprobados es : {len(matrizAprobado)}\nLa cantidad de reprobados es : {len(matrizReprobado)}\n")
print(f"El promedio de los aprobados es  : {sumAprobados/ len(matrizAprobado)}")
print(f"El promedio de los reprobados es : {sumReprobados / len(matrizReprobado)}")


