import os 
# datos de prueba ['20286769-3', '20286769-3', '20286769-3'],['AA1122', 'AA1122', 'AA1122'],[10,20,30],[40,50,60]

taxistas = []
generado = [False] #Poner en True para ejecutar pruebas

def menu():
    print("""
    ******* RAPIDITO.com ******
    1. Ingresar datos a la matriz
    2. Mostrar
    3. Gasto total
    4. Salir
    """)

def validar_opcion():
    while True:
        try:
            opcion = int(input("\tIngresa una opcion: "))
            if opcion > 4 or opcion < 0:
                print("\tIngresa una de las opciones mencionadas(1-4)")
            else:
                os.system("cls")
                break
        except ValueError:
            print("\tError, caracter invalido")
    return opcion

def ingresar_datos():
    ruts = []
    patentes = []
    kilometros_inicio = []
    kilometros_final = []
    if generado[0] == False:
        #Ingresando rut de los taxistas
        for taxi in range(31):
            while True:
                try:
                    rut = input(f"Ingresa el ruto del taxista {taxi + 1} (xxxxxxxx-x): ").strip().upper()
                    if len(rut) < 10:
                        print("Ingresa el rut correctamente ej: 12345789-K")
                    else:
                        ruts.append(rut)
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido")

        #Ingresando las patentes de los taxistas
        for taxi in range(31):
            while True:
                try:
                    patente = input(f"Ingrese la patente del taxista {taxi + 1} (AA1122): ").strip().upper()
                    if len(patente) < 6:
                        print("Ingresa la patente correctamente ej: AA1122 ")
                    else:
                        patentes.append(patente)
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido")
        
        #Ingresando los kilometros con los que parte
        for taxi in range(31):
            while True:
                try:
                    kilometro_inicio = int(input(f"Ingrese los kilometros con los que inicia  el taxi nro {taxi + 1} (20): "))
                    if kilometro_inicio <= 0:
                        print("Ingrese los kilometros, estos son mayores a 0")
                    else:
                        kilometros_inicio.append(kilometro_inicio)
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido")

        #Ingresando los kilometros con los que finaliza el dia
        for taxi in range(31):
            while True:
                try:
                    kilometro_final = int(input(f"Ingrese los kilometros con los que finaliza  el taxi nro {taxi + 1} (20): "))
                    if kilometro_final <= 0:
                        print("Ingrese los kilometros, estos son mayores a 0")
                    else:
                        kilometros_final.append(kilometro_final)
                        os.system("cls")
                        break
                except ValueError:
                    print("Error, caracter no valido")
        taxistas.append(ruts)
        taxistas.append(patentes)
        taxistas.append(kilometros_inicio)
        taxistas.append(kilometros_final)

        generado[0] = True
    else:
        while True:
            try:
                opcion = input("Quiere generar nuevos taxistas? (s|n): ").strip().lower()
                if opcion != 's' and opcion != 'n':
                    print("Ingrese alguna de las opciones mencionados")
                else:
                    os.system("cls")
                    break
            except ValueError:
                print("Error, caracter no valido")

        if opcion == 's':
            del taxistas[:]
            generado[0] = False
            ingresar_datos()
    
def mostrar_taxistas():
    if generado[0] == True:
        num_columnas = len(taxistas[0])
        for columna in range(num_columnas):
            print(f"""
            ----- TAXISTA Nº {columna + 1} -----
            RUT: {taxistas[0][columna]}
            PATENTE: {taxistas[1][columna]}
            KILOMETROS INICIO: {taxistas[2][columna]}
            KILOMETROS FINAL: {taxistas[3][columna]}
            """)
    else:
        print("No puedes usar esta opcion si aun no haz ingresado los datos")

def gasto_total():
    if generado[0] == True:
        sum = 0
        total_km = []
        litro_bencina = 1056

        num_columnas = len(taxistas[0])
        for columna in range(num_columnas):
            viaje = taxistas[3][columna] - taxistas[2][columna] 
            if viaje < 0:
                viaje *= -1
            total_km.append(viaje)

        for numero in total_km:
            multiplicador = numero // 5 
            bencina = multiplicador * litro_bencina
            sum += bencina
        
        print(f"El gasto que realizo en duenno en bencina es: ${sum}")
    else:
        print("No puedes usar esta opcion si aun no haz ingresado los datos")




def main():
    while True:
        menu()
        opcion = validar_opcion()
        
        if opcion == 1:
            ingresar_datos()
        if opcion == 2:
            mostrar_taxistas()            
        if opcion == 3:
            gasto_total()
        if opcion == 4:
            print("Juan Marchant - Seccion XDDDD ")
            break
main()