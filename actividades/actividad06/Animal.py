'''Clase Animal'''

from enum import Enum


class Especie (Enum):
    '''Clase que define los distintos tipos de especie admitidos'''
    PERRO = 'perro'
    GATO = 'gato'
    CONEJO = 'conejo'

class Animal:
    '''Clase Animal'''
    def __init__(self, nombre: str, especie: Especie, edad: int, adoptado: bool, id: int = None):
        '''Constructor de Animal'''
        self._id = id
        self._nombre = nombre
        self._especie = especie
        self._edad = edad
        self._adoptado = adoptado

    def __str__(self):
        return f"({self.id}) - {self._nombre} es un {self._especie} tiene {self._edad} años y {"está adoptado" if self._adoptado else "no está adoptado"}"


    # GETTERS
    @property
    def id(self):
        '''Getter de id'''
        return self._id
    @property
    def nombre(self):
        '''Getter de nombre'''
        return self._nombre
    @property
    def especie(self):
        '''Getter de especie'''
        return self._especie
    @property
    def edad(self):
        '''Getter de edad'''
        return self._edad
    @property
    def adoptado(self):
        '''Getter de adoptado'''
        return self._adoptado

    # SETTERS
    @id.setter
    def id(self, valor: int):
        '''Setter de id'''
        self._id = valor
    @nombre.setter
    def nombre(self, valor: str):
        '''Setter de nombre'''
        self._nombre = valor
    @edad.setter
    def edad(self, valor: int):
        '''Setter de edad'''
        self._edad = valor
    @especie.setter
    def especie(self, valor: Especie):
        '''Setter de especie'''
        self._especie = valor
    @adoptado.setter
    def adoptado(self, valor: bool):
        '''Setter de adoptado'''
        self._adoptado = valor
