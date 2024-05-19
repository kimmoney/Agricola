"""
동물의 이동을 검증하는 클래스
:param: 필드(7*11), 포지션
:return: 동물의 이동 가능 여부
"""
from collections import deque
from copy import copy

from behavior.behavior import Behavior
from entity.field_type import FieldType


class AnimalMoveValidation(Behavior):
    def __init__(self, field_status, animal_type, position):
        self.field_status = copy(field_status)
        self.animal_type = animal_type
        self.position = position

    def execute(self):
        pass

    def check_already_placed(self):
        pass

    def check_same_type(self):
        expanded_field_status = [[FieldType.NONE_FIELD for i in range(9)] for j in range(13)]
        check = [[0 for i in range(9)] for j in range(13)]
        for i, item in enumerate(self.field_status):
            for j, value in enumerate(item):
                expanded_field_status[i + 1][j + 1] = value
        queue = deque()
        check[self.position[0]][self.position[1]] = 1
        queue.append((self.position[0], self.position[1]))
        while queue:
            x, y = queue.popleft()
            dx = [0, 0, -1, 1]
            dy = [-1, 1, 0, 0]
            for i in range(4):
                p = x + dx[i]
                q = y + dy[i]
                r = p + dx[i]
                s = q + dy[i]
                if 0 <= r < 9 and 0 <= s < 13 and check[r][s] == 0 and expanded_field_status[p][q] != FieldType.FENCE:
                    check[r][s] = 1
                    queue.append((r, s))
        for i in range(0, 9, 2):
            for j in range(0, 13, 2):
                if check[i][j] == 0 and expanded_field_status[i][j] != FieldType.NONE_FIELD and \
                        expanded_field_status[i][j] != FieldType.CAGE:
                    self.log_text = "울타리 안에는 외양간을 제외한 다른 구조물이 있을 수 없습니다."
                    return False
        return True

    def log(self):
        pass

"""
1. 집, 밭, 다른 동물이 존재하는 곳 여부
2. 동물 같은 종류 여부
"""