"""
농장의 상태
"""
from entity.animal_type import AnimalType
from entity.farm.none_field import NoneField
from entity.house_type import HouseType


class Farm:
    def __init__(self):
        self.observers = []
        self.house_status = HouseType.WOOD
        self.field = [[NoneField() for i in range(5)] for j in range(3)]
        self.fence = [[NoneField() for i in range(6)] for j in range(4)]
        self.pet = AnimalType.NONE

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_house_status(self, house_status):
        self.house_status = house_status
        self.notify()

    def set_field(self, row, col, field):
        self.field[row][col] = field
        self.notify()

    def set_fence(self, row, col, fence):
        self.fence[row][col] = fence
        self.notify()

    def set_pet(self, pet):
        self.pet = pet
        self.notify()