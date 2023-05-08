# Ingresar 15 números y mostrar: 
    # La suma de los pares
    # El total de números cero ingresados
contador = 0

contadorCeros = 0 
sumaTotalPares = 0

while contador < 3 : 

    numero = int(input("Ingrese un numero: "))

    if numero % 2 == 0 :
        sumaTotalPares = sumaTotalPares + numero
    
    if numero == 0 : 
        contadorCeros = contadorCeros + 1

    contador = contador + 1

print("La suma total de los pares es: ", sumaTotalPares)
print("La cantidad de ceros ingresados es: ", contadorCeros)

