# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:01:18 2021

@author: Edgar_Polo
"""
# Ejercicio 1

import numpy as a
tam = int(input("Tamaño Del Vector: "))
v = []
for i in range(tam):
    elemento = int(input(f"Ingrese El Elemento  {i+1} Para El Vector: "))
    v.append(elemento)

sumatoria = int(sum(v))
productoria = int(a.prod(v))
maximo = int(max(v))
minimo = int(min(v))

print(f'''
La Sumatoria De Los Elementos Del Vector Es: {sumatoria}
La Productoria De Los Elementos Del Vector Es: {productoria}
El Mayor Elemento Del Vector Es: {maximo}
El Menor Elemento Del Vector Es: {minimo}
''')


# Ejercicio 2

tam = int(input("Tamaño Del Vector: "))
v = []
for i in range(tam):
    elemento = int(input(f"Ingrese El Elemento  {i+1} Para El Vector: "))
    v.append(elemento)

   par,impar,primo=0,0,0
    for element in v:
        if element % 2 == 0:
        par += 1
    else:
        impar += 1
    if all(element % i != 0 for i in range(2, element)):
        primo += 1

print(f'''
Este vector tiene:
{par} Elementos Pares
{impar} Elementos Impares
{primo} Elementos Primos
''')

"""
Ejercicio 3

Dado un Vector v y un Vector v1 de cómo resultado un Vector resultante de
las siguientes operaciones:
a. Suma
b. Resta
"""
va = []
vb = []
for i in range(2):
    tam = int(input(f"Tamaño Del Vector {i+1}: "))
    for j in range(tam):
        elemet = int(input(f"Ingrese El Elemento {j+1} Para El Vector {i+1}:"))
        if i == 0:
            va.append(elemet)
        else:
            vb.append(elemet)

suma, resta = 0,0
if len(va) != len(vb):
    print('Error')
else:
    suma = np.array(va) + np.array(vb)
    resta = np.array(va) - np.array(vb)
print(f'''
La Suma De Estos Dos Vectores Es: {suma}
La Resta De Estos Dos Vectores Es: {resta}''')


"""
Ejercicio 4

De los n elementos de un vector dado identifique el número que mas se
repite e indique cual es.
"""

tam = int(input("Tamaño Del Vector: "))
v = []
for i in range(tam):
    elemento = int(input(f"Ingrese El Elemento  {i+1} Para El Vector: "))
    v.append(elemento)

repetido = 0
repete = []
for x in range(len(v)):
    cout = 0
    for element in v:
        if v[x] == element:
            cout = cout + 1
    repete.append(cout)
mas_repetido = repete.index(max(repete))
repetido = (v[mas_repetido])
print(f'''EL Elemento Que Más Se Repite Es: {repetido}''')

"""
Ejercicio 5

Dado un Vector v de longitud par, divida en 2 partes, en la primera parte
realice la productoria y en la segunda la sumatoria. Entregue los valores
resultantes.
"""

tam = int(input("Tamaño Del Vector: "))
v = []
for i in range(tam):
    elemento = int(input(f"Ingrese El Elemento  {i+1} Para El Vector: "))
    v.append(elemento)

productoria = 1
sumatoria = 0
if len(v) % 2 == 0:
    for x in range(len(v)):
        if x < int(len(v) / 2):
            productoria = productoria * v[x]
        else:
            sumatoria = sumatoria + v[x]
else:
    print("La Longitud del vector no es par")

print(f'''
La Productoria De La Primera Parte Es: {productoria}
La Sumatoria De La Otra Parte Es: {sumatoria}''')


"""
Ejercicio 6

Dado un vector v, indique si es simétrico, un vector es simétrico si siendo
longitud par los números de la primera mitad son iguales al inverso de la
otra mitad por ejemplo: X=[1,2,3,3,2,1], en el ejemplo x es un vector
simétrico, en caso que la longitud del vector sea impar, se ignorará el
elemento central y se seguirá la misma lógica anterior, por ejemplo:
Y=[3,5,7,8,7,5,3], en este ejemplo Y es simétrico.
"""

tam = int(input("Tamaño Del Vector: "))
v = []
for i in range(tam):
    elemento = int(input(f"Ingrese El Elemento  {i+1} Para El Vector: "))
    v.append(elemento)

if len(v) % 2 == 0:
    i = 1
    for x in range(int(len(v) / 2)):
        if v[x] == v[len(v)-i]:
            i += 1
            sime = True
        else:
            sime = False
            break
else:
    l = list(v)
    l.pop(v[int(len(l) / 2)-1])
    l = tuple(l)
    if len(l) % 2 == 0:
        i = 1
        for x in range(int(len(l) / 2)):
            if l[x] == l[len(l)-i]:
                i += 1
                sime = True
            else:
                sime = False
                break
simetrico = sime

if simetrico:
    print(f'El Vector {v} Es Simetrico')
else:
    print(f'El Vector {v} No Es Simetrico')

"""
Ejercicio 7

Dado dos vectores númericos A y B debe realizar las siguiente operaciones
con conjuntos:
a. Unión: Conjunto que contiene(sin repetir) los elementos de A y B.
b. Intersección: Conjunto que contiene los elementos comunes que
aparecen en los conjuntos A y B
c. Diferencia(A-B) Conjunto formado por los elementos que pertenecen
al conjunto A y no pertenecen al conjunto B.
d. Diferencia (B-A) Conjunto formado por los elementos que pertenecen
al conjunto B y no pertenecel al conjunto A.
"""

va = []
vb = []
for i in range(2):
    tam = int(input(f"Tamaño Del Vector {i+1}: "))
    for j in range(tam):
        elemet = int(input(f"Ingrese El Elemento {j+1} Para El Vector {i+1}:"))
        if i == 0:
            va.append(elemet)
        else:
            vb.append(elemet)

va = set(va)
vb = set(vb)
union = va | vb
interseccion = va & vb
diferen_A = va - vb
diferen_B = vb - va
print(f'''
La Unión Entre Los 2 Vectores Da Como Resultado: {union}
La Intersección Entre Los 2 Vectores Da Como Resultado: {interseccion}
La Diferencia Entre El Vector A y El Vector B Da Como Resultado: {diferen_A}
La Diferencia Entre El Vector B y El Vector A Da Como Resultado: {diferen_B}
''')