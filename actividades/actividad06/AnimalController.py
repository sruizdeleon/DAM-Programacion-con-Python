'''
Clase de Controlador - Intermediario entre Modelo y Vista
'''
import AnimalModel
from AnimalView import AnimalView
import csv

class AnimalController:
    '''Clase de controlador'''
    def __init__(self):
        # Instancia de la vista para pedir información y mostrar información al usuario
        self.vista = AnimalView()

    def mostrar_menu(self):
        '''Método para ordenar a la Vista que muestre el menú'''
        return self.vista.mostrar_menu()

    def salir_del_programa(self):
        '''Método para salir del programa'''
        self.vista.mostrar_mensaje_info("Saliendo del programa.")


    def listar_animales(self):
        '''Obtiene los animales de Model y los pasa a View para que los muestre'''
        animales = AnimalModel.obtener_todos_animales()
        if animales:
            self.vista.mostrar_lista(animales)
        else:
            self.vista.mostrar_mensaje_info("No hay animales registrados en el refugio.")

    def buscar_animal_por_id(self):
        '''Obtiene un animal por ID de Model y los pasa a View para que los muestre'''
        id = self.vista.pedir_id()
        animal = AnimalModel.obtener_animal_por_id(id)
        if animal:
            self.vista.mostrar_animal(animal)
        else:
            self.vista.mostrar_mensaje_info(f"No hay animal registrado con ID ({id}) en el refugio.")

    def agregar_animal(self):
        '''Guarda un nuevo animal por medio del Model'''
        animal = self.vista.pedir_datos_animal()
        exito = AnimalModel.crear_animal(animal)
        if exito:
            self.vista.mostrar_mensaje_info(f"{animal.nombre} ha sido registrado correctamente.")
        else:
            self.vista.mostrar_mensaje_error("Error al intentar registrar al animal.")

    def actualizar_animal(self):
        '''Busca un animal y lo actualiza por medio de Model'''
        # Primero lo buscamos por si no existe
        id_buscado = self.vista.pedir_id()
        animal_encontrado = AnimalModel.obtener_animal_por_id(id_buscado)
        # Si existe lo actualizamos
        if animal_encontrado:
            animal_a_actualizar = self.vista.pedir_datos_animal()
            animal_a_actualizar.id = id_buscado

            exito = AnimalModel.actualizar_animal(animal_a_actualizar.id, animal_a_actualizar)
            if exito:
                self.vista.mostrar_mensaje_info(f"{animal_a_actualizar.nombre} ha sido actualizado correctamente.")
            else:
                self.vista.mostrar_mensaje_error("Error al intentar actualizar al animal.")
        # Si no existe mostramos error
        else:
            self.vista.mostrar_mensaje_error(f"No existe animal con el ID ({id_buscado})")

    def eliminar_animal(self):
        '''Busca un animal y lo elimina usando el Model'''
        id = self.vista.pedir_id()
        # Primero buscamos si existe el animal
        animal_encontrado = AnimalModel.obtener_animal_por_id(id)
        # Si existe lo eliminamos
        if animal_encontrado:
            if AnimalModel.eliminar_animal(id):
                self.vista.mostrar_mensaje_info("Animal eliminado del sistema.")
            else:
                self.vista.mostrar_mensaje_error("No se pudo eliminar: ID no encontrado.")
        # Si no existe mostramos error
        else:
            self.vista.mostrar_mensaje_error(f"No existe animal con el ID ({id})")

    def listar_por_especie(self) -> list:
        '''Pide la especie y muestra los animales de esa especie'''
        especie = self.vista.pedir_especie()
        animales = AnimalModel.obtener_por_especie(especie.value)
        if animales:
            self.vista.mostrar_lista(animales)
        else:
            self.vista.mostrar_mensaje_error("No hay animales registrados en el refugio.")

    def exportar_a_csv(self):
        '''Obtiene los datos y los escribe en un archivo CSV'''
        animales = AnimalModel.obtener_todos_animales()

        # Si no hay animales mostramos el error y no creamos el fichero
        if not animales:
            self.vista.mostrar_mensaje_error("No hay datos para exportar.")
            return

        # Creamos el nombre del fichero
        nombre_fichero = "actividades/actividad06/refugio_animales.csv"
        try:
            # Creamos el fichero en modo escritura
            with open(nombre_fichero, "w", newline="", encoding="utf-8") as archivo:
                # Creamos el escritor
                escritor = csv.writer(archivo)
                # Insertamos la cabecera
                escritor.writerow(["ID", "Nombre", "Especie", "Edad", "Adoptado"])
                # Insertamos cada animal en una fila
                for a in animales:
                    escritor.writerow([a.id, a.nombre, a.especie, a.edad, a.adoptado])

            # Exportación existosa
            self.vista.mostrar_mensaje_info(f"Datos exportados con éxito a {nombre_fichero}")
        except Exception as e:
            # Error durante la exportación
            self.vista.mostrar_mensaje_error(f"Error al exportar el csv: {e}")
