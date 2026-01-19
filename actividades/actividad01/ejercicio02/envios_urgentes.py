'''
Docstring para actividades.actividad01.ejercicio02.envios_urgentes
'''

import utilidades as u

# Soliciatamos los datos al usuario

while True:
    peso_paquete = u.pedir_decimal("Peso del paquete en Kg: ")
    if not u.validacion_decimal_positivo(peso_paquete):
        print("ERROR: el peso del paquete debe ser un decimal positivo mayor o igual que 0.")
    else:
        break

while True:
    distancia_recorrido = u.pedir_decimal("Distancia a recorrer en Km: ")
    if not u.validacion_decimal_positivo(distancia_recorrido):
        print("ERROR: la distancia a recorrer debe ser un decimal positivo mayor o igual que 0.")
    else:
        break

while True:
    precio_por_kg = u.pedir_decimal("Precio por Kg en €: ")
    if not u.validacion_decimal_positivo(precio_por_kg):
        print("ERROR: el precio por Kg debe ser un decimal positivo mayor o igual que 0.")
    else:
        break

while True:
    recargo_urgente = u.pedir_booleano("¿El envío es urgente? (1=Sí o 0=No): ")
    if not u.validacion_formato_booleano(int(recargo_urgente)):
        print("ERROR: debe introducir 1 para Sí o 0 para No.")
    else:
        break

while True:
    tiene_seguro = u.pedir_booleano("¿El envío tiene seguro? (1=Sí o 0=No): ")
    if not u.validacion_formato_booleano(int(tiene_seguro)):
        print("ERROR: debe introducir 1 para Sí o 0 para No.")
    else:
        break

# Constantes
PORCENTAJE_COSTE_URGENTE = 0.08
PESO_MAXIMO = 2
DISTANCIA_MAXIMA = 30

# Cálculo del coste base del envío
coste_base = peso_paquete * precio_por_kg

# Cálculo del recargo por envío urgente
coste_urgente = coste_base + (coste_base * PORCENTAJE_COSTE_URGENTE) if recargo_urgente else coste_base

# Cálculo coste final
if tiene_seguro:
    coste_final = coste_urgente * (1 + PORCENTAJE_COSTE_URGENTE)
else:
    coste_final = coste_urgente

# Clasificación

if peso_paquete <= PESO_MAXIMO:
    if distancia_recorrido <= DISTANCIA_MAXIMA:
        tipo_envio = "Rápido"
    else:
        tipo_envio = "Normal"
else:
    tipo_envio = "Especial"


# Mostramos si el envío es económico

COSTE_ECONOMICO = 20
DISTANCIA_ECONOMICA = 30
PESO_ECONOMICO = 2

if coste_final <= COSTE_ECONOMICO and distancia_recorrido <= DISTANCIA_ECONOMICA and peso_paquete <= PESO_ECONOMICO:
    envio_economico = True
else:
    envio_economico = False

# Mostrarmos los datos introducidos
print("\n---/ Datos introducidos /---")
print(f"Peso del paquete en Kg: {peso_paquete} Kg")
print(f"Distancia a recorrer en Km: {distancia_recorrido} Km")
print(f"Precio por Kg en €: {precio_por_kg} €")
print(f"¿El envío es urgente?: {'Sí' if recargo_urgente else 'No'}")
print(f"¿El envío tiene seguro?: {'Sí' if tiene_seguro else 'No'}")

# Mostramos los cálculos realizados
print("\n---/ Resultados /---")
print(f"Coste final del envío: {coste_final} €")
print(f"Tipo de envío: {tipo_envio}")
print(f"¿El envío es económico?: {'Sí' if envio_economico else 'No'}")
