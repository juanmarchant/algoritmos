# Se está planificando el campeonato de futbol a nivel regional de una determinada ciudad de nuestro país.

# La venta de los tickets ya se ha comenzado a realizar, por lo que se les ha
# solicitado a estudiantes de Duoc UC, que elabore programa que permita:
# • Ingresar la cantidad de tickets, validando que la cantidad sea un número positivo (mayor a cero).
# • Determine el monto a pagar por la compra de los tickets sabiendo que de acuerdo a la forma de pago (1: efectivo, 2: debito, 3: crédito),
    # se puede aplicar un descuento:
    # Efectivo: 6% de descuento al monto total.
    # Débito: 7% de descuento al monto total.
    # Crédito: si la compra de tickets es mayor a 3, se aplica un descuento del 5% al monto total; en caso contrario no aplica descuento.
# • Mostrar: monto por la compra de tickets, monto de descuentos, monto total a pagar.

import os

print("===== CAMPEONATO DE FUTBOL =====")

#valor ticket no mecionado en el texto, precio random

valorTicket = 10000
r = 's'
valorTotal = 0

while r == 's':
    while True:
        try:
            cantidadEntradas = int(input("Cuantas entradas quiere comprar?: "))
            if cantidadEntradas < 0:
                print("Ingrese una cantidad de entradas mayor a 0")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido.... porfavor ingresar una cantidad de entradas mayor a 0")

    while True:
        try:
            metodoPago = int(input("Con metodo se cancelara (1: efectivo, 2: debito, 3: crédito): "))
            if metodoPago != 1 and metodoPago != 2 and metodoPago != 3:
                print("Porfavor ingresa alguno de los metodos mostrados anteriormente")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... porfavor ingresar alguno de los metodos mencionados anteriormente")

    if metodoPago == 1: 
        valorTotal = ( valorTicket * cantidadEntradas ) * 0.94
    elif metodoPago == 2:
        valorTotal = ( valorTicket * cantidadEntradas ) * 0.93
    else:
        if cantidadEntradas > 3:
            valorTotal = ( valorTicket * cantidadEntradas ) * 0.95
        else:
            valorTotal = valorTicket * cantidadEntradas
        
    print(f"""===== MONTO =====

    El monto total a pagar es de: {valorTotal} CLP
    """)

    while True:
        try:
            r = input("Quieres ingresar otra compra?: (s/n) ").lower()
            if r != 's' and r != 'n':
                print("Ingresa alguna de las opciones mencionas (s/n)")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... porfavor ingresa alguno de los metodos mencionados anteriormente")




