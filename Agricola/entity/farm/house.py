from entity.farm.field import Field

'''
집 구상 클래스
'''


class House(Field):
    def __init__(self, position):
        self._position = position
