# Realizar un programa que permita simular una calculadora básica,
# 1. Suma, 2. resta, 3. multiplicación, 4.división. 5. Salir
# En cada caso se deberán ingresar dos números para realizar las operaciones.
# Recordar que la división por cero no se debe realizar

while True:
    print("""===== CALCULADORA =====

        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division
        5. Salir

    """)

    opcion = int(input("Ingrese una opcion: "))
    contador = 0

    if opcion == 1:
        
        r1 = 's'
        while r1 == 's':

            suma = 0

            while contador < 2:
                contador = contador + 1 

                if contador == 1:
                    numero = int(input("Ingrese el primer numero: "))
                    suma = numero
                else:
                    numero = int(input("Ingrese el segundo numero: "))
                    suma = suma + numero

            print(f"La suma de los numeros ingresados es: {suma}")

            r1 = input("Quieres volver a ingresar un numero (s/n): ")

            if r1 =='s':
                contador = 0
            else:
                numero = 0
                contador = 0


    elif opcion == 2:
        r1 = 's'
        while r1 == 's':

            resta = 0
            numero = 0
            while contador < 2:
                contador = contador + 1 

                if contador == 1:
                    numero = int(input("Ingrese el primer numero: "))
                    resta = numero
                else:
                    numero = int(input("Ingrese el segundo numero: "))
                    resta = resta - numero

            
            print(f"La resta de los numeros ingresados es: {resta}")

            r1 = input("Quieres volver a ingresar un numero (s/n): ")

            if r1 =='s':
                contador = 0
            else:
                numero= 0
                contador = 0

    elif opcion == 3:
        r1 = 's'
        while r1 == 's':

            multiplicacion = 0
            numero = 0
            while contador < 2:
                contador = contador + 1 

                if contador == 1:
                    numero = int(input("Ingrese el primer numero: "))
                    multiplicacion = numero
                else:
                    numero = int(input("Ingrese el segundo numero: "))
                    multiplicacion = multiplicacion * numero

            
            print(f"La multiplicación de los numeros ingresados es: {multiplicacion}")

            r1 = input("Quieres volver a ingresar un numero (s/n): ")

            if r1 =='s':
                contador = 0
            else:
                numero= 0
                contador = 0
    elif opcion == 4:
        r1 = 's'
        while r1 == 's':

            division = 0
            numero = 0

            while contador < 2:
                contador = contador + 1 

                if contador == 1:
                    numero = int(input("Ingrese el primer numero: "))
                    division = numero
                else:
                    numero = int(input("Ingrese el segundo numero: "))
                    if numero == 0:
                        print("No se puede hacer una divion por cero")
                        break
                    else:
                        division = division / numero

            if numero == 0:
                r1 = input("Quieres volver a intentarlo? (s/n): ")
            else:
                print(f"La division de los numeros ingresados es: {division}")
                r1 = input("Quieres volver a intentarlo? (s/n): ")

            if r1 =='s':
                contador = 0
            else:
                numero= 0
                contador = 0
    else:
        if opcion == 5:
            break
        else:
            print("Ingrese alguna de las opciones mencionadas")
    



