from entity.farm.crop_type import CropType
from entity.farm.field import Field

'''
경작지
position : 위치
type : 쌓인 작물의 종류
stack : 쌓인 작물의 갯수
'''
class ArableLand(Field):
    def __init__(self, position):
        self._position = position
        self._stack = 0
        self._type = CropType.NONE
