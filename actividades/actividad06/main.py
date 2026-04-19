'''Programa principal'''

from AnimalController import AnimalController

def main():
    '''Método para envolvere el programa principal'''
    # Instancia del controlador
    controlador = AnimalController()
    salir = False

    while not salir:
        # Mostramos el menú y solicitamos la opción
        opcion = controlador.mostrar_menu()

        # Listamos todos los animales
        if opcion == 1:
            controlador.listar_animales()
        # Listamos los animales de una especie concreta
        elif opcion == 2:
            controlador.listar_por_especie()
        # Buscamos un animal por su ID
        elif opcion == 3:
            controlador.buscar_animal_por_id()
        # Agregamos un animal nuevo al refugio
        elif opcion == 4:
            controlador.agregar_animal()
        # Actualizamos los datos de un animal del refugio
        elif opcion == 5:
            controlador.actualizar_animal()
        # Eliminamos un animal del refugio
        elif opcion == 6:
            controlador.eliminar_animal()
        # Exportamos los datos de la BBDD a un CSV
        elif opcion == 7:
            controlador.exportar_a_csv()
        # Salimos del programa.
        elif opcion == 8:
            controlador.salir_del_programa()
            salir = True

# Arrancamos el programa
main()
