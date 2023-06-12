import os
asientos = []
recaudado = [0]

def crearAsientos():
    fila = [] 
    for asiento in range(1,41,1):
        fila.append(asiento)
        if len(fila) == 4:
            asientos.append(fila)
            fila = []

def mostrarAsientos():
    for fila in range(len(asientos)):
        print("{:<3} {} \t\t {:<3} {}".format(asientos[fila][0],asientos[fila][1],asientos[fila][2],asientos[fila][3]))

def validarOpcion():
    while True:
        try:
            opcion = int(input("\tIngrese una opcion: "))
            if opcion > 5 or opcion < 0:
                print("Ingrese una de las opciones mencionadas (1-5)")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")

    return opcion

def validarAsiento(asientoSeleccionado): 
    valorVentana =  5000
    valorPasillo = 4000 
    for fila in range(len(asientos)):
        for asiento in range(len(asientos[fila])):
            if asientos[fila][asiento] == asientoSeleccionado:
                asientos[fila][asiento] = 0
                if asiento == 0 or asiento ==3:
                    validacion = [True, valorVentana]
                    recaudado[0] = recaudado[0] + valorVentana
                    return validacion
                else:
                    validacion = [True, valorPasillo] 
                    recaudado[0] = recaudado[0] + valorPasillo
                    return validacion
    
    return [False, 0]

def cancelarPasaje():
    mostrarAsientos()
    contador = 0
    while True:
        try:
            asientoSeleccionado = int(input("Ingrese un numero de asiento: "))
            if asientoSeleccionado > 40 or asientoSeleccionado < 1: 
                print("Porfavor seleccione uno de los asientos (1-40)")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")
    
    for fila in range(len(asientos)):
        for asiento in range(len(asientos[fila])):
            contador +=1
            if contador == asientoSeleccionado: 
                if asientos[fila][asiento] == 0:
                    asientos[fila][asiento] = contador
                    print(f"El {asientoSeleccionado} a quedado disponible nuevamente")
                    if asiento == 3 or asiento == 0:
                        recaudado[0] = recaudado[0] - 5000
                    else:
                        recaudado[0] = recaudado[0] - 4000
                    return 
                else:
                    print("El asiento seleccionado aun esta disponible")
                    return
    
def comprarPasaje():
    mostrarAsientos()

    while True:
        try:
            asientoSeleccionado = int(input("Ingrese un numero de asiento: "))
            if asientoSeleccionado > 40 or asientoSeleccionado < 1: 
                print("Porfavor seleccione uno de los asientos (1-40)")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")

    pagar = validarAsiento(asientoSeleccionado) 

    if pagar[0]:
        print(f"""
        Compra Realizada ASIENTO {asientoSeleccionado}
        --------------------

        Total a pagar: {pagar[1]}
        """) 
    else:
        print("No se pudo realizar la compra, el asiento esta ocupado\n")
    
def menu():
    print(f"""
     Vamos donde tú quieras
     *********************
1.	Mostrar asientos disponibles 	
2.	Comprar Pasaje
3.	Anular venta
4.	Total recaudado
5.	Salir
""")

def main():
    crearAsientos() 

    while True:
        menu()
        opcion = validarOpcion()
        
        if opcion == 1:
            mostrarAsientos()

        if opcion == 2:
            comprarPasaje()

        if opcion == 3:
            cancelarPasaje()

        if opcion == 4:
            print(f"El total recaudado es: {recaudado[0]}")

        if opcion == 5:
            break

        
main()
