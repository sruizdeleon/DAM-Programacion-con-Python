'''
Modelo - Se encarga de extraer datos de MySQL
'''

from conexion import crear_conexion
from Animal import Animal, Especie
from AnimalView import AnimalView as vista
import mysql

def obtener_todos_animales() -> list:
    '''Método para obtener todos los animales'''
    animales = []
    # Creamos la conexión
    conexion = crear_conexion()

    if conexion:
        try:
            # Creamos el cursor
            cursor = conexion.cursor(dictionary=True)
            # Ejecutamos la query
            cursor.execute("SELECT * FROM animales")
            # Traemos los resultados
            resultados = cursor.fetchall()

            # Transformamos la tabla en una Lista de Animales
            for fila in resultados:
                animal = Animal(
                    nombre=fila['nombre'],
                    especie=fila['especie'],
                    edad=fila['edad'],
                    adoptado=fila['adoptado'],
                    id=fila['id']
                )
                animales.append(animal)

        except mysql.connector.Error as e:
            vista().mostrar_mensaje_error(f"Se ha producido un error en MySQL: {e}")
        finally:
            cursor.close()
            conexion.close()
    return animales

def obtener_por_especie(especie: Especie) -> Animal:
    '''Método para obtener un animal por id'''
    # Creamos la conexión
    conexion = crear_conexion()
    animales = []

    if conexion:
        try:
            # Creamos el cursor
            cursor = conexion.cursor(dictionary=True)
            # Creamos la sentencia SQL
            sql = "SELECT * FROM animales WHERE especie = %s"
            # Ejecutamos la sentencia con la tupla del tipo de especie
            cursor.execute(sql, (especie,))
            # Traemos todos los resultados de la búsqueda
            resultado = cursor.fetchall()

            # Si hay resultados los transformamos del tabla a Lista de animales
            if resultado:
                for fila in resultado:
                    animal = Animal(
                        nombre = fila['nombre'],
                        especie = fila['especie'],
                        edad = fila['edad'],
                        adoptado = fila['adoptado'],
                        id = fila['id'],
                    )
                    animales.append(animal)

        except mysql.connector.Error as e:
            vista().mostrar_mensaje_error(f"Se ha producido un error en MySQL: {e}")
        finally:
            cursor.close()
            conexion.close()
    return animales

def obtener_animal_por_id(id: int) -> Animal:
    '''Método para obtener un animal por id'''
    # Creamos la conexión
    conexion = crear_conexion()
    animal = None

    if conexion:
        try:
            # Creamos el cursor
            cursor = conexion.cursor(dictionary=True)
            # Creamos la sentencia SQL
            sql = "SELECT * FROM animales WHERE id = %s"
            # Ejecutamos la query junto al la tupla de id
            cursor.execute(sql, (id,))
            # Traemos el resultado de la búsqueda
            resultado = cursor.fetchone()

            # Si existe resultado lo transformamos en un Animal
            if resultado:
                animal = Animal(
                    nombre = resultado['nombre'],
                    especie = resultado['especie'],
                    edad = resultado['edad'],
                    adoptado = resultado['adoptado'],
                    id = resultado['id'],
                )

        except mysql.connector.Error as e:
            vista().mostrar_mensaje_error(f"Se ha producido un error en MySQL: {e}")
        finally:
            cursor.close()
            conexion.close()
    return animal



def crear_animal(animal: Animal) -> bool:
    '''Método para crear animal'''
    # Crear conexión
    conexion = crear_conexion()
    resultado = False

    if conexion:
        try:
            # Creamos el cursor
            cursor = conexion.cursor(dictionary=True)
            # Creamos la sentencia SQL
            sql = "INSERT INTO animales (nombre, especie, edad, adoptado) VALUES (%s, %s, %s, %s)"
            # Creamos los valores a pasar
            valores = (animal.nombre, animal.especie, animal.edad, animal.adoptado)
            # Ejecutamos la sentencia SQL y los valores
            cursor.execute(sql, valores)
            # Guardamos los cambios
            conexion.commit()

            resultado = True
        except mysql.connector.Error as e:
            vista().mostrar_mensaje_error(f"Se ha producido un error en MySQL: {e}")
        finally:
            cursor.close()
            conexion.close()
    return resultado


def actualizar_animal(id: int, animal: Animal) -> bool:
    '''Método para actualizar animal'''
    # Creamos la conexión
    conexion = crear_conexion()
    resultado = False

    if conexion:
        try:
            # Creamos el cursor
            cursor = conexion.cursor(dictionary=True)
            # Creamos la sentencia SQL
            sql = "UPDATE animales SET nombre = %s, especie = %s, edad = %s, adoptado = %s WHERE id = %s"
            # Creamos los valores asociados
            valores = (animal.nombre, animal.especie, animal.edad, animal.adoptado, animal.id)

            # Ejecutamos la sentencia
            cursor.execute(sql, valores)
            # Guardamos los cambios
            conexion.commit()
            resultado = True
        except mysql.connector.Error as e:
            vista().mostrar_mensaje_error(f"Se ha producido un error en MySQL: {e}")
        finally:
            cursor.close()
            conexion.close()
    return resultado


def eliminar_animal(id: int) -> bool:
    '''Método para eliminar animal'''
    # Creamos la conexión
    conexion = crear_conexion()
    resultado = False

    if conexion:
        try:
            # Creamos el cursor
            cursor = conexion.cursor(dictionary=True)
            # Creamos la sentencia SQL
            sql = "DELETE FROM animales WHERE id = %s"
            # Ejecutamos la sentencia con la tupla de id
            cursor.execute(sql, (id,))
            # Guardamos los cambios
            conexion.commit()
            resultado = True
        except mysql.connector.Error as e:
            vista().mostrar_mensaje_error(f"Se ha producido un error en MySQL: {e}")
        finally:
            cursor.close()
            conexion.close()
    return resultado
