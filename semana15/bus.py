import os
asientos = []

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
    for fila in range(len(asientos)):
        for asiento in range(len(asientos[fila])):
            if asientos[fila][asiento] == asientoSeleccionado:
                asientos[fila][asiento] = 'O'
                print("Encontrado")
                return True
            else:
                print("No encontrado")
                return False

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

    validarAsiento(asientoSeleccionado)

# pagar = validarAsiento(asientoSeleccionado)

# precio = precioAsiento(asientoSeleccionado)
# if pagar:
# print(f"""
# Compra Realizada ASIENTO {asientoSeleccionado}
# --------------------

# Total a pagar:
# """)
# else:
# print("No se pudo realizar la compra, el asiento esta ocupado\n")
        
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
        if opcion == 5:
            break

        
main()
