'''
    Ejercicio 03: Ordenación y búsqueda
'''

import textos as t

lista = [2, 2, 3, 5, 10, 1, 3, 6, 9]

lista_ordenada = t.ordenar_lista(lista)

print(f"==| Lista ordenada: {lista_ordenada}")

index = t.busqueda_binaria(lista_ordenada, 5, 0, len(lista_ordenada)-1)

print(f"==| Posición de 5: {index}")
