'''
Archivo para crear la conexión con MySQL
'''

import mysql.connector
from mysql.connector import Error
import config

def crear_conexion():
    '''Establece y devuelve la conexión con la bbdd'''
    try:
        # Creamos la conexión con los datos de configuración
        conexion = mysql.connector.connect(
            host = config.HOST,
            user = config.USER,
            password = config.PASSWORD,
            database = config.DATABASE
        )

        # Comprobamos la conexión y la devolvemos si es correcta
        if conexion.is_connected():
            return conexion

    # Si hay un error de conexión lo mostramos y no devolvemos nada
    except Error as e:
        print(f"ERROR - No se pudo conectar a la base de datos: {e}")
        return None
