'''
Docstring para actividades.actividad02.ejercicio03.utilidades
'''

import os

# Funciones de utilidad para la carrera de coches
def mostrar_coche(posicion: int, meta: int, coche_emoji: str, meta_emoji: str) -> None:
    """Muestra el carril de un coche."""
    # Creamos el camino con espacios y colocamos el coche y la meta
    camino = " " * posicion + coche_emoji

    # Ajustamos los espacios restantes hasta la meta
    espacios_restantes = " " * (meta - posicion)

    # Mostramos la línea completa
    print(camino + espacios_restantes + meta_emoji)

# Función para pedir un entero en un rango específico
def pedir_distancia_rango(instruccion: str, minimo: int, maximo: int) -> int:
    """Pide un entero al usuario y valida que esté en el rango."""
    while True:
        texto = input(instruccion)
        try:
            valor = int(texto)
            if not minimo <= valor <= maximo:
                raise ValueError(f"La distancia debe estar entre {minimo} y {maximo}.")
            return valor
        except ValueError as e:
            print(f"ERROR: {e}")

# Limpiar la pantalla de la consola
def limpiar_pantalla():
    """Borra la pantalla de la consola."""
    os.system('cls')
