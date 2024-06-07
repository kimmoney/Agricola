"""
농장 확장 기본 행동
:param: 플레이어 번호, 변하고자 하는 필드 상태
:return: 실행 결과.
:rtype: bool
"""
from behavior.behavior_interface import BehaviorInterface
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository
from behavior.basebehavior.house_expansion import HouseExpansion


class FarmExpansion(BehaviorInterface):

    def __init__(self, field_status):
        self.log_text = ""
        self.field_status = field_status
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.EXPAND.value]

    def can_play(self):
        # 농장 확장이 가능한 위치가 있는지 확인
        return True

    def execute(self):
        doExpansion = HouseExpansion(self.field_status)
        if doExpansion.execute():
            self.log_text = f"농장 확장에 성공했습니다."
            return True
        else:
            self.log_text = f"농장을 확장하지못했습니다."
            return False

    def log(self):
        return self.log_text
