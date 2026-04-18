'''
Clases para definir el modelo de energía que utiliza cada tipo de central
'''
from enum import Enum

class TipoEnergia(Enum):
    '''Clase para albergar todos los tipos de energías'''


class TipoCombustible(TipoEnergia):
    '''Clase que define los tipos de combustible de una Central Térmica'''
    PETROLEO = "petróleo"
    GAS = "gas"
    CARBON = "carbón"

    def __str__(self):
        return f"Combustibles: {self.PETROLEO} | {self.GAS} | {self.CARBON}"


class TipoMaterial(TipoEnergia):
    '''Clase que define los tipos de materiales de una Central Nuclear'''
    URANIO = "uranio"
    PLUTONIO = "plutonio"
    NEPTUNIO = "neptunio"

    def __str__(self):
        return f"Materiales: {self.URANIO} | {self.PLUTONIO} | {self.NEPTUNIO}"
