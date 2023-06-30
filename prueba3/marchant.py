import os
donadores = []

def menu():
    print("""
    ******** TODO SE RECOMPONE ********
    1. Ingresar
    2. Mostrar
    3. Recaudacion Total
    4. Salir
    """)

def ingresar_datos(validacion):
    nombres = []
    generos = []
    edades = []
    donaciones = []

    if validacion == False:
        for donador in range(8):
            while True:
                try:
                    nombre=input(f"Ingrese el nombre del donador {donador+1}: ").strip()
                    if len(nombre) <= 6:
                        print("El nombre del donador tiene que ser mayor a 6 caracteres...")
                    else:
                        nombres.append(nombre)
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido")

        for donador in range(8):
            while True:
                try:
                    genero=input(f"Ingrese el genero del donador {donador + 1} (mujer/hombre): ").strip().lower()
                    if genero!= "mujer" and genero!="hombre":
                        print("El genero del donador puede ser mujer/hombre")
                    else:
                        generos.append(genero)
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido")

        for donador in range(8):
            while True:
                try:
                    edad=int(input(f"Ingrese la edad del donador {donador + 1} (mayor a 12 annos): "))
                    if edad <=12:
                        print("La edad del donador tiene que ser mayor a 12 annos")
                    else:
                        edades.append(edad)
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido")

        for donador in range(8):
            while True:
                try:
                    donacion=int(input(f"Ingrese el monto del donador {donador + 1} (mayor a $10000): "))
                    if donacion <=10000:
                        print("El monto tiene que ser mayor a $10000")
                    else:
                        donaciones.append(donacion)
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido")

        donadores.append(nombres)
        donadores.append(generos)
        donadores.append(edades)
        donadores.append(donaciones)

        return donadores

def validar_opcion():
    while True:
        try:
            opcion = int(input("\tIngrese una opcion: "))
            if opcion < 1 or opcion > 4:
                print("Porfavor, ingrese una de las opciones mencionadas(1-4)")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")
    return opcion


def mostrar_donador(validacion, donadores):
    if validacion == True:
        nro_columnas = len(donadores[0])
        valores = []

        for columna in range(nro_columnas):
            valores.append(donadores[3][columna])

        #Calculando el mayor
        numero_mayor = valores[0]
        for numero in valores:
            if numero > numero_mayor:
                numero_mayor = numero

        #Mostrando el nombre
        for numero in range(len(valores)):
            if donadores[3][numero] == numero_mayor:
                print(f"{donadores[0][numero]} fue quien dono mas, siendo un monto de: ${numero_mayor}")
    else:
        print("Primero tienes que ingresar los datos, porfavor seleccione la opcion 1")

def recaudacion_total(validacion, donadores):
    if validacion == True:
        sum = 0
        nro_columnas = len(donadores[0])
        valores = []
        for columna in range(nro_columnas):
            valores.append(donadores[3][columna])

        for numero in valores:
            sum += numero
        print(f"La recaudacion total del evento es ${sum}")
    else:
        print("Primero tienes que ingresar los datos, porfavor seleccione la opcion 1")