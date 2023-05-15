import os
#revisado 11:30

# Cantidades Juegos
cantidadDarkest = 0
cantidadDiablo = 0
cantidadDisco = 0
cantidadDivinity = 0

# Precios Juegos
precioDarkest =  60000
precioDiablo = 48000
precioDisco = 80000
precioDivinity = 75500

#Plata GENERAL
totalPagar = 0
totalDiscoElysium = 0 
recaudado5K = 0


agregarJuego ='s'
seguirVentas = 's'
while seguirVentas =='s':
    while True:
        try:
            cliente = int(input("Ingrese el id del cliente: (Max: 2 caracteres | ex: XX): "))
            if cliente < 1:
                print("Error, ingrese el id del cliente nuevamente (numero positivo) ..ex: XX -> 12")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no validos... intentelo nuevamente | ex: XX -> 12")

    seguirComprando = 's'
    while seguirComprando == 's':
        print(f"""
        ******** Cliente N° {cliente} El Secreto del abismo ********
        ===========================================================

        [1] -> Darkest Dungeon 
        [2] -> Diablo II Resurrected
        [3] -> Disco Elysium
        [4] -> Divinity: Original Sin II
        [5] -> Salir
        """)

        while True:
            try:
                op = int(input("\t\tElija Opcion: "))
                if op < 1 or op > 5:
                    print("Error, Elija una de las opcion mencionadas (1-5)")
                else:
                    os.system("cls")
                    break 
            except ValueError:
                print("Error, caracter no valido.. Recuerda ingresar una de las opcion mencionadas (1-5 )")

        if op == 1:

            while True:
                try:
                    cantidadDarkest = int(input("A seleccionado Darkest Dungeon.. cuantos desea adquirir ?: "))
                    if cantidadDarkest < 1:
                        print("Error, Elija una opcion mayor a 0")
                    else:
                        os.system("cls")
                        break 
                except ValueError:
                    print("Error, caracter no valido.. Recuerda ingresar una cantidad mayor a 0")
            
            while True:
                try:
                    opcion5K = input("El juego es 5k? (s/n) : ").lower()
                    if opcion5K != 's' and opcion5K != 'n':
                        print("Error, recuerda ingresar una de las opciones mencionadas (s/n)")
                    else:
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido.... porfavor ingresa una de las opciones mencionadas (s/n)")

            if opcion5K == 's':
                precioDarkest += 7000
                recaudado5K += precioDarkest * cantidadDarkest
            
            totalPagar = (precioDarkest * cantidadDarkest) + totalPagar
            precioDarkest = 60000

        if op == 2:
            while True:
                try:
                    cantidadDiablo = int(input("A seleccionado Diablo II Resurrected.. cuantos desea adquirir ?: "))
                    if cantidadDiablo < 1:
                        print("Error, Elija una opcion mayor a 0")
                    else:
                        os.system("cls")
                        break 
                except ValueError:
                    print("Error, caracter no valido.. Recuerda ingresar una cantidad mayor a 0")
            
            while True:
                try:
                    opcion5K = input("El juego es 5k? (s/n) : ").lower()
                    if opcion5K != 's' and opcion5K != 'n':
                        print("Error, recuerda ingresar una de las opciones mencionadas (s/n)")
                    else:
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido.... porfavor ingresa una de las opciones mencionadas (s/n)")

            if opcion5K == 's':
                precioDiablo += 7000
                recaudado5K += precioDiablo * cantidadDiablo

            totalPagar = (precioDiablo * cantidadDiablo) + totalPagar
            precioDiablo = 48000

        if op == 3:
            while True:
                try:
                    cantidadDisco = int(input("A seleccionado Disco Elysium.. cuantos desea adquirir ?: "))
                    if cantidadDisco < 1:
                        print("Error, Elija una opcion mayor a 0")
                    else:
                        os.system("cls")
                        break 
                except ValueError:
                    print("Error, caracter no valido.. Recuerda ingresar una cantidad mayor a 0")
            
            while True:
                try:
                    opcion5K = input("El juego es 5k? (s/n) : ").lower()
                    if opcion5K != 's' and opcion5K != 'n':
                        print("Error, recuerda ingresar una de las opciones mencionadas (s/n)")
                    else:
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido.... porfavor ingresa una de las opciones mencionadas (s/n)")

            if opcion5K == 's':
                precioDisco += 7000
                recaudado5K += precioDisco * cantidadDisco

            totalPagar = (precioDisco * cantidadDisco) + totalPagar
            precioDisco = 80000
            totalDiscoElysium += cantidadDisco

        if op == 4:
            while True:
                try:
                    cantidadDivinity = int(input("A seleccionado Divinity: Original Sin II.. cuantos desea adquirir ?: "))
                    if cantidadDivinity < 1:
                        print("Error, Elija una opcion mayor a 0")
                    else:
                        os.system("cls")
                        break 
                except ValueError:
                    print("Error, caracter no valido.. Recuerda ingresar una cantidad mayor a 0")
            
            while True:
                try:
                    opcion5K = input("El juego es 5k? (s/n) : ").lower()
                    if opcion5K != 's' and opcion5K != 'n':
                        print("Error, recuerda ingresar una de las opciones mencionadas (s/n)")
                    else:
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido.... porfavor ingresa una de las opciones mencionadas (s/n)")

            if opcion5K == 's':
                precioDivinity += 7000
                recaudado5K += precioDivinity * cantidadDivinity

            totalPagar = (precioDivinity * cantidadDivinity) + totalPagar
            precioDiablo = 75500
    
        if op == 5:
            print(f"""
            ===== SESION FINALIZADA =====
            *****************************

            Se han vendido {totalDiscoElysium} Disco Elysium
            -
            Se ha recaudado {recaudado5K} con los juegos 5K

            """)
            seguirVentas = False
            agregarJuego = False
            seguirComprando = False
            
        while agregarJuego == 's':
            try:
                seguirComprando = input("Desea agregar otro tipo de juego? (s/n): ").lower()
                if seguirComprando != 's' and seguirComprando != 'n':
                    print("Error, recuerda ingresar una de las opciones mencionadas (s/n)")
                else:
                    os.system("cls")
                    break
            except ValueError:
                print("Error, caracter no valido.... porfavor ingresa una de las opciones mencionadas (s/n)")

        if seguirComprando == 'n':
            print(f""" 
            EL cliente N° {cliente} BOLETA:
            =============================

            TOTAL: {totalPagar}
            """)
            totalPagar = 0
