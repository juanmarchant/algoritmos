import os
"""

[0] [0, 1, 2, 3, 4]
[1] [0, 1, 2, 3, 4]
[2] [0, 1, 2, 3, 4]
"""
import numpy as np

matriz = np.empty((2,5), type(object))
print(matriz)
print(matriz)

largo = len(matriz[0])

for i in range(2):
    while True:
        try:
            nombre=input(f"Persona {i + 1}\nIngrese el nombre del donador").strip()
            if len(nombre) <= 6:
                print("El nombre del donador tiene que ser mayor a 6 caracteres...")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")
    matriz[0][i] =  nombre

    while True:
        try:
            genero=input(f"Persona {i + 1}\n Ingrese el genero del donador (mujer/hombre): ").strip().lower()
            if genero!= "mujer" and genero!="hombre":
                print("El genero del donador puede ser mujer/hombre")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")
    matriz[1][i] =  genero

for columna in range(largo):
    print(f""" 
    {matriz[0][columna]}
    {matriz[1][columna]}
    """)