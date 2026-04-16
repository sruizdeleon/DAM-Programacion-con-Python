'''
Doctype CRUD para películas y series
'''
def agregar(diccionario: dict, titulo: str, tipo: str, genero: list, year: int, valoracion: float, comentario: str):
    '''
    Función para agregar un nuevo elemento (Pelicula o Serie) al listado
    '''
    if buscar_por_titulo(diccionario, titulo) is False:
        # Creamos el diccionario de detalles
        detalles = {
            "tipo": tipo,
            "genero": genero,
            "year": year,
            "valoracion": valoracion,
            "comentario": comentario
        }
        # Añadimos al diccionario con el título
        diccionario[titulo] = detalles
        return True
    else:
        return False


def eliminar(diccionario: dict, titulo: str):
    '''
    Función para eliminar elemento
    '''
    # Buscamos en el diccionario por título
    # Si no existe devolvemos False
    if buscar_por_titulo(diccionario, titulo) is False:
        return False
    # Si existe borramos el elemento
    else:
        del diccionario[titulo]
        # Comprobamos que se borre
        if buscar_por_titulo(diccionario, titulo) is False:
            return True
        else:
            return False

def buscar_por_titulo(diccionario: dict, titulo: str):
    '''
    Funcion para buscar elemento por título
    '''
    # Buscamos el elemento
    resultado = diccionario.get(titulo, "No encontrado")
    # Si no se encuentra devolvemos False
    if resultado == "No encontrado":
        return False
    # Si se encuentra devolvemos el elemento
    else:
        return resultado


def actualizar_valoracion(diccionario: dict, titulo: str, valoracion: float):
    '''
    Función para actualizar valoración
    '''
    # Buscamos el elemento
    # Si no se encuentra False
    if buscar_por_titulo(diccionario, titulo) is False:
        return False
    # Si se encuentra extraemos la valoración y la actualizamos
    else:
        detalles = diccionario.get(titulo)
        detalles["valoracion"] = valoracion
        diccionario[titulo] = detalles
        return True


def filtrar_por_genero(diccionario: dict, genero: str):
    '''
    Función para filtrar elementos por género
    '''
    # Filtramos por género
    resultados = dict(filter(lambda item: genero in item[1]['genero'], diccionario.items()))
    return resultados

def mostrar_mejores(diccionario: dict, n: int = 0):
    '''
    Función para obtener los n elementos con mejor valoracion
    '''
    # Ordenamos el diccionario por valoración
    diccionario_ordenado = sorted(diccionario.items(), key=lambda item: item[1]['valoracion'], reverse=True)
    # Si hay limitación de resultados y es menor o igual a 0 o mayor que el largo del diccionario devolvemos entero
    if n <= 0 or n > len(diccionario_ordenado):
        return diccionario_ordenado
    # Si no devolvemos el diccionario limitado a la cantidad
    resultado = list(filter(lambda i: diccionario_ordenado.index(i) < n, diccionario_ordenado))
    return resultado
