'''
Programa principal para la gestión de centrales energéticas
'''

from gestion_centrales import GestionCentrales
from modelo_central import CentralTermica, CentralNuclear
from modelo_energia import TipoCombustible, TipoMaterial
import utilidades as u


def agregar_central(gestor: GestionCentrales):
    '''Función del menú para agregar central'''
    # Validamos que no haya nombres repetidos
    try:
        while True:
            nombre = u.pedir_string("\nNombre: ")
            if not GestionCentrales.existe_nombre(gestor, nombre):
                break
            print("ERROR - Ya existe una central con ese nombre.")
        ubicacion = u.pedir_string("\nUbicación: ")
        kwh = u.pedir_entero_positivo("\nProducción (kWh >= 0): ")
        # Recogemos el tipo de opción
        tipo = u.pedir_opciones("\nEscribe el tipo de central (Térmica o Nuclear): ", ["Térmica", "Nuclear"])

        nueva_central = None
        # Si es térmica
        if tipo == "Térmica":
            combustible = u.pedir_opciones(f"\nSelecciona el tipo de combustible {[e.value for e in TipoCombustible]}: ", [e.value for e in TipoCombustible])
            nueva_central = CentralTermica(nombre, kwh, ubicacion, combustible)
        # Si es nuclear
        elif tipo == "Nuclear":
            material = u.pedir_opciones(f"\nSelecciona el tipo de material {[e.value for e in TipoMaterial]}: ", [e.value for e in TipoMaterial])
            nueva_central = CentralNuclear(nombre, kwh, ubicacion, material)
        else:
            print("\nERROR - Tipo de central no reconocido.")
            return

        gestor.agregar_central(nueva_central)
        print("\nSUCCESS - Central añadida con éxito.")
    except ValueError as e:
        print(e)


def mostrar_centrales(gestor: GestionCentrales):
    '''Función del menú para mostrar todas las centrales'''
    centrales = gestor.obtener_centrales()
    if not centrales:
        print("\nNo hay centrales registradas.")
    else:
        print("\n============ LISTADO DE CENTRALES =============")
        n = 1
        for c in centrales:
            print(f"({n}) {c})")
            n += 1


def ver_produccion_total(gestor: GestionCentrales):
    '''Función del menú para ver la producción de todas las centrales'''
    total = gestor.obtener_produccion()
    print(f"\nLa producción total de todas las centrales es de: {total} kWh")


def ver_produccion_por_tipo(gestor: GestionCentrales):
    '''Función del menú para ver la producción por tipo de central'''
    prod_termica = gestor.obtener_produccion_centrales_termicas()
    prod_nuclear = gestor.obtener_produccion_centrales_nucleares()

    print("\n===========  PRODUCCIÓN  =============")
    print(f"==| Producción TÉRMICA total: {prod_termica} kWh")
    print(f"==| Producción NUCLEAR total: {prod_nuclear} kWh")


def ver_mayor_produccion(gestor: GestionCentrales):
    '''Función del menú para buscar la central con mayor producción'''
    central = gestor.obtener_central_mayor_produccion()
    if central:
        print(f"\nLa central con mayor producción es:\n{central}")
    else:
        print("\nNo hay centrales registradas en el sistema.")


MENU = '''\n--- GESTIÓN DE CENTRALES ENERGÉTICAS ---
1. Añadir nueva Central
2. Mostrar todas las centrales
3. Ver producción total
4. Ver producción por tipo (Térmica/Nuclear)
5. Buscar central con mayor producción
6. Salir

==| Selecciona una opción: '''


def main():
    '''Función de entrada al programa principal'''
    # Iniciamos el Gestor de Centrales vacío
    gestor = GestionCentrales()

    while True:
        opcion = u.pedir_entero_entre(MENU, 1, 6)
        
        if opcion == 1:
            agregar_central(gestor)  
        elif opcion == 2:
            mostrar_centrales(gestor)
        elif opcion == 3:
            ver_produccion_total(gestor)
        elif opcion == 4:
            ver_produccion_por_tipo(gestor)
        elif opcion == 5:
            ver_mayor_produccion(gestor)
        elif opcion == 6:
            print("EXIT - Saliendo del programa")
            break


if __name__ == "__main__":
    main()