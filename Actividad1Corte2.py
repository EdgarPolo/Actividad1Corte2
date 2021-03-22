# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:01:18 2021

@author: Edgar_Polo
"""

# Ejercicio 1

    def operaciones(v):
        import numpy as a
    sumatoria = int(sum(v))
    productoria = int(a.prod(v))
    maximo = int(max(v))
    minimo = int(min(v))

    return sumatoria, productoria, maximo, minimo

tam = int(input("Tamaño Del Vector: "))
v = []
for i in range(tam):
    elemento = int(input(f"Ingrese El Elemento  {i+1} Para El Vector: "))
    v.append(elemento)

 sumatoria, productoria , maximo, minimo  = operaciones(v)

print(f'''
La Sumatoria De Los Elementos Del Vector Es: {sumatoria}
La Productoria De Los Elementos Del Vector Es: {productoria}
El Mayor Elemento Del Vector Es: {maximo}
El Menor Elemento Del Vector Es: {minimo}
''')

# Ejercicio 2

def par_impar_primos(v):
    par, impar, primo = 0, 0, 0
    for elemento in v:
        if elemento % 2 == 0:
            par += 1
        else:
            impar += 1
        if all(elemento % i != 0 for i in range(2, elemento)):
            primo += 1
    return par, impar, primo

tam = int(input("Tamaño Del Vector: "))
v = []
for i in range(tam):
    elemento = int(input(f"Ingrese El Elemento  {i+1} Para El Vector: "))
    v.append(elemento)

par,impar,primo = par_impar_primos(v)

print(f'''
Este vector tiene:
{par} Elementos Pares
{impar} Elementos Impares
{primo} Elementos Primos
''')

# Ejercicio 3

def suma_resta(va, vb):
    import numpy as np
    if len(va) != len(vb):
        return TypeError
    else:
        suma = np.array(va) + np.array(vb)
        resta = np.array(va) - np.array(vb)
        return suma,  resta

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

suma, resta = suma_resta(va, vb)
print(f'''
La Suma De Estos Dos Vectores Es: {suma}
La Resta De Estos Dos Vectores Es: {resta}''')

# Ejercicio 4

def repetidos(v):
    repete = []
    for x in range(len(v)):
        cout = 0
        for element in v:
            if v[x] == element:
                cout = cout + 1
        repete.append(cout)
    mas_repetido = repete.index(max(repete))
    return(v[mas_repetido])

tam = int(input("Tamaño Del Vector: "))
v = []
for i in range(tam):
    elemento = int(input(f"Ingrese El Elemento  {i+1} Para El Vector: "))
    v.append(elemento)

repetido = repetidos(v)
print(f'''EL Elemento Que Más Se Repite Es: {repetido}''')


# Ejercicio 5

def mitad_mitad(v):
    productoria = 1
    sumatoria1 = 0
    if len(v) % 2 == 0:
        for x in range(len(v)):
            if x < int(len(v) / 2):
                productoria = productoria * v[x]
            else:
                sumatoria1 = sumatoria1 + v[x]
    else:
        print("La Longitud del vector no es par")

    return productoria, sumatoria1


tam = int(input("Tamaño Del Vector: "))
v = []
for i in range(tam):
    elemento = int(input(f"Ingrese El Elemento  {i+1} Para El Vector: "))
    v.append(elemento)

productoria_mitad, sumatoria_mitad = mitad_mitad(v)

print(f'''
La Productoria De La Primera Parte Es: {productoria_mitad}
La Sumatoria De La Otra Parte Es: {sumatoria_mitad}''')

# Ejercicio 6

def simetrico(v):
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
        v = list(v)
        v.pop(v[int(len(v) / 2)-1])
        v = tuple(v)
        if len(v) % 2 == 0:
            i = 1
            for x in range(int(len(v) / 2)):
                if v[x] == v[len(v)-i]:
                    i += 1
                    sime = True
                else:
                    sime = False
                    break
    return sime

tam = int(input("Tamaño Del Vector: "))
v = []
for i in range(tam):
    elemento = int(input(f"Ingrese El Elemento  {i+1} Para El Vector: "))
    v.append(elemento)

simetrico = simetrico(v)

if simetrico:
    print(f'El Vector {v} Es Simetrico')
else:
    print(f'El Vector {v} No Es Simetrico')


# Ejercicio 7

def conjuntos(va, vb):
    va = set(va)
    vb = set(vb)
    union = va | vb
    interseccion = va & vb
    diferen_A = va - vb
    diferen_B = vb - va

    return union, interseccion, diferen_A,  diferen_B

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

union, interseccion, diferen_A,  diferen_B = conjuntos(va, vb)
print(f'''
La Unión Entre Los 2 Vectores Da Como Resultado: {union}
La Intersección Entre Los 2 Vectores Da Como Resultado: {interseccion}
La Diferencia Entre El Vector A y El Vector B Da Como Resultado: {diferen_A}
La Diferencia Entre El Vector B y El Vector A Da Como Resultado: {diferen_B}
''')
