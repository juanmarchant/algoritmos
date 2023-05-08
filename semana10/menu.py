import os

op = 0

while op != 4:
    print("""
    1. Divisores de un numero
    2. Numeros Perfectos
    3. Numeros Primos
    4. Finalizar
    """)

    while True:
        try:
            op = int(input("Ingrese la opcion (1-4): "))
            if op < 1 or op > 4:
                print("Ingrese un numero en el rango de 1-4")
            else:
                break
        except ValueError:
            print("Error, ingresaste algun caracter distinto de (1-4)")
    
    os.system('cls')
    
    if op == 1:
        r = 's'
        while r == 's': 
            while True:
                try: 
                    numero =  int(input("Ingrese un numero: "))
                    break
                except ValueError:
                    print("Error, ingreso un numero erroneo ")
            
            if numero < 0:
                numeroPrueba = numero * -1
            else:
                numeroPrueba = numero

            contador = 0
            
            while contador < numeroPrueba:
                contador = contador + 1
                if numeroPrueba % contador == 0:
                    print(f"El numero {contador} es divisor de {numero}")

            while True:
                try:
                    r = input("Ingresa otro numero s/n: ").lower()
                    if r != 's' and r != 'n':
                        print("Recuerda ingresar s o n")
                    else:
                        os.system('cls')
                        break
                except ValueError:
                    print("Error, ingresaste un valor erroneo.. intenta denuevo con s/n")
        
    if op == 2:
        r = 's'
        while r == 's': 
            while True:
                try: 
                    numero =  int(input("Ingrese un numero: "))
                    break
                except ValueError:
                    print("Error, ingreso un numero erroneo ")
            
            if numero < 0:
                numeroPrueba = numero * -1
            else:
                numeroPrueba = numero

            contador = 0
            sumaDivisores = 0

            while contador < numeroPrueba:
                contador = contador + 1
                if (numeroPrueba % contador ==0 and contador != numeroPrueba ):
                    sumaDivisores = sumaDivisores + contador
            
            if sumaDivisores == numeroPrueba:
                print(f"El numero {numero} si es perfecto")
            else:    
                print(f"El numero {numero} no es perfecto por que sus sumas dan {sumaDivisores}")
            
            while True:
                try:
                    r = input("Ingresa otro numero s/n: ").lower()
                    if r != 's' and r != 'n':
                        print("Recuerda ingresar s o n")
                    else:
                        os.system('cls')
                        break
                except ValueError:
                    print("Error, ingresaste un valor erroneo.. intenta denuevo con s/n")
                
    if op == 3:

        r = 's'
        while r == 's': 
            while True:
                try: 
                    numero =  int(input("Ingrese un numero: "))
                    break
                except ValueError:
                    print("Error, ingreso un numero erroneo ")
            
            if numero < 0:
                numeroPrueba = numero * -1
            else:
                numeroPrueba = numero

            contador = 0
            contadorPrimo = 0 

            while contador < numeroPrueba:
                contador = contador + 1

                if numeroPrueba % contador == 0:
                    contadorPrimo = contadorPrimo + 1 
            
            if contadorPrimo == 2:
                print(f"El numero {numero} si es primo")
            else:
                print(f"El numero {numero} no es primo")

            while True:
                try:
                    r = input("Ingresa otro numero s/n: ").lower()
                    if r != 's' and r != 'n':
                        print("Recuerda ingresar s o n")
                    else:
                        os.system('cls')
                        break
                except ValueError:
                    print("Error, ingresaste un valor erroneo.. intenta denuevo con s/n")



    


