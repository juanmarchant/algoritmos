# 2. Ingresar 10 números y mostrar:
# Cuantos números ingresados son pares
# Cuantos son impares


acumulador = 0

contadorPares = 0
contadorImpares = 0

while acumulador < 10 :
    acumulador = acumulador + 1
    
    numero = int(input("Ingese un numero: "))

    if numero % 2 == 0:
        contadorPares = contadorPares + 1
    else:
        contadorImpares = contadorImpares + 1

print("Numeros Pares: ", contadorPares)
print("Numeros Impares: ", contadorImpares)


