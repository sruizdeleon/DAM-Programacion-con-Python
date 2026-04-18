'''
Archivo para organizar las clases y tipos de Centrales
'''

from abc import ABC
from modelo_energia import TipoCombustible, TipoMaterial

class Central(ABC):
    '''Clase padre de Central que heredan el resto de hijos de tipo de centrales'''
    def __init__(self, nombre: str, kwh: int, ubicacion: str):
        self._nombre = nombre
        if kwh < 0:
            raise ValueError("ERROR - La producción no puede ser negativa")
        self._kwh = kwh
        self._ubicacion = ubicacion

    def __str__(self):
        return f"CENTRAL con nombre {self._nombre},se ubica en {self._ubicacion} y produce {self._kwh} kWh"

    @property
    def nombre(self):
        '''Obtener nombre'''
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        '''Registrar nombre'''
        self._nombre = nombre

    @property
    def kwh(self):
        '''Obtener kwh'''
        return self._kwh
    @kwh.setter
    def kwh(self, kwh):
        '''Registrar kwh'''
        if kwh < 0:
            raise ValueError("ERROR - La producción no puede ser negativa")
        self._kwh = kwh

    @property
    def ubicacion(self):
        '''Obtener ubicacion'''
        return self._ubicacion
    @ubicacion.setter
    def ubicacion(self, ubicacion):
        '''Registrar ubicacion'''
        self._ubicacion = ubicacion





class CentralTermica(Central):
    '''Clase hija de Central que define una Central Térmica'''
    def __init__(self, nombre: str, kwh: int, ubicacion: str, combustible: str):
        super().__init__(nombre, kwh, ubicacion)
        if combustible not in TipoCombustible:
            raise ValueError(f"ERROR - No has introduccido un combustible válido. {TipoCombustible}")
        self._combustible = combustible

    def __str__(self):
        return f"{super().__str__()} y usa de combustible {self._combustible}"

    @property
    def combustible(self):
        '''Obtener combustible'''
        return self._combustible

    @combustible.setter
    def combustible(self, combustible):
        '''Registrar combustible'''
        self._combustible = combustible



class CentralNuclear(Central):
    '''Clase hija de Central que define una Central Nuclear'''
    def __init__(self, nombre: str, kwh: int, ubicacion: str, material: str):
        super().__init__(nombre, kwh, ubicacion)
        if material not in TipoMaterial:
            raise ValueError(f"ERROR - No has introduccido un material válido. {TipoMaterial}")
        self._material = material

    def __str__(self):
        return f"{super().__str__()} y usa de material {self._material}"

    @property
    def material(self):
        '''Obtener material'''
        return self._material

    @material.setter
    def material(self, material):
        '''Registrar material'''
        self._material = material
