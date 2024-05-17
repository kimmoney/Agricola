from entity.crop_type import CropType
from entity.farm.field import Field
from entity.field_type import FieldType

'''
경작지
position : 위치
type : 쌓인 작물의 종류
stack : 쌓인 작물의 갯수
'''


class ArableLand(Field):
    def __init__(self, position):
        self.field_type = FieldType.ARABLE
        self._position = position
        self._stack = 0
        self._type = CropType.NONE
