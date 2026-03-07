'''
    Ejercicio 1: Escribir un programa que solicite al usuario su nombre y luego imprima un mensaje de bienvenida personalizado.
'''

import textos as t
import utilidades as u

frases = []

while True:
    frase = u.pedir_string("Introduce una frase (vacía para terminar): ")
    if len(frase) == 0:
        break
    else:
        frases.append(frase)

print("--- PROCESANDO FRASES ---")
if len(frases) == 0:
    print("===| No se ha añadido frases")

for f in frases:
    print(f"===| FRASE: {f}")
    print(f"===| Número de palabras: {t.contar_palabras(f, " .,:;¡!¿?()[]")}")
    print(f"===| Número total de caracteres (sin espacios ni puntuación): {t.caracteres_total(f, " .,:;¡!¿?()[]")}")
    print(f"===| Palabra más larga: {t.palabra_mas_larga(f)}")
    print("------------------------")
print("--- FIN DE FRASES ---")
