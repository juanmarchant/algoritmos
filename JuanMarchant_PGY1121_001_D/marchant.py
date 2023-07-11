import os

edificio = []
clientes = []
cantidadA = [0]
cantidadB = [0]
cantidadC = [0]
cantidadD = [0]
totalCompraA = [0]
totalCompraB = [0]
totalCompraC = [0]
totalCompraD = [0]

clientes = []

def menu():
    print("""
1. Comprar departamento 
2. Mostrar departamentos disponibles 
3. Ver listado de compradores 
4. Mostrar ganancias totales 
5. Salir
""")
    
def validarOpcion():

    while True:
        try:
            opcion = int(input('\tIngrese una opcion: '))
            if opcion  > 5 or opcion < 1:
                print('Opcion no valida, porfavor seleccione una de las mencionadas')
            else:
                os.system('cls')
                return opcion
        except ValueError:
            print('Error, caracter no valido')

def crearEdificio():
    for piso in range(10, 0, -1):
        pasillo = []
        for fila in range(4):
            suelo = ''
            pasillo.append(suelo)
        edificio.append(pasillo)

def mostrarEdificio():
    contador =  10
    print("Piso\t     Tipo")
    print("\t A  B  C  D")
    for fila in range(len(edificio)-1, -1 , -1):
        print("{}\t| {} | {} | {} | {} |".format(contador,edificio[fila][0],edificio[fila][1],edificio[fila][2],edificio[fila][3]))
        contador -=1

def comprarEdificio():
    while True:
        try:
            rut = int(input("Ingresa tu rut sin puntos ni guion: "))
            if len(str(rut)) < 8: 
                print("Ingrese el rut correctamente")
            else:
                break
        except ValueError:
            print("Error, caracter no valido")

    while True:
        try:
            piso_departamento = int(input("Ingrese el piso que desea: "))
            if piso_departamento > 10 or piso_departamento <1:
                print("Porfavor escoga entre el piso 10-1")
            else:
                break
        except ValueError:
            print("Error, caracter no valido")
    
    while True:
        try:
            tipo_departamento = input(f"Escoga un tipo de departamento para el piso {piso_departamento} -> A B C D: ").strip().upper()
            if tipo_departamento != 'A' and tipo_departamento != 'B' and tipo_departamento != 'C' and tipo_departamento != 'D':
                print("Porfavor elija un tipo de departamento, ya sea A B C o D")
            else:
                break
        except ValueError:
            print("Error, caracter no valido")

    validarDepartamento(piso_departamento, tipo_departamento,rut)       
        
def validarDepartamento(piso_departamento, tipo_departamento,rut):
    # A = 0
    # B = 1
    # C = 2
    # D = 3
    for pasillo in range(len(edificio)):
        if pasillo+1 == piso_departamento:
            for departamento in range(len(edificio[pasillo])):
                if departamento == 0 and tipo_departamento == 'A':
                    if edificio[pasillo][departamento] == '':
                        print(f"Piso Disponible {piso_departamento} - {tipo_departamento}")
                        edificio[pasillo][departamento] = 'x'
                        cantidadA[0] += 1
                        totalCompraA[0] += 3800
                        print("Pagar - 3800")
                        clientes.append(rut)
                        break
                    else:
                        print("Piso no disponible, porfavor elija otro")
                        break
                if departamento == 1 and tipo_departamento == 'B':
                    if edificio[pasillo][departamento] == '':
                        print(f"Piso Disponible {piso_departamento} - {tipo_departamento}")
                        edificio[pasillo][departamento] = 'x'
                        cantidadB[0] +=1
                        totalCompraB[0] += 3000
                        print("Pagar - 3000")
                        clientes.append(rut)
                        break
                    else:
                        print("Piso no disponible, porfavor elija otro")
                        break
                if departamento == 2 and tipo_departamento == 'C':
                    if edificio[pasillo][departamento] == '':
                        print(f"Piso Disponible {piso_departamento} - {tipo_departamento}")
                        edificio[pasillo][departamento] = 'x'
                        cantidadC[0] +=1
                        totalCompraC[0] += 2800
                        print("Pagar - 2800")
                        clientes.append(rut)
                        break
                    else:
                        print("Piso no disponible, porfavor elija otro")
                        break
                if departamento == 3 and tipo_departamento == 'D':
                    if edificio[pasillo][departamento] == '':
                        print(f"Piso Disponible {piso_departamento} - {tipo_departamento}")
                        edificio[pasillo][departamento] = 'x'
                        cantidadD[0] +=1
                        totalCompraD[0] += 3500
                        print("Pagar - 3500")
                        clientes.append(rut)
                        break
                    else:
                        print("Piso no disponible, porfavor elija otro")
                        break
    

def mostrarBoleta():
    totalCantidad = cantidadA[0] + cantidadB[0] + cantidadC[0] + cantidadD[0]
    totalCompra = totalCompraA[0] + totalCompraB[0] + totalCompraC[0] + totalCompraD[0]
    print(f"""
    Tipo Departamento| Cantidad | Total
    Tipo A 3800 UF   | {cantidadA[0]}        | {totalCompraA[0]}
    Tipo B 2800 UF   | {cantidadB[0]}        | {totalCompraB[0]}
    Tipo C 3000 UF   | {cantidadC[0]}        | {totalCompraC[0]}
    Tipo D 3500 UF   | {cantidadD[0]}        | {totalCompraD[0]}
    -------------------------------------
    TOTAL            | {totalCantidad}        | {totalCompra}
    """)

def mostrarClientes():
    if len(clientes) == 0:
        print("No se han ingresado clientes, porfavor ingrese alguna compra (Opcion 1)")
    else:
        print("*****Lista Compradores*****")
        clientes.sort()
        contador = 1
        for cliente in clientes:
            print(f"{contador}.- {cliente}")
            contador +=1