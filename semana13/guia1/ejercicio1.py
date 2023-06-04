# 1.	Llene un arreglo con N números enteros generados aleatoriamente 
# (deberá usar la función random) , muestre el arreglo una vez lleno

# Ingresar, además un número entero, y mostrar:
# •	Todos los elementos del arreglo que sean divisibles por ese número
# •	Dejar en un segundo arreglo, la multiplicación de los elementos del primero por el numero ingresado.
# •	El mayor elemento de ambos arreglos
# •	Dejar en un tercer arreglo los elementos del segundo que sean divisibles por 6


import random, os 
 
while True:
    try:
        cantidadNumeros = int(input("Ingrese el tamnno de la lista: "))
        if cantidadNumeros <= 0:
            print("Ingrese un tamanno mayor a 0")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Caracter no valido")

arrayRandom = [round(random.random() * 10) for i in range(cantidadNumeros)]

print(f"Arreglo Aleatorio : {arrayRandom}")

while True:
    try:
        numeroUsuario = int(input("Ingrese un numero a evaluar: "))
        os.system("cls")
        break
    except ValueError:
        print("Caracter no valido")

for numero in arrayRandom:
    if numeroUsuario != 0 and numero % numeroUsuario == 0 :
        print(f"El numero {numero} es divisible por {numeroUsuario}")


arrayMultiplicacion = [number * numeroUsuario for number in arrayRandom]

print(f"""\n 
Multiplicacion: 
{arrayRandom} * {numeroUsuario} = {arrayMultiplicacion}
""")
 
numeroMayorPrimero = arrayRandom[0]
numeroMayorSegundo = arrayMultiplicacion[0]

for number in arrayRandom:
    if number > numeroMayorPrimero:
        numeroMayorPrimero = number

for number in arrayMultiplicacion:
    if number > numeroMayorSegundo:
        numeroMayorSegundo = number

print(f"""
El numero mayor del primer arreglo es: {numeroMayorPrimero}
\nEl numero mayor del segundo arreglo es: {numeroMayorSegundo}
""")

arrayTercero = [number for number in arrayMultiplicacion if number % 6 == 0 ]
if len(arrayTercero) > 0:
    print(f"""Tercer arreglo con numeros divisibles por 6 -> {arrayTercero}""")
else:
    print("No hay numeros divisbles por 6 ")
