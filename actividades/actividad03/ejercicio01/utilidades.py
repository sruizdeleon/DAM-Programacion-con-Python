'''
Docstring para actividades.actividad01.ejercicio02.utilidades

'''

# Utilidades para pedir datos

# Enteros
def pedir_entero(instruccion: str) -> int:
    '''
    Pide un número entero al usuario hasta que se proporcione uno válido y lo devuelve.
    '''
    while True:
        texto = input(instruccion)
        try:
            entero = int(texto)
            return entero
        except ValueError:
            print("ERROR: no has proporcionado un número entero válido (Ejemplo: 1)")

# Decimales
def pedir_decimal(instruccion: str) -> float:
    "Pide un número decimal al usuario hasta que se proporcione uno válido y lo devuelve."
    while True:
        texto = input(instruccion)
        try:
            decimal = float(texto)
            return decimal
        except ValueError:
            print("ERROR: no has proporcionado un número decimal válido (Ejemplo: 1.5)")

# Booleanos
def pedir_booleano(instruccion: str) -> bool:
    '''
    Pide un booleano al usuario en formato 1=true o 0=false
    hasta que se proporcione uno y lo devuelve
    '''
    while True:
        texto = input(instruccion)
        try:
            entero = int(texto)
            if entero == 1:
                return True
            elif entero == 0:
                return False
            else:
                print("ERROR: no has proporcionado un valor válido (1=Sí o 0=No)")
        except ValueError:
            print("ERROR: no has proporcionado un número entero válido (1=Sí o 0=No)")

# Cadenas
def pedir_string(instruccion: str) -> str:
    '''
    Pide una cadena de texto al usuario la valida y devuelve la cadena
    '''
    while True:
        texto = input(instruccion)
        try:
            cadena = str(texto)
            return cadena
        except ValueError:
            print("ERROR: no has proporcionado una cadena de texto válida.")


# Utilidades para validación de datos
def validacion_entero_positivo(entero: int) -> bool:
    '''
    Valida que un entero sea positivo, mayor o igual que 0.
    '''
    return entero >= 0

def validacion_entero_negativo(entero: int) -> bool:
    '''
    Valida que un entero sea negativo, menor que 0.
    '''
    return entero < 0

def validacion_decimal_positivo(decimal: float) -> bool:
    '''
    Valida que un decimal sea positivo, mayor o igual que 0.
    '''
    return decimal >= 0

def validacion_decimal_negativo(decimal: float) -> bool:
    '''
    Valida que un decimal sea negativo, menor que 0.
    '''
    return decimal < 0

def validacion_formato_booleano(entero: int) -> bool:
    '''
    Valida booleanos por medio de 0 -> false y 1 -> true.
    '''
    return entero == 1 or entero == 0

def validacion_porcentaje(decimal: float) -> bool:
    '''
    Valida un porcentaje en formato decimal entre 0 y 1.
    '''
    return 0 <= decimal <= 1
