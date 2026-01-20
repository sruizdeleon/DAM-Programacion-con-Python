'''
Docstring para actividades.actividad02.ejercicio01.juego
'''

import utilidades as u

# Variables y constante
MAXIMO_PARTIDAS = 3
partidas_usuario = 0
partidas_maquina = 0

# Comienzo del juego
while partidas_usuario < MAXIMO_PARTIDAS and partidas_maquina < MAXIMO_PARTIDAS:
    # Pedimos jugada al usuario y la máquina
    jugada_usuario = u.pedir_jugada_usuario("Introduce tu jugada: piedra, papel o tijeras: ")
    jugada_maquina = u.pedir_jugada_maquina()

    # Mostramos las jugadas de ambos
    print("\n---/ Jugadas /---")
    print(f"La juagada del usuario es: {jugada_usuario}")
    print(f"La jugada de la máquina es: {jugada_maquina}\n")

    # Resolvemos las jugadas y determinamos el ganador
    resultado = u.determinar_ganador(jugada_usuario, jugada_maquina)
    print(f"El resultado de la partida es: {resultado}")

    # Actualizamos los marcadores
    if resultado == "ganar":
        partidas_usuario += 1
    elif resultado == "perder":
        partidas_maquina += 1

    # Mostramos el marcador parcial o el marcador final con el ganador
    if partidas_usuario == MAXIMO_PARTIDAS or partidas_maquina == MAXIMO_PARTIDAS:
        print("\n---/ Resultado final /---")
        print(f"Usuario {partidas_usuario} - Máquina {partidas_maquina}")
        print("\n ---/ Ganador /---")
        print("Usuario" if partidas_usuario == MAXIMO_PARTIDAS else "Máquina")
        print("¡Fin del juego!")
    else:
        print(f"Resultado de la ronda: Usuario {partidas_usuario} - Máquina {partidas_maquina}\n")
