import marchant as va

edificio = []


def main():
    va.crearEdificio()
    while True:
        va.menu()
        opcion = va.validarOpcion()

        if opcion == 1:
            print("Comprar Edificio")
            va.comprarEdificio()
            
        if opcion ==2:
            print("***** EDIFCIO *****")
            va.mostrarEdificio()
        if opcion ==3:
            va.mostrarClientes()
            pass
        if opcion ==4:
            va.mostrarBoleta()
        if opcion == 5:
            print('Muchas gracias - Juan Marchant 7/11/2023')
            break

main()