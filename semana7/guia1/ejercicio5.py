# 5. Ingresa n numeros enteros y mostrar el mayor y el menor.

cantidadNumeros = int(input("Cuantas veces desea ingresar un numero ? : "))
contador = 0

numeroMayor = 0
numeroMenor = 0
while contador < cantidadNumeros: 

    numero = int(input("Ingrese un numero: "))

    if contador == 0:
        numeroMayor = numero
        numeroMenor = numero

    if numero > numeroMayor: 
        numeroMayor = numero

    if numero < numeroMenor:
        numeroMenor = numero 
        
    contador = contador + 1

print("El numero mayor es: ", numeroMayor)
print("El numero menor es: ", numeroMenor)



