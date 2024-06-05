"""
null값의 역할을 수행하는 noneField
"""
from entity.animal_type import AnimalType
from entity.farm.field import Field
from entity.field_type import FieldType
from entity.crop_type import CropType


class NoneField(Field):
    def __init__(self):
        self.field_type = FieldType.CAGE
        self.kind = CropType.NONE
        self.count = 0
        self.maximum = 0
        self.barn = False
