"""
울타리 + 우리 생성 클래스
:param: 변경하고자 하는 필드 상태 (3*5 field), vertical fence 상태, horizontal fence 상태
:return: 우리 생성 성공 여부
:rtype: bool
우리 생성 및 max 값 조정
농장 상태 업데이트도 수행되어야 함
"""
import copy
from collections import deque
from typing import List

from command import Command
from entity.farm.cage import Cage
from entity.farm.field import Field
from entity.farm.none_field import NoneField
from entity.field_type import FieldType
from fence_validation import FenceValidation
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository


# Todo

class ConstructFence(Command):

    def __init__(self, field_status, vertical_fence, horizontal_fence):
        self.field_status = copy.deepcopy(field_status)
        self.vertical_fence = copy.deepcopy(vertical_fence)
        self.horizontal_fence = copy.deepcopy(horizontal_fence)
        self.log_text = None

    def execute(self):
        expanded_field = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
        for i in range(3):
            for j in range(6):
                if self.vertical_fence is True:
                    expanded_field[i * 2 + 1][2 * j] = FieldType.FENCE
        for i in range(4):
            for j in range(5):
                if self.horizontal_fence is True:
                    expanded_field[i * 2][j * 2 + 1] = FieldType.FENCE
        for i in range(3):
            for j in range(5):
                expanded_field[i * 2 + 1][j * 2 + 1] = self.field_status[i][j].field_type
        fence_validation = FenceValidation(expanded_field)
        if fence_validation.execute():
            self.log_text = "울타리 건설 성공"
            self.create_cage()
            return True
        else:
            self.log_text = "울타리 건설 검증에 실패했습니다"
            return False

    def create_cage(self):
        expanded_field: List[List[Field]] = [[NoneField() for i in range(13)] for i in range(9)]
        for i in range(3):
            for j in range(6):
                if self.vertical_fence is True:
                    expanded_field[i * 2 + 2][2 * j + 1].field_type = FieldType.FENCE
        for i in range(4):
            for j in range(5):
                if self.horizontal_fence is True:
                    expanded_field[i * 2 + 1][j * 2 + 2].field_type = FieldType.FENCE
        for i in range(3):
            for j in range(5):
                expanded_field[i * 2 + 3][j * 2 + 3] = self.field_status[i][j]
        # 1. 우리 안과 우리 밖 구분하기
        queue = deque()
        deque.append((0, 0))
        check = [[False for _ in range(13)] for __ in range(9)]
        check[0][0] = True
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        while not queue:
            x, y = queue.popleft()
            for k in range(4):
                p = x + dx[k] + dx[k]
                q = y + dy[k] + dy[k]
                pp = x + dx[k]
                qq = y + dy[k]
                if 0 <= p < 9 and 0 <= q < 13 and expanded_field[pp][qq].field_type != FieldType.FENCE and not check[p][q]:
                    check[p][q] = True
                    queue.append((p, q))
        # 2. 우리 안 Cage() 객체 생성해야됨 -> 기존 객체의 정보를 그대로 담아야 함.
        for i in range(9):
            for j in range(13):
                if not check[i][j] and isinstance(expanded_field[i][j], NoneField):
                    new_field = Cage()
                    new_field.barn = expanded_field[i][j].barn
                    expanded_field[i][j] = new_field
        # 3. maximum 값 조정하기
        check2 = [[False for _ in range(13)] for __ in range(9)]
        for i in range(9):
            for j in range(13):
                if i % 2 == 0 and j % 2 == 0 and not check[i][j]:
                    check[i][j] = True
                    check2[i][j] = True
                    barn_count = 0
                    if expanded_field[i][j].barn:
                        barn_count += 1
                    queue.append((i, j))
                    while not queue:
                        x, y = queue.popleft()
                        for k in range(4):
                            p = x + dx[k] + dx[k]
                            q = y + dy[k] + dy[k]
                            pp = x + dx[k]
                            qq = y + dy[k]
                            if 0 <= p < 9 and 0 <= q < 13 and expanded_field[pp][qq].field_type != FieldType.FENCE and not check2[p][q]:
                                check[p][q] = True
                                check2[p][q] = True
                                queue.append((p, q))
                                if expanded_field[p][q].barn:
                                    barn_count += 1
                    maximum = 2**barn_count * 2
                    check3 = [[False for _ in range(13)] for __ in range(9)]
                    queue.append((i, j))
                    check3[i][j] = True
                    expanded_field[i][j].maximum = maximum
                    while not queue:
                        x, y = queue.popleft()
                        for k in range(4):
                            p = x + dx[k] + dx[k]
                            q = y + dy[k] + dy[k]
                            pp = x + dx[k]
                            qq = y + dy[k]
                            if 0 <= p < 9 and 0 <= q < 13 and expanded_field[pp][qq].field_type != FieldType.FENCE and not check3[p][q]:
                                check3[p][q] = True
                                expanded_field[p][q].maximum = maximum
                                queue.append((p, q))
        field_status = [[Field() for _ in range(5)] for __ in range(3)]
        for i in range(3):
            for j in range(5):
                field_status[i][j] = expanded_field[i*2 + 2][j * 2 + 2]
        player_status_repository.player_status[game_status_repository.game_status.now_turn_player].farm.field = field_status




    def log(self):
        return self.log_text
