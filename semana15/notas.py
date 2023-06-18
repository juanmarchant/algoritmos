"""Modulos para usar cls y random"""
import os
import random

generado = [False]
estudiantes = []

promedios = [False]
estudiantesAprobados = []
estudiantesReprobados = []


def seleccionarOpcion():
    """Esta funcion validara nuestra opcion en nuestro menu"""
    while True:
        try:
            opcion = int(input("\tElija Opción: "))
            if opcion > 5 or opcion < 0:            
                print("\tIngrese alguna de las opciones mencionadas")
            elif opcion != 1 and generado[0] == False and opcion !=5:
                print("\tPrimero genere los alumnos")
            else:
                os.system("cls")
                break
        except ValueError:
            print("\tError, caracter no valido")
    return opcion

def mostrarNotas():
    """Mostrar las notas de los alumnos"""
    for nota in range(len(estudiantes)): 
        print(f"""
        Estudiante {nota+1}
        \tCalificación 1: {estudiantes[nota][0]}
        \tCalificación 2: {estudiantes[nota][1]}
        \tCalificación 3: {estudiantes[nota][2]}
        \tCalificación 4: {estudiantes[nota][3]}
        \tPromedio obtenido: {(estudiantes[nota][0] + estudiantes[nota][1] + estudiantes[nota][2] + estudiantes[nota][3] )/ 4:0.1f}
        """)

def mostrarAprobadosReprobados():
    if promedios[0] == False:
        for nota in range(len(estudiantes)):
            promedio =  (estudiantes[nota][0] + estudiantes[nota][1] + estudiantes[nota][2] + estudiantes[nota][3] ) / 4
            promedio = round(promedio,1) 
            if promedio >= 4.0:
                estudiantesAprobados.append(promedio)
            else:
                estudiantesReprobados.append(promedio)

        print(f"""
        Estudiantes Aprobados: {len(estudiantesAprobados)}
        Estudiantes Reprobados: {len(estudiantesReprobados)}
        """)
        promedios[0] = True
    else:
        print(f"""
        Estudiantes Aprobados: {len(estudiantesAprobados)}
        Estudiantes Reprobados: {len(estudiantesReprobados)}
        """)

def promediomayormenor():
    """ Esta funcion calculara el promedio mayor y menor"""
    promediototal = []
    sumatoria = 0
    for estudiante in range(len(estudiantes)):
        for nota in range(len(estudiantes[estudiante])):
            sumatoria += estudiantes[estudiante][nota]
            if nota == 3:
                promedio =  sumatoria / 4
                promedio = round(promedio, 1)
                promediototal.append(promedio)
                sumatoria = 0

    for nota in range(len(promediototal)):
        if nota == 0:
            promedioMayor = promediototal[0]
            promedioMenor = promediototal[0]

        if promediototal[nota] > promedioMayor:
            promedioMayor = promediototal[nota]

        if promediototal[nota] < promedioMenor:
            promedioMenor = promediototal[nota]

    print(f"""
    El promedio mayor es: {promedioMayor}
    El promedio menor es: {promedioMenor}
    """)

def generarAlumnos():
    if generado[0] == False:
        while True:
            try:
                cantidadAlumnos = int(input("Ingrese la cantidad de alumnos: "))
                if cantidadAlumnos <= 0:
                    print("Ingrese un cantidad mayor a 0")
                else:
                    os.system("cls")
                    break
            except ValueError:
                print("Error, caracter no valido")
        #[t1, nt2, nt3, nt4]
        calificaciones = []
        for estudiante in range(cantidadAlumnos): 
            for i in range(4):
                nota = random.uniform(1.0, 7.0)
                nota = round(nota,1)

                calificaciones.append(nota)
                if len(calificaciones) == 4:
                    estudiantes.append(calificaciones)
                    calificaciones = []
        generado[0] = True
    else:
        while True:
            try:
                opcion = input("Quiere generar nuevos estudiantes? (s|n): ").strip().lower()
                if opcion != 's' and opcion != 'n':
                    print("Ingrese alguna de las opciones mencionados")
                else:
                    os.system("cls")
                    break
            except ValueError:
                print("Error, caracter no valido")

        if opcion == 's':
            del estudiantes[:]
            del estudiantesAprobados[:]
            del estudiantesReprobados[:]
            promedios[0] = False
            generado[0] = False
            generarAlumnos()


def menu():
    """ Funcion que imprimira el menu"""
    print("""
    ******* Matemáticas ******
    1. Generar
    2. Mostrar cada nota y el promedio obtenido por cada estudiante
    3. Cantidad de estudiantes que hayan aprobado y reprobado
    4. Promedio más alto y promedio más bajo obtenido en la asignatura
    5. Salir
    """)

def main():
    """Esta es la funcion main, donde todas las funciones son llamadas"""
    while True:
        menu()
        opcion = seleccionarOpcion()
        if opcion == 1:
            generarAlumnos()
        if opcion == 2:
            mostrarNotas()
        if opcion == 3:
            mostrarAprobadosReprobados()
        if opcion == 4:
            promediomayormenor()
        if opcion == 5:
            break

main()
