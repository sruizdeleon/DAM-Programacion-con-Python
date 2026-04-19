'''
Clase de Vista - Se encarga de intractuar con el usuario
'''
from Animal import Especie
from Animal import Animal
import utilidades as u

class AnimalView:
    '''Clase de Vista'''

    MENU = '''
=========== REFUGIO DE ANIMALES ============
1. Listar todos los animales
2. Listar por especie
3. Buscar animal por ID
4. Registrar nuevo animal
5. Actualizar animal
6. Eliminar animal
7. Exportar a CSV
8. Salir
'''

    def __init__(self):
        # Ponemos una instancia de la vista para comunicarse y traer información
        pass

    def mostrar_menu(self) -> int:
        '''Método para mostrar el menú de opciones y solicitar opción'''
        print(self.MENU)
        return u.pedir_entero_entre("==| Elige una opción: ", 1, 8)

    def mostrar_lista(self, animales: list):
        '''Método para mostrar una lista de animales o mensaje de refugio vacío'''
        if not animales:
            self.mostrar_mensaje_info("No hay animales en el refugio")
        else:
            print("\n======== ANIMALES ========")
            for animal in animales:
                print(f"[ANIMAL] {(animal)}")

    def mostrar_animal(self, animal: Animal):
        '''Método para mostrar un animal o refugio vacío'''
        if not animal:
            self.mostrar_mensaje_info("No hay animal en el refugio")
        else:
            print("\n======== ANIMAL ========")
            print(f"[ANIMAL] {(animal)}")

    def mostrar_mensaje_info(self, mensaje: str):
        '''Método para mostrar un mensaje de información'''
        print(f"\n[INFO] - {mensaje}")

    def mostrar_mensaje_error(self, mensaje: str):
        '''Método para mostrar un mensaje de error'''
        print(f"\n[ERROR] - {mensaje}")

    def pedir_datos_animal(self) -> Animal:
        '''Método para pedir los datos de un animal'''
        # Pedimos el nombre
        nombre = u.pedir_string("\n==| Nombre del animal: ")
        # Pedimos la especie
        especie = self.pedir_especie()
        # Pedimos la edad
        edad = u.pedir_entero_positivo("\n==| Edad del animal: ")
        # Pedimos si está adoptado o no
        adoptado = u.pedir_booleano("\n==| ¿Está adoptado? (0 = No) o (1 = Sí): ")

        return Animal(nombre, especie, edad, adoptado)

    def pedir_especie(self) -> Especie:
        '''Método para pedir especie'''
        # Creamos el mensaje a mostrar
        mensaje = f"\n==| Escribe la especie a buscar ({[e.value for e in Especie]}): "
        # Guardamos las opciones en una lista
        opciones = [e.value for e in Especie]
        # Pedimos a la utilidad de opciones que elija una opción
        especie = u.pedir_opciones(mensaje, opciones)
        # Devolvemos el valor de especie
        return Especie(especie).value

    def pedir_id(self) -> int:
        '''Método para pedir id'''
        return u.pedir_entero_positivo("\n==| Escribe el id: ")
