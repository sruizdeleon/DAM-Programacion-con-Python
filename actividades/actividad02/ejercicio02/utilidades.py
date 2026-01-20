'''
Docstring para actividades.actividad02.ejercicio02.utilidades
'''

def pedir_saldo_inicial(instruccion: str) -> float:
    "Pide el saldo inicial de la cuenta al usuario hasta que se proporcione uno válido y lo devuelve."
    while True:
        texto = input(instruccion)
        try:
            decimal = float(texto)
            return decimal
        except ValueError:
            print("ERROR: no has proporcionado un número decimal válido (Ejemplo: 1000.50)")

def pedir_operacion(instruccion: str) -> str:
    "Pide la operación a realizar al usuario (ingreso, reintegro o salir)."
    while True:
        texto = input(instruccion)
        try:
            operacion = int(texto[0])
            if 1 <= operacion <= 5:
                return operacion
            else:
                print("ERROR: no has proporcionado una opción válida.")
        except (ValueError, IndexError):
            print("ERROR: no has proporcionado una opción válida.")

def ingresar(instruccion: str, saldo: float) -> float:
    "Realiza un ingreso en la cuenta y devuelve el nuevo saldo."
    while True:
        texto = input(instruccion)
        try:
            cantidad = float(texto)
            if cantidad < 0:
                raise ValueError("La cantidad a ingresar no puede ser negativa.")
            saldo += cantidad
            mostrar_saldo(saldo)
            return saldo
        except ValueError as e:
            print(f"ERROR: {e if str(e) else 'No has proporcionado un número decimal válido (Ejemplo: 1000.50)'}")

def retirar(instruccion: str, saldo: float) -> float:
    "Realiza una retirada en la cuenta y devuelve el nuevo saldo."
    while True:
        texto = input(instruccion)
        try:
            cantidad = float(texto)
            if cantidad < 0:
                raise ValueError("La cantidad a retirar no puede ser negativa.")
            if cantidad > saldo:
                raise ValueError("No hay suficiente saldo para realizar la retirada.")
            saldo -= cantidad
            mostrar_saldo(saldo)
            return saldo
        except ValueError as e:
            print(f"ERROR: {e if str(e) else 'No has proporcionado un número decimal válido (Ejemplo: 1000.50)'}")

def mostrar_saldo(saldo: float) -> None:
    "Muestra el saldo actual de la cuenta."
    print(f"Saldo actual en cuenta: {saldo:.2f} €")

def estadisticas(ingresos: int, retiradas: int) -> None:
    "Muestra las estadísticas de operaciones realizadas."
    print("\n---/ Estadísticas de operaciones /---")
    print(f"Ingresos: {ingresos}")
    print(f"Retiradas: {retiradas}")
