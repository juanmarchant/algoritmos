# La empresa "Dulce chupetin" necesita un programa en python que maneje el ingreso de datos de sus n trabajadores
# Para esto se deben utilizar arreglos. Los datos que se piden ingresar son:
# Nombre trabajador, rut trabajador, horastrabajadas, valor hora, horas extras.
# Se pide llenar los arreglos, una vez llenos mostrar:

# a)Nombre, rut y sueldo de cada trabajador (el sueldo se calcula: horas trabajadas* valor hora+ (horas extra* valorhora extra)
# el valor hora extra es el 50% mas del valor hora normal
# b)Nombre y rut del trabajador con mayor sueldo
# c)Total de dinero que paga la empresa a sus trabajadores
# d)Nombre y rut de quien gana el mayor sueldo

import os

while True:
    try:
        cantidadTrabajadores = int(input("Ingrese la cantidad de trabajadores: "))
        if cantidadTrabajadores <= 0:
            print("Ingresa un valor mayor a 0")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, caracter no valido")

listaTrabajadores =[]
trabajadorRegistro = []

for trabajador in range(cantidadTrabajadores):
    
    while True:
        try:
            nombre =  input("Ingrese el nombre del trabajador: ").strip()
            if len(nombre) < 3 :
                print("Ingrese un nombre con una longitud de 3 o mas caracteres")
            else:
                os.system("cls")
                #Nombre agregado
                trabajadorRegistro.append(nombre)
                break
        except ValueError:
            print("Error, Caracter no valido")

    while True:
        try:
            rut = input("Ingrese el rut del trabajador (xxxxxxxx-x): ").strip()
            if len(rut) < 10:
                print("Ingresa el rut correctamente")
            else:
                os.system("cls")
                #Rut agregado
                trabajadorRegistro.append(rut)
                break
        except ValueError:
            print("Error, caracter no valido")


    while True:
        try:
            horastrabajadas = int(input("Ingrese las horas trabajadas: "))
            if horastrabajadas < 0:
                print("Ingrese un valor igual o mayor a 0")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")
        
    while True:
        try:
            valorHoraNormal = int(input("Ingrese el valor de las horas: "))
            if valorHoraNormal <= 0:
                print("Ingrese un valor mayor a 0")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")
    
    while True:
        try:
            horasExtra = int(input("Ingrese las horas extras trabajadas: "))
            if horasExtra < 0:
                print("Ingrese un valor igual o mayor a 0")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")
        
    valorHoraExtra = valorHoraNormal * 1.50
    sueldo = valorHoraNormal * horastrabajadas + (valorHoraExtra * horasExtra)
    trabajadorRegistro.append(sueldo)
    listaTrabajadores.append(trabajadorRegistro)
    trabajadorRegistro = []


totalPagoEmpresa = 0
sueldos = []

for trabajador in listaTrabajadores:
    totalPagoEmpresa += trabajador[2]
    sueldos.append(trabajador[2])

sueldoMayor = sueldos[0]
indice = 0
for i, sueldo in enumerate(sueldos):
    if i == 0:
        indice = i
    else:
        if sueldo > sueldoMayor:
            sueldoMayor = sueldo
            indice = i

for trabajador in range(len(listaTrabajadores)):
    print(f"""
    -----Trabajador-----
    Nombre: {listaTrabajadores[trabajador][0]}
    Rut: {listaTrabajadores[trabajador][1]}
    Sueldo: {listaTrabajadores[trabajador][2]}
    """)

print(f"""\n
------Trabajador con sueldo mayor-----
Nombre: {listaTrabajadores[indice][0]}
Rut: {listaTrabajadores[indice][1]}
Sueldo: {sueldoMayor}
""")
print(f"El total de los pagos es: ${totalPagoEmpresa} CLP")

