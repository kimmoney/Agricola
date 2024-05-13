"""
농장의 상태
"""
from entity.animal_type import AnimalType
from entity.farm.none_field import NoneField
from entity.house_type import HouseType


class Farm:
    def __init__(self):
        self.house_status = HouseType.WOOD
        self.field = [[NoneField() for i in range(5)] for j in range(3)]
        self.fence = [[NoneField() for i in range(6)] for j in range(4)]
        self.pet = AnimalType.NONE
