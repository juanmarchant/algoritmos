# 1. Ingresar 10 números y mostrar: 
    # Cuantos son positivos
    # Cuantos son negativos


acumulador = 0
contadorPositivos = 0
contadorNegativos = 0


while acumulador < 10:
    acumulador = acumulador + 1

    numero = int(input(" Ingresa un numero: "))

    if numero > 0:
        contadorPositivos = contadorPositivos + 1
    else:
        contadorNegativos = contadorNegativos + 1

print("Numeros positivos: ", contadorPositivos)
print("Numeros negativos: ", contadorNegativos)
