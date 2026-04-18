'''
Control y gestión de centrales
'''
from modelo_central import Central, CentralNuclear, CentralTermica
from modelo_energia import TipoMaterial, TipoCombustible

class GestionCentrales:
    '''Clase que almacena centrales y gestiona su acceso'''
    def __init__(self):
        self.centrales = []

    def existe_nombre(self, nombre_nuevo: str) -> bool:
        '''Método para comprobar si existe el nombre en algun central existente'''
        for central in self.centrales:
            if nombre_nuevo == central.nombre:
                return True
        return False



    def agregar_central(self, nueva_central: Central):
        '''Método para agregar una nueva central al sistema'''
        if not self.existe_nombre(nueva_central.nombre):
            self.centrales.append(nueva_central)
        print("ERROR - Ya existe una central con ese nombre")

    def obtener_centrales(self):
        '''Método para obtener todas las centrales'''
        return self.centrales

    def mostrar_centrales(self) -> None:
        '''Muestra por pantalla la información de todos los tipos de centrales'''
        print("============CENTRALES=============")
        n = 1
        for central in self.centrales:
            print(f"==| ({n}) {central}")
            n += 1

    def obtener_produccion(self) -> int:
        '''Devuelve la producción total de todas las centrales'''
        total_produccion = 0
        for central in self.centrales:
            total_produccion += central.kwh
        return total_produccion

    def obtener_produccion_central(self, nombre) -> int:
        '''Devuelve la producción de una central por su nombre'''
        total_produccion = 0
        for central in self.centrales:
            if central.nombre == nombre:
                total_produccion = central.kwh
        return total_produccion

    def obtener_central_mayor_produccion(self) -> int:
        '''Devuelve la central con mayor producción o nulo'''
        central_mayor_produccion = None
        mayor_produccion = 0
        for central in self.centrales:
            if central.kwh > mayor_produccion:
                central_mayor_produccion = central
        return central_mayor_produccion

    def obtener_centrales_termicas(self) -> list:
        '''Devuleve una lista de centrales térmicas o lista vacía'''
        centrales_termicas = []
        for central in self.centrales:
            if isinstance(central, CentralTermica):
                centrales_termicas.append(central)
        return centrales_termicas

    def obtener_centrales_termicas_por_combustible(self, combustible) -> list:
        '''Devuleve una lista de centrales térmicas filtrada por combustible o lista vacía'''
        centrales_termicas = []
        valores_permitidos = [energia.value for energia in TipoCombustible]
        if combustible not in valores_permitidos:
            raise ValueError(f"ERROR - No has introducido un combustible válido. {TipoCombustible}")
        for central in self.centrales:
            if isinstance(central, CentralTermica) and central.combustible == combustible:
                centrales_termicas.append(central)
        return centrales_termicas

    def obtener_produccion_centrales_termicas(self) -> int:
        '''Devuleve la producción de centrales térmicas o nulo'''
        centrales_termicas = self.obtener_centrales_termicas()
        total_produccion = 0
        for central in centrales_termicas:
            total_produccion += central.kwh
        return total_produccion

    def obtener_centrales_nucleares(self) -> list:
        '''Devuleve una lista de centrales nucleares o lista vacía'''
        centrales_nucleares = []
        for central in self.centrales:
            if isinstance(central, CentralNuclear):
                centrales_nucleares.append(central)
        return centrales_nucleares

    def obtener_centrales_nucleares_por_material(self, material) -> list:
        '''Devuleve una lista de centrales nucleares filtrada por material o lista vacía'''
        centrales_nucleares = []
        valores_permitidos = [energia.value for energia in TipoMaterial]
        if material not in valores_permitidos:
            raise ValueError(f"ERROR - No has introducido un material válido. {TipoMaterial}")
        for central in self.centrales:
            if isinstance(central, CentralNuclear) and material == central.material:
                centrales_nucleares.append(central)
        return centrales_nucleares

    def obtener_produccion_centrales_nucleares(self) -> int:
        '''Devuleve la producción de centrales nucleares o nulo'''
        centrales_nucleares = self.obtener_centrales_nucleares()
        total_produccion = 0
        for central in centrales_nucleares:
            total_produccion += central.kwh
        return total_produccion
