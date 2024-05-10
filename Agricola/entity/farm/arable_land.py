from entity.farm.field import Field


class ArableLand(Field):
    def __init__(self, position):
        self._position = position
        self._stack = 0
