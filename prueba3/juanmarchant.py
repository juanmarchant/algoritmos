import os
# Datos para probar
#['Juancito', 'Fernando', 'Manuelito','Sebastian', 'Florencio', 'Fernaflo','Barbaro','Ignacio' ], 
#['hombre','hombre','hombre','hombre','hombre','hombre','hombre','hombre'], 
# [13,13,13,13,13,13,13,13], 
# [10500, 20000, 25000,30000,50000,20000,10500,11000]
donadores = []
generado = [False]
import marchant as va

def main():
    while True:
        va.menu()
        opcion = va.validar_opcion()

        if opcion == 1:
            if generado[0] == False:
                donadores = va.ingresar_datos(generado[0])
                generado[0] = True
            else:
                while True:
                    try:
                        opcion = input("Quiere generar nuevos donadores? (s|n): ").strip().lower()
                        if opcion != 's' and opcion != 'n':
                            print("Ingrese alguna de las opciones mencionados")
                        else:
                            os.system("cls")
                            break
                    except ValueError:
                        print("Error, caracter no valido")

                if opcion == 's':
                    del donadores[:]
                    generado[0] = False
                    donadores = va.ingresar_datos(generado[0])
                    generado[0] = True

        if opcion == 2:
            if generado[0] == True:
                va.mostrar_donador(generado[0], donadores)
            else:
                print("Primero tienes que ingresar los datos, porfavor seleccione la opcion 1")
        if opcion == 3:
            if generado[0] == True:
                va.recaudacion_total(generado[0], donadores)
            else:
                print("Primero tienes que ingresar los datos, porfavor seleccione la opcion 1")    
        if opcion == 4:
            print("Muchas gracias! Juan Marchant")
            break

main()