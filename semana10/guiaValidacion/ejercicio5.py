
# Una nave intergaláctica, está planificando viajes para el nuevo planeta Orión que se ha encontrado.

# El nuevo planeta presenta muchas de las características similares a la tierra en
# cuanto a clima, atmósfera, flora y fauna. Por tal motivo, se le ha solicitado a usted que elabore un programa que permita:
# • Ingresar nombre de la persona y cantidad de pasajes a comprar
# • Validar que el nombre tenga como mínimo 3 caracteres y la cantidad sea mayor a cero.

# Teniendo en cuenta esta información, determine y muestre:
# • Monto por pagar de cada persona, sabiendo que el valor de un pasaje corresponde a 2 criptomonedas de orión.
# Una criptomoneda de orión corresponde al equivalente de 10.000 dólares.

# • Si una persona adquiere más de 2 pasajes, se realiza un 50% de descuento al valor de uno de los pasajes adquiridos.
# • Mostrar el monto en dólares equivalente al descuento en caso de que hubiera.
# • Mostrar el monto en dólares a pagar por cada usuario.
# • Mostrar el monto total a pagar en su equivalente a pesos (moneda nacional).

# Considere que el valor del dólar cambia todos los días, por lo tanto, es un valor que se ingresa.
# Y recuerde que todo lo que se ingresa, se debe validar.

import os, math

while True:
    try:
        valorUSD = float(input("Ingresar valor del dolar (Chile) (ex: 790.68): "))
        if valorUSD < 0:
            print("El valor del dolar no puede ser negativo ")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, valor no valido... recuerda ingresar el valor del dolar *positivo*")

r = 's'
orionEntradaCRYPTO =  20000

while r == 's':
    
    while True:
        try:
            nombreCliente = input("Ingrese el nombre de el cliente: ")
            if len(nombreCliente) < 3:
                print("El nombre de el cliente debe ser de 3 caracteres minimo...")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... ingrese un nombre de minimo 3 caracteres")

    while True:
        try:
            cantidadEntradas = int(input("Ingrese la cantidad de entradas: "))
            if cantidadEntradas < 0:
                print("Ingresa una cantidad postiva.... (ex: entradas >= 1)")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... ingrese la cantidad de entradas")

    if cantidadEntradas == 1:
        valorEntradasTotal = orionEntradaCRYPTO * 2 
    else:
        if cantidadEntradas > 2:
            valorEntradasTotal = (cantidadEntradas - 1) * orionEntradaCRYPTO + (orionEntradaCRYPTO * 0.5)
        else:
            valorEntradasTotal = orionEntradaCRYPTO * 2
    
    if cantidadEntradas > 2:
        print(f"""
        -Se realizo la compra de {cantidadEntradas} entrada/s-
    
        Valor a pagar + dscto incluido = {valorEntradasTotal} USD
        
        Valor a pagar en CLP = {round(valorEntradasTotal * valorUSD)} CLP
        """)
    else:
        print(f"""
        -Se realizo la compra de {cantidadEntradas} entrada/s-
    
        Valor a pagar = {valorEntradasTotal} USD 
        Valor a pagar en CLP = {round(valorEntradasTotal * valorUSD)} CLP
        """)
    
    while True:
        try:
            r = input("Quiere volver a ingresar a otro cliente? (s/n): ").lower()
            if r != 's' and r != 'n':
                print("Ingresa alguna de las opciones mencionas (s/n)")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido... ingresa alguna de las opciones mencionadas s/n")

