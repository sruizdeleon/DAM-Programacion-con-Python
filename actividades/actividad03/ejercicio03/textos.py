'''
Modulo para tratamiento de textos
'''
def contar_palabras(cadena:str, caracteres_no_validos:str) -> int:
    '''
    Devuelve el número de palabras de una cadena de texto
    eliminando los caracteres dados en caracteres no válidos
    '''
    cadena_limpia = reemplazar_caracteres(cadena, caracteres_no_validos, " ")
    palabras = cadena_limpia.strip().split()
    numero_palabras = len(palabras)
    return numero_palabras


def reemplazar_caracteres(cadena: str, caracteres_reemplazo: str, caracter_nuevo: str) -> str:
    '''
    Devuelve un la cadena de texto reemplazando todos los caracteres
    de la lista por el caracter nuevo
    '''
    if len(cadena) == 0:
        return ""
    nueva_cadena = cadena
    for c in caracteres_reemplazo:
        nueva_cadena = nueva_cadena.replace(c, caracter_nuevo)
    return nueva_cadena



def caracteres_total(cadena: str, caracteres_no_validos: str) -> int:
    '''
    Devuelve el número total de caracteres en una cadena,
    excluyendo los caracteres no válidos aportados.
    '''
    cadena_limpia = reemplazar_caracteres(cadena, caracteres_no_validos, "")
    numero_caracteres = len(cadena_limpia)
    return numero_caracteres


def palabra_mas_larga(cadena:str) -> str:
    '''
    Devuelve la palanbra más larga de una cadena de texto dada o vacio.
    '''
    CARACTERES_NO_VALIDOS = ".,;:¡!¿?()[]\""
    cadena_limpia = reemplazar_caracteres(cadena, CARACTERES_NO_VALIDOS, " ")
    palabras = cadena_limpia.strip().split()
    palabra_larga = ""
    for p in palabras:
        if len(p) > len(palabra_larga):
            palabra_larga = p
    return palabra_larga

def invertir_cadena(cadena: str) -> str:
    '''
    Devuelve la cadena invertida
    '''
    if len(cadena) <= 1:
        return cadena
    return cadena[-1] + invertir_cadena(cadena[0:(len(cadena)-1)])

def ordenar_lista(lista: list[int]) -> list[int]:
    '''
    Ordena una lista de enteros
    '''
    # Método Burbuja: elegido porque es una manera sencilla de abordar la ordenación
    # sólo intercambias posiciones desplazando el elemento mayor al final de la lista
    lista_ordenada = lista.copy()
    largo = len(lista)
    for i in range(0, largo - 1):
        for j in range(0, largo - 1):
            if lista_ordenada[j] > lista_ordenada[j+1]:
                aux = lista_ordenada[j+1]
                lista_ordenada[j+1] = lista_ordenada[j]
                lista_ordenada[j] = aux
    return lista_ordenada

def busqueda_binaria(lista, elemento, inicio, fin) -> int:
    '''
    Busca la posición de un elemento por búsqueda binaria
    '''
    if inicio > fin:
        return -1

    medio = (inicio + fin) // 2
    if elemento == lista[medio]:
        return medio

    if elemento < lista[medio]:
        return busqueda_binaria(lista, elemento, inicio, medio - 1)
    else:
        return busqueda_binaria(lista, elemento, medio + 1, fin)
