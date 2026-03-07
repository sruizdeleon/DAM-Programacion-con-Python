'''
    Ejercicio 2: Crear una función recursiva que reciba una cadena y devuelva la cadena invertida.
'''

import textos as t
import utilidades as u

texto = u.pedir_string("Introduce una palabra o frase y pulsa enter: ")
texto_invertido = t.invertir_cadena(texto)
print(texto_invertido)
