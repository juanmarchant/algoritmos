# Se está realizando una encuesta a n estudiantes de la Escuela de informática, con el objetivo
# de conocer qué tipo de aplicaciones son de su interés para poder construir o codificar.

# El levantamiento de información a consultar es la siguiente: nombre, edad, carrera, tipo de aplicación.

# Se solicita que usted valide la información de la siguiente manera:
# • Nombre: debe permitir ingresar como mínimo 3 caracteres.
# • Edad: debe permitir ingresar una edad mínima a partir de los 17 años.
# • Carrera: debe permitir ingresar 1: analista, 2: ingeniería, 3: redes.
# • Tipo de aplicación: m: móviles, w: web, i: Iot

# A partir de esta información ingresada, determine y muestre:
# • Cantidad de estudiantes en las distintas preferencias de aplicación.
# • Promedio de edad de todos los estudiantes ingresados.
# • Cantidad de estudiantes encuestados por cada carrera.

import os

while True:
    try:
        cantidadEstudiantes = int(input("Cuantos estudiantes quiere ingresar? : "))
        if cantidadEstudiantes < 0:
            print("Ingresa una cantidad >= 1")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, caracter no valido.. recuerda ingresar la cantidad de estudiantes encuestados (>=1)")


contador = 0

contadorMoviles = 0
contadorWeb = 0
contadorIot = 0

sumaEdades = 0

contadorAnalista  = 0
contadorIngenieria = 0
contadorRedes = 0 

while contador < cantidadEstudiantes:
    contador = contador + 1 

    while True:
        try:
            nombreEstudiante = input(f"{contador}. Ingrese el nombre del estudiante: ")
            if len(nombreEstudiante) < 2: 
                print("El minimo de caracteres es de 3..")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... recuerda ingresar un nombre con minimo de 3 caracteres")

    while True:
        try:
            edadEstudiante = int(input(f"{contador}. Ingrese la edad del estudiante: "))
            if edadEstudiante < 16: 
                print("El minimo de edad es de 17 annos")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... recuerda ingresar la edad con minimo de 17 annos")

    while True:
        try:
            carreraEstudiante = int(input(f"{contador}. Ingrese la carrera del estudiante (1: analista, 2: ingeniería, 3: redes): "))
            if carreraEstudiante != 1 and carreraEstudiante != 2 and carreraEstudiante != 3: 
                print("La carrera permitidas son 1: analista, 2: ingeniería, 3: redes")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... recuerda ingresar la carrera del estudiante 1: analista, 2: ingeniería, 3: redes")
            
    while True:
        try:
            tipoAplicacionEstudiante = input(f"{contador}. Ingrese el tipo de aplicacion (w: web, m: moviles, i: Iot): ").lower()
            if tipoAplicacionEstudiante != 'w' and tipoAplicacionEstudiante != 'm' and tipoAplicacionEstudiante != 'i': 
                print("Los tipos de aplicacion permitidas son m: móviles, w: web, i: Iot")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... recuerda ingresar el tipo de aplicacio m: móviles, w: web, i: Iot ")
    
    if tipoAplicacionEstudiante == 'w':
        contadorWeb = contadorWeb + 1
    elif tipoAplicacionEstudiante == 'm':
        contadorMoviles = contadorMoviles + 1
    else:
        contadorIot = contadorIot + 1


    sumaEdades = edadEstudiante + sumaEdades

    if carreraEstudiante == 1:
        contadorAnalista = contadorAnalista + 1
    elif carreraEstudiante == 2:
        contadorIngenieria = contadorIngenieria + 1
    else:
        contadorRedes = contadorRedes + 1 

print(f"""
Tipos de aplicacion

Web -> {contadorWeb}
Moviles -> {contadorMoviles}
Iot -> {contadorIot}
""")

promedioEdad  = sumaEdades / cantidadEstudiantes
print(f"El promedio de las edades de los estudiantes es:  {promedioEdad}")


print(f"""
Estudiantes encuestados por carrera

Analista -> {contadorAnalista}
Ingenieria -> {contadorIngenieria}
Redes -> {contadorRedes}
""")

