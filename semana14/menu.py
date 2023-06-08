import os

trabajadores = []

def menu():
    print("""
    1. Crear Trabajador
    2. Mostrar datos trabajador(todos)
    3. Mostrar sueldo Trabajador
    4. Salir
    """)

def seleccionarOpcion():
    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion > 4 or opcion < 0:
                print("Elige una opcion válida (1-4)")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no válido")

    return opcion

def seleccionarRut():

    if len(trabajadores) == 0:
        print("No hay trabajadores, porfavor crea alguno")
    else:
        while True:
            try:
                rut = input("Ingrese el rut del trabajador: ")
                if len(rut) < 10:
                    print("Ingrese un rut válido ej (xxxxxxxx-x)")
                else :
                    os.system("cls")
                    break
            except ValueError:
                print("Error, caracter no válido") 
        return rut

def calcularBono(sueldo, puesto, annos):
    if puesto == 'OPERARIO' and annos > 5:
        bono = sueldo * 0.10
    elif puesto == 'ADMINISTRATIVO' and annos > 6:
        bono = sueldo * 0.15
    elif puesto == 'JEFE':
        bono = sueldo * 0.05
    else:
        bono = sueldo * 0.03

    return bono

def crearTrabajador():
    trabajador = []

    while True:
        try:
            nombre = input("Ingrese el nombre del trabajador: ").strip()
            if len(nombre) < 3:
                print("Ingrese un nombre con al menos 3 o más caracteres")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no válido")

    while True:
        try:
            rut = input("Ingrese el rut del trabajador: ")
            if len(rut) < 10:
                print("Ingrese un rut válido ej (xxxxxxxx-x)")
            else :
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no válido")

    while True:
        try:
            puesto = input("Ingrese el puesto del trabajador (Operario | Administrativo | Jefe): ").strip().upper()
            if puesto != 'OPERARIO' and puesto != 'ADMINISTRATIVO' and puesto != 'JEFE':
                print("Ingresa una de las opciones mencionadas (Operario | Administrativo | Jefe)")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no válido")

    while True:
        try:
            annos = int(input("Ingresa los annos de antiguedad del trabajador: "))
            if annos < 0:
                print("Ingresa un valor igual o mayor a 0")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no válido")

    while True:
        try:
            sueldo = int(input("Ingresa el sueldo del trabajador: "))
            if sueldo < 0:
                print("Ingresa un sueldo mayor o igual a 0")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no válido")

    bono = calcularBono(sueldo, puesto, annos)

    trabajador.append(nombre)
    trabajador.append(rut)
    trabajador.append(puesto)
    trabajador.append(annos)
    trabajador.append(sueldo)
    trabajador.append(bono)

    trabajadores.append(trabajador)
    print(f"Felicitaciones, haz creado exitosamente al trabajador {nombre}")

def mostrarTrabajadores():

    if len(trabajadores) == 0:
        print("No hay trabajadores, porfavor crea alguno")
    else:

        for i in range(len(trabajadores)):
            print(f""" 
            =====TRABAJADOR=====

            Nombre: {trabajadores[i][0]}
            Rut:    {trabajadores[i][1]}
            Puesto: {trabajadores[i][2]}
            Años de antiguedad: {trabajadores[i][3]}
            Sueldo bruto: {trabajadores[i][4]}
            Bono:   {trabajadores[i][5]}
            """)
        
def buscarSaldo(rut):
    for trabajador in range(len(trabajadores)):
        if rut == trabajadores[trabajador][1]:
            print(f"El sueldo del trabajador con rut {rut} es de : {trabajadores[trabajador][4]}")
    

def main():

    while True:
        menu()
        opcion = seleccionarOpcion()

        if opcion == 1:
            crearTrabajador()
        
        if opcion == 2:
            mostrarTrabajadores()
        
        if opcion == 3:
            rutTrabajador = seleccionarRut()
            buscarSaldo(rutTrabajador)
        
        if opcion == 4:
            break

main()
