# Usted elabore un programa en Python que solicite para n vecinos (donde n es
# una cantidad ingresada por el usuario) la siguiente información y permita validar:

# • Nombre: debe permitir ingresar como mínimo 3 caracteres.
# • Genero: debe permitir ingresar mujer, hombre, otro género.
# • Edad: debe permitir ingresar una edad mínima de 60 años.
# • Lugar de viaje: debe permitir ingresar 1:la serena, 2: Villarrica, 3: Termas de Chillán

# A partir de la información ingresada, determine y muestre:
# • Cantidad de preferencia por cada lugar de viaje.
# • Promedio de edad de los hombres
# • Promedio de edad de las mujeres
# • Promedio de edad de otros géneros.

import os

while True:
    try:
        cantidadPersonas = int(input("Cuantas perso-nas quiere ingresar?: "))
        if cantidadPersonas < 0:
            print("Porfavor ingresar una cantidad postiva.. ex: personas > 0")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, caracter no valido... porfavor ingrese la cantidad de personas")

contador = 0


sumaHombres = 0
sumaMujeres = 0
sumaOtro = 0 

contadorHombres = 0
contadorMujeres = 0 
contadorOtro = 0

contadorLaSerena  = 0
contadorVillarica = 0
contadorTermas = 0

while contador < cantidadPersonas:
    contador = contador + 1
    
    while True:
        try:
            nombreVecino = input(f"{contador}. Ingrese el nombre del vecino: ")
            if len(nombreVecino) < 2: 
                print("El minimo de caracteres es de 3..")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... recuerda ingresar un nombre con minimo de 3 caracteres")
    
    while True:
        try:
            generoVecino = input(f"{contador}. ingrese el genero del vecino (m: mujer, h: hombre, o: otro): ").lower()
            if generoVecino != 'm' and generoVecino != 'h' and generoVecino != 'o': 
                print("recuerda seleccionar alguna de las opciones ya mencionadas... m, h , o")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... recuerda ingresar alguna de las opciones mencionadas")
    
    while True:
        try:
            edadVecino = int(input(f"{contador}. ingrese la edad del vecino: "))
            if edadVecino < 59: 
                print("La edad minima es de 60 annos")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... recuerda ingresar una edad minima de 60")

    while True:
        try:
            lugarVecino = int(input(f"{contador}. ingrese el lugar de viaje del vecino (1: la serena, 2: Villarica, 3: Termas de chillan): "))
            if lugarVecino != 1 and lugarVecino != 2 and lugarVecino != 3 : 
                print("Recuerda ingresar alguna de las opciones mencionadas...")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... recuerda ingresar alguna de las opciones mencionadas")



    if lugarVecino == 1:
        contadorLaSerena = contadorLaSerena + 1

    if lugarVecino == 2:
        contadorVillarica = contadorVillarica + 1 

    if lugarVecino == 3:
        contadorTermas = contadorTermas + 1

    
    if generoVecino == 'm':
        contadorMujeres = contadorMujeres + 1
        sumaMujeres = edadVecino + sumaMujeres
    elif generoVecino == 'h':
        contadorHombres = contadorHombres + 1
        sumaHombres = edadVecino + sumaHombres
    else:
        contadorOtro = contadorOtro + 1
        sumaOtro = edadVecino + sumaOtro

print(f"""
===== Preferencias de viaje =====

La serena -> {contadorLaSerena}
Villarica -> {contadorVillarica}
Termas de Chillan -> {contadorTermas}

""")



if contadorHombres != 0:
    promedioEdadHombres = sumaHombres / contadorHombres
    print(f"El promedio de la edad de los hombres es: {promedioEdadHombres}")
else:
    print("No se ingresaron vecinos Hombres")

if contadorMujeres != 0:
    promedioEdadMujeres = sumaMujeres / contadorMujeres
    print(f"El promedio de la edad de las mujeres es: {promedioEdadMujeres}")
else:
    print("No se ingresaron vecinas Mujeres")

if contadorOtro != 0:
    promedioEdadOtros = sumaOtro / contadorOtro
    print(f"El promedio de la edad de los Otros es: {promedioEdadOtros}")
else:
    print("No se ingresaron vecinos Otros")
