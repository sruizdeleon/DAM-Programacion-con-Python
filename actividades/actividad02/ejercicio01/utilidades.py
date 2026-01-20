'''
Docstring para actividades.actividad02.ejercicio01.utilidades
'''

import random


def pedir_jugada_usuario(instruccion: str) -> str:
    "Pide la siguiente jugada al usuario (piedra, papel o tijera)."
    while True:
        texto = input(instruccion)
        texto = texto.lower()
        if texto in ["piedra", "papel", "tijeras"]:
            return texto
        else:
            print("ERROR: no has proporcionado una jugada válida (piedra, papel o tijeras)")


def pedir_jugada_maquina() -> str:
    "Genera una jugada aleatoria para la máquina (piedra, papel o tijera)."
    jugada_numero = random.Random().randint(1, 3)
    if jugada_numero == 1:
        return "piedra"
    elif jugada_numero == 2:
        return "papel"
    elif jugada_numero == 3:
        return "tijeras"

def determinar_ganador(jugada_usuario: str, jugada_maquina: str) -> str:
    "Determina el ganador de la partida según las jugadas del usuario y de la máquina."
    if jugada_usuario == jugada_maquina:
        return "empatar"
    elif (jugada_usuario == "piedra" and jugada_maquina == "tijeras") or \
         (jugada_usuario == "papel" and jugada_maquina == "piedra") or \
         (jugada_usuario == "tijeras" and jugada_maquina == "papel"):
        return "ganar"
    else:
        return "perder"
