'''
Docstring para actividades.actividad02.ejercicio03.carrera_coches
'''

import random
import utilidades as u

# Constantes y variables
COCHE_A_EMOJI = "🚗"
COCHE_B_EMOJI = "🚙"
META_EMOJI = "🏁"
posicion_a = 0
posicion_b = 0
turno = 1


# Silicitamos el tamaño de carrera
distancia_meta = u.pedir_distancia_rango("Introduce la distancia de la carrera (30-60): ", 30, 60)

# Comienzo de la carrera
while posicion_a < distancia_meta and posicion_b < distancia_meta:
    # Borramos pantalla
    u.limpiar_pantalla()

    # Mostramos el turno
    print(f"--- Turno {turno} ---")

    # Movimiento aleatorio de A y su categorización
    numero_a = random.randint(1, 100)
    mensaje_coche_a = ""
    if numero_a <= 20:
        posicion_a = max(0, posicion_a - 5)
        mensaje_coche_a = "Pinchazo!! Retrocede 5 casillas" # 20%
    elif numero_a <= 50:
        posicion_a += 5
        mensaje_coche_a = "Turbo! Avanza 5 casillas" # 30%
    else:
        mensaje_coche_a = "No ocurre nada" # 50%


    # Movimiento aleatorio de B y su categorización
    numero_b = random.randint(1, 100)
    mensaje_coche_b = ""
    if numero_b <= 20:
        posicion_b = max(0, posicion_b - 5)
        mensaje_coche_b = "Pinchazo!! Retrocede 5 casillas"
    elif numero_b <= 50:
        posicion_b += 5
        mensaje_coche_b = "Turbo! Avanza 5 casillas"
    else:
        mensaje_coche_b = "No ocurre nada"

    # Anunciamos los movimientos de los coches
    print(f"Coche A: {mensaje_coche_a}")
    print(f"Coche B: {mensaje_coche_b}")
    print("\nPosiciones:")

    # Dibujamos la posición de los coches
    u.mostrar_coche(posicion_a, distancia_meta, COCHE_A_EMOJI, META_EMOJI)
    u.mostrar_coche(posicion_b, distancia_meta, COCHE_B_EMOJI, META_EMOJI)

    # Esperamos al nuevo turno
    input("\nPulsa Enter para que avance el turno...")
    turno += 1

# Final de la carrera
print("\n--- RESULTADO FINAL ---")
if posicion_a >= distancia_meta and posicion_b >= distancia_meta:
    print("¡Empate! Ambos coches han cruzado la meta.")
elif posicion_a >= distancia_meta:
    print("¡Ganador: Coche A (Jugador)! 🏆")
else:
    print("¡Ganador: Coche B (Máquina)! 🏆")
