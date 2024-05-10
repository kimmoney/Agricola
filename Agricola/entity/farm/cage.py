from entity.farm.animal_type import AnimalType
from entity.farm.field import Field


class Cage(Field):
    def __init__(self, position):
        self._kind = AnimalType.NONE
        self._count = 0
        self._maximum = 0
        self._barn = False
        self._position = position


