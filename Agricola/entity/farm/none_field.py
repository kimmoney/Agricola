"""
null값의 역할을 수행하는 noneField
"""
from entity.farm.field import Field
from entity.field_type import FieldType


class NoneField(Field):
    def __init__(self):
        self.value = FieldType.NONE_FIELD
