'''
Docstring para actividades.actividad01.ejercicio01.alquiler_salas

'''
import math
import utilidades as u

# Programa principal para pedir datos sobre el alquiler de salas de trabajo
while True:
    # Pedimos un entero al usuario
    numero_trabajadores = u.pedir_entero("Número de trabajadores: ")
    # Validamos que sea un entero positivo
    if not u.validacion_entero_positivo(numero_trabajadores):
        print("ERROR: el número de trabajadores debe ser un entero positivo mayor o igual que 0.")
    else:
        break

while True:
    # Pedimos un entero al usuario
    distancia_al_centro = u.pedir_entero("Distancia al centro de la ciudad en Km: ")
    # Validamos que sea un entero positivo
    if not u.validacion_entero_positivo(distancia_al_centro):
        print("ERROR: la distancia al centro debe ser un entero positivo mayor o igual que 0.")
    else:
        break

while True:
    # Pedimos un numero decimal al usuario
    precio_alquiler_mensual = u.pedir_decimal("Precio del alquiler mensual de una sala de trabajo en €: ")
    # Validamos que sea un numero decimal positivo
    if not u.validacion_decimal_positivo(precio_alquiler_mensual):
        print("ERROR: el precio del alquiler mensual debe ser un decimal positivo mayor o igual que 0.")
    else:
        break

while True:
    # Pedimos un numero decimal al usuario
    porcentaje_descuento = u.pedir_decimal("Porcentaje de descuento sobre el precio del alquiler mensual (Entre 0-1. Ej: 0.2->20%): ")
    # Validamos que sea un numero decimal entre 0 y 1 para el porcentaje
    if not u.validacion_porcentaje(porcentaje_descuento):
        print("ERROR: el porcentaje de descuento debe estar entre 0 y 1 (Incluidos).")
    else:
        break

while True:
    # Pedimos un booleano al usuario
    tiene_sala_descanso = u.pedir_booleano("¿Tiene sala de descanso? (1=Sí o 0=No): ")
    # Validamos que sea un booleano correcto con formato 1 o 0
    if not u.validacion_formato_booleano(int(tiene_sala_descanso)):
        print("ERROR: debe introducir 1 para Sí o 0 para No.")
    else:
        break


# Cálculo de salas necesarias
CAPACIDAD_MAXIMA_SALA = 10 # Personas por sala
if numero_trabajadores == 0:
    numero_de_salas = 0
else: 
    numero_de_salas = math.ceil(numero_trabajadores / CAPACIDAD_MAXIMA_SALA)

# Cálculo del precio a pagar teniendo en cuenta el descuento
porcentaje_a_pagar = 1 - porcentaje_descuento
precio_total_alquiler = numero_de_salas * precio_alquiler_mensual * porcentaje_a_pagar

# Clasificación del centro necesario
if numero_de_salas == 1:
    tipo_de_centro = "Pequeño"
elif 2 <= numero_de_salas <= 3:
    tipo_de_centro = "Mediano"
elif numero_de_salas >= 4:
    tipo_de_centro = "Grande"
else:
    tipo_de_centro = "No aplica"

# Centro es idióneo
DISTANCIA_MAXIMA = 5  # Kilometros
PRECIO_MAXIMO = 100 # Euros

if (tipo_de_centro != "No aplica"
    and tiene_sala_descanso
    and precio_alquiler_mensual <= PRECIO_MAXIMO
    and distancia_al_centro < DISTANCIA_MAXIMA
    ):
    centro_idoneo = True
else:
    centro_idoneo = False


# Mostrarmos los datos introducidos
print("\n---/ Datos introducidos /---")
print(f"Número de trabajadores: {numero_trabajadores}")
print(f"Distancia al centro de la ciudad en Km: {distancia_al_centro}")
print(f"Precio del alquiler mensual de una sala de trabajo en €: {precio_alquiler_mensual}")
print(f"Porcentaje de descuento sobre el precio del alquiler mensual: {porcentaje_descuento * 100}%")
print(f"¿Tiene sala de descanso?: {'Sí' if tiene_sala_descanso else 'No'}")

# Mostramos los cálculos realizados
print("\n---/ Resultados /---")
print(f"Número de salas necesarias: {numero_de_salas}")
print(f"Clasificación del centro necesario: {tipo_de_centro}")
print(f"Precio total a pagar por el alquiler mensual de las salas de trabajo: {precio_total_alquiler} €")
print(f"¿El centro es idóneo?: {'Sí' if centro_idoneo else 'No'}")
