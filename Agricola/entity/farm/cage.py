from entity.farm.animal_type import AnimalType
from entity.farm.field import Field

'''
울타리 정보
한 칸별로 생성
한칸당 최대 2마리까지 수용
외양간 존재 시 4마리까지 수용
'''
class Cage(Field):
    def __init__(self, position):
        self._kind = AnimalType.NONE
        self._count = 0
        self._maximum = 0
        self._barn = False
        self._position = position


