# Pediremos los id (números) de alumnos de dos clases (n), álgebra y análisis.
# Queremos mostrar todos los alumnos comunes en las dos asignaturas.
# Estos alumnos se guarden en un tercer arreglo y que sea el que se muestre.
# También indica el numero de alumnos que se repiten.



import os



alumAlgebra = []
alumAnalisis = []

while True:
    try:
        cantidadAlumno = int(input("Ingrese la cantidad de alumnos: "))
        if cantidadAlumno <=0:
            print("Ingrese un valor mayor a 0")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, caracter no valido")


for alumno in range(cantidadAlumno):
    while True:
        try:
            idAlumno = int(input("(CLASE ALGEBRA) Ingrese el id del alumno: "))
            if idAlumno < 0:
                print("Ingrese el id del alumno correctamente")
            else:
                #alumno se agrega
                alumAlgebra.append(idAlumno)

                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")


for alumno in range(cantidadAlumno):
    while True:
        try:
            idAlumno = int(input("(CLASE ANALISIS) Ingrese el id del alumno: "))
            if idAlumno < 0:
                print("Ingrese el id del alumno correctamente")
            else:
                #alumno se agrega
                alumAnalisis.append(idAlumno)
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")


alumRepetidos =  [ alumAlgebra[i] for i in range(cantidadAlumno) for j in range(cantidadAlumno) if alumAlgebra[i] == alumAnalisis[j]]

print(f"Los alumnos repetidos son: {alumRepetidos} un total de {len(alumRepetidos)} repetidos")
