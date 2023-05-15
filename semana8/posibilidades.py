import random


contadorPosibilidades = 0
numeroRandom = random.randrange(10)

while contadorPosibilidades != 5:
    try:
        numeroUsuario = int(input("Ingresa un numero: "))
        if numeroUsuario == numeroRandom:
            print(f"Felicidades! Haz adivinado el numero random {numeroRandom}")
            break
        else:
            contadorPosibilidades += 1
            print(f"Error, No haz acertado... Te quedan {5 - contadorPosibilidades} Posibilidades")
    except ValueError:
        print("Error, ingresaste un valor no valido, recuerda ingresar un valor entero")

if contadorPosibilidades == 5:
    print("Lo sentimos.. Vuelve a intentarlo mas tarde")
