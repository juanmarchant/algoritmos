while True:
    try:
        cantidadVehiculos =  int(input("Ingrese la cantidad de vehiculos: "))
        if cantidadVehiculos < 0:
            print("Ingrese una cantidad positiva")
        else:
            break
    except ValueError:
        print("Error, ingresaste un valor erroneo")

contadorVehiculosMujer_2005 = 0
totalMotos_1999_2001 = 0
totalVehiculosHombres = 0
totalPeaje = 0 

vehiculoMayor = ""
edadConductorMayor = 0
generoConductorMayor = ""

contadorVehiculosMujer_2005 = 0 
totalMotos_1999_2001 = 0
totalVehiculosHombres = 0
sumaTotalHombresAutomoviles_34 = 0
sumaEdadesHombresCamionetas = 0
contadorHombresCamionetas = 0

contador = 0 

while contador < cantidadVehiculos:
    while True:
        try:
            patente = input("Ingrese la patente (AAAAAA - BBBBB): ")
            if len(patente) < 5 or len(patente) > 6:
                print("Ingrese una patente correcta (AAAAAA - BBBBB)")
            else:
                break
        except ValueError:
            print("Error, haz ingresado un valor error...")
    
    while True:
        try: 
            tipoV = input("Tipo de Vehículo (A: Automóvil, C: Camioneta, M: Moto) : ").upper()
            if tipoV != 'A' and tipoV != 'C' and tipoV != 'M' :
                print("Ingrese alguna de las opciones mencionadas (A: Automóvil, C: Camioneta, M: Moto)")
            else:
                break
        except ValueError:
            print("Error, haz ingresado un valor error...")

    while True:
        try:
            annoV = int(input("Ingrese el anno del vehiculo (1980-2006): "))
            if annoV < 1980 or annoV > 2006:
                print("Recuerda que solo puedes ingresar vehiculos del anno 1980-2006")
            else:
                break
        except ValueError:
            print("Error, haz ingresado un valor error...")

    while True: 
        try:
            generoConductor = input("Sexo delconductor (F: Femenino o M: Masculino)").upper()
            if generoConductor != 'F' and generoConductor != 'M':
                print("Recuerda ingresar alguna de las opciones (F: Femenino o M: Masculino)")
            else:
                break
        except ValueError:
            print("Error, haz ingresado un valor error...")
            
    while True:
        try:
            edadConductor = int(input("Ingrese la edad del conductor +18: "))
            if edadConductor < 18 or edadConductor < 0:
                print("Recuerda ingresar correcta, mayor o igual a 18 annos")
            else:
                break
        except ValueError:
            print("Error, haz ingresado un valor error...")

    if tipoV == 'A':
        if annoV > 1998:
            print("Valor Peaje: 1000")
            totalPeaje = totalPeaje + 1000
        if annoV <= 1998:
            print("Valor Peaje: 800")
            totalPeaje = totalPeaje + 800
    
    if tipoV == 'C':
        if annoV > 1998:
            print("Valor Peaje: 1200")
            totalPeaje = totalPeaje + 1200
        if annoV <= 1998:
            print("Valor Peaje: 1000")
            totalPeaje = totalPeaje + 1000

    if tipoV == 'M':
        if annoV > 1998:
            print("Valor Peaje: 600")
            totalPeaje = totalPeaje + 600
        if annoV <= 1998:
            print("Valor Peaje: 400")
            totalPeaje = totalPeaje + 400

    if tipoV == 'C' and generoConductor == 'F':
        contadorVehiculosMujer_2005 = contadorVehiculosMujer_2005 + 1
        
    if tipoV == 'M' and (annoV >= 1999 and annoV <= 2001):
        totalMotos_1999_2001 = totalMotos_1999_2001 + 1


    if generoConductor == 'M':
        totalVehiculosHombres = totalVehiculosHombres + 1
    
    if contador == 0:
        vehiculoMayor, edadConductorMayor, generoConductorMayor = tipoV, edadConductor, generoConductor
    else:
        if edadConductor > edadConductorMayor:
            vehiculoMayor, edadConductorMayor, generoConductorMayor = tipoV, edadConductor, generoConductor

    if generoConductor == 'M' and tipoV == 'C':
        sumaEdadesHombresCamionetas =  sumaEdadesHombresCamionetas + edadConductor
        contadorHombresCamionetas =  contadorHombresCamionetas + 1

    if tipoV == 'A' and generoConductor == 'M' and edadConductor < 34:
        if annoV > 1998:
            sumaTotalHombresAutomoviles_34 = sumaTotalHombresAutomoviles_34 + 1000 
        if annoV <= 1998:
            sumaTotalHombresAutomoviles_34 = sumaTotalHombresAutomoviles_34 + 800
    
    contador = contador +1

print(f"El total recaudado fue: {totalPeaje}")

print(f"""La persona mayor
Tipo Vehículo: {vehiculoMayor}
Edad : {edadConductorMayor}
Genero : {generoConductorMayor}
""")

if contadorHombresCamionetas != 0:
    promedioHombresCamionetas = sumaEdadesHombresCamionetas / contadorHombresCamionetas
    print(f"El promedio de las edades de los hombres que manejan camioneta es : {promedioHombresCamionetas}")
else:
    print("No se ingresaron hombres que conducen camionetas")

print(f"La suma total de los automoviles conducidos por hombre y una edad menor a 34 es: {sumaTotalHombresAutomoviles_34}")
