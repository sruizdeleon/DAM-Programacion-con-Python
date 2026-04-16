'''
Programa para añadir series y películas
'''
import utilidades as u
import series as s

# Tipos de elementos
TIPOS = ("Serie", "Película")
# Menú principal
MENU = '''
Menú
1. Ver todas las Series/Películas
2. Agregar nueva entrada
3. Eliminar una entrada
4. Buscar por título
5. Filtrar por género
6. Mostrar mejores Series/Peliculas
7. Salir

==| Escribe la opción: '''

# Funciones auxiliares para el menú

def ver_todas(diccionario: dict):
    '''
    Función para ver todas en el menú principal
    '''
    # Imprimimos el diccionario o vacío o con elementos
    print('''\n======== CATÁLOGO ========''')
    if len(diccionario) == 0:
        print(diccionario)
    else:
        for d in diccionario.items():
            print(d)


def definir_generos():
    '''
    Helper para definir los géneros
    '''
    generos = []
    genero = ""
    # Recogemos parámetros
    while(True):
        genero = u.pedir_string(f"\n==| Escribe un género o escribe 'Salir' volver {generos}: ")
        # Salir
        if genero == "salir" or genero == "Salir":
            # Tiene que haber por lo menos un género para salir
            if len(generos) > 0:
                break
            print(f"\nERROR - Debes añadir al menos un género.")
        # Si ya se añadió ese género
        elif genero in generos:
            print(f"\nERROR - Ya exite el genero {genero}")
        # Lo añadimos a la lista
        else:
            generos.append(genero)
    return generos


def definir_tipo():
    '''
    Helper para definir el tipo
    '''
    while(True):
        # Pedimos el tipo
        tipo = u.pedir_string("\n==| Escribe el tipo (Serie o Película): ")
        # Comprobamos que el tipo corresponda con nuestra tupla de opciones
        for t in TIPOS:
            if t == tipo:
                return tipo
        print(f"\nERROR - No has introducido una opción válida.")



def agregar_nueva_entrada(diccionario: dict):
    '''
    Función para agregar nueva entrada en el menú principal
    '''
    # Pedimos el titulo
    titulo = u.pedir_string("\n==| Escribe el título: ")
    # Si no existe el título
    if s.buscar_por_titulo(diccionario, titulo) is False:
        # Solicitamos los datos
        tipo = definir_tipo()
        genero = definir_generos()
        year = u.pedir_entero_entre("\n==| Escribe el año entre 1900 y 2026: ", 1900, 2026)
        valoracion = u.pedir_decimal_entre("\n==| Escribe la valoración del 0 al 10: ", 0, 10)
        comentario = u.pedir_string("\n==| Escribe un comentario relacionado: ")
        # Agregamos el elemento
        if s.agregar(diccionario, titulo, tipo, genero, year, valoracion, comentario):
            print(f"\nSUCCESS - {tipo} con titulo {titulo} fua añadida correctamente.")
        else:
            print(f"\nERROR - No se pudo añadir el elemento {titulo}.")
    else:
        print(f"\nERROR - {titulo} ya existe en el catálogo")


def eliminar_una_entrada(diccionario: dict):
    '''
    Función para eliminar una entrada en el menú principal
    '''
    # Solicitamos el título
    titulo = u.pedir_string("\n==| Escribe el titulo a eliminar: " )
    # Si se elimina correctamente
    if s.eliminar(diccionario, titulo):
        print(f"\nSUCCESS - elemento {titulo} fue eliminado correctamente.")
    # Si no se encontró el elemento
    else:
        print(f"\nERROR - No se pudo añadir el elemento {titulo}.")



def buscar_titulo(diccionario: dict):
    '''
    Función para buscar por título en el menú principal
    '''
    # Pedimos el título
    titulo = u.pedir_string("\n==| Escribe el titulo a buscar: ")
    # Buscamos el elemento
    elemento = s.buscar_por_titulo(diccionario, titulo)
    # Si no se encuentra el elemento
    if elemento is False:
        print(f"\nERROR - No existe el elemento: {titulo}")
    # Si se encuentra el elemento
    else:
        print(f"=========== ELEMENTO ============")
        print(elemento)


def filtrar_genero(diccionario: dict):
    '''
    Función para filtrar por género en el menú principal
    '''
    # Solicitamos el género
    genero = u.pedir_string("\n==| Escribe el género por el qué buscar: ")
    # Filtramos los elementos
    elementos = s.filtrar_por_genero(diccionario, genero)
    # Si no hay elementos en la lista error
    if not elementos:
        print(f"\nERROR - No existen elementos con género: {genero}")
    # Si hay elementos en la lista mostramos
    else:
        print(f"\n=========== ELEMENTOS GENERO = {genero} ============")
        for e in elementos.items():
            print(e)


def mostar_mejores(diccionario: dict):
    '''
    Función para mostrar los mejor valorados en el menú principal
    '''
    # Creamos la el diccionario
    mejores_elementos = {}
    while(True):
        # Solicitamos si quiere limitar el tamaño de búsqueda
        quiere_cantidad = u.pedir_string("\n==| ¿Quieres algún límite de resultados? Escribe Sí o No: ")
        # Si quiere limitar
        if(quiere_cantidad == "Sí" or quiere_cantidad == "Si" or quiere_cantidad == "SI" or quiere_cantidad == "SÍ"):
            # Pedimos cantidad
            cantidad = u.pedir_entero("\n==| Escribe el número de elementos a mostrar: ")
            # Extramos el diccionario ordenado por valoración y limitado
            mejores_elementos = s.mostrar_mejores(diccionario, cantidad)
            break
        # Si no quiere limitar
        elif(quiere_cantidad == "No" or quiere_cantidad == "NO"):
            # Extramos el diccionario ordenado por valoración
            mejores_elementos = s.mostrar_mejores(diccionario)
            break
        # Si no da una respuesta válida
        else:
            print(f"\nERROR - No has introducido una respuesta válida.")

    # Si hay elementos elementos mostramos
    if len(mejores_elementos) > 0:
        print(f"\n=========== MEJOR VALORADOS ============")
        for e in mejores_elementos:
            print(e)
    # Si no hay elementos error
    else:
        print(f"\nERROR - No existen elementos")



# Función de programa principal
def main():
    '''
    Programa principal
    '''
    # Creamos el diccionario = catálogo
    catalogo = dict()
    # Añadimos unos datos para pruebas
    catalogo['Titanic'] = {'tipo': 'Película', 'genero': ['Drama', 'Romance'], 'year': 1997, 'valoracion': 10.0, 'comentario': 'Puesto 39'}
    catalogo['Interstellar'] = {'tipo': 'Serie', 'genero': ['Science-Fiction', 'Action & Adventure', 'Comedy', 'Crime', 'Drama'], 'year': 2026, 'valoracion': 9.5, 'comentario': 'Puesto 1'}
    catalogo['The Boys'] = {'tipo': 'Película', 'genero': ['Drama', 'Science-Fiction', 'Action & Adventure'], 'year': 2014, 'valoracion': 9.6, 'comentario': 'Puesto 21'}

    # Iniciamos el programa
    while(True):
        # Solicitamos opción
        opcion = u.pedir_entero_entre(MENU, 1, 7)
        # Ejecutamos las opciones auxiliares del menú
        if opcion == 1:
            ver_todas(catalogo)
        elif opcion == 2:
            agregar_nueva_entrada(catalogo)
        elif opcion == 3:
            eliminar_una_entrada(catalogo)
        elif opcion == 4:
            buscar_titulo(catalogo)
        elif opcion == 5:
            filtrar_genero(catalogo)
        elif opcion == 6:
            mostar_mejores(catalogo)
        elif opcion == 7:
            break

# Lanzamos el programa principal
main()
