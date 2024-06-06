"""
농장 확장 기본 행동
:param: 플레이어 번호, 변하고자 하는 필드 상태
:return: 실행 결과.
:rtype: bool
"""
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository
from behavior.basebehavior.house_expansion import HouseExpansion


# Todo

class FarmExpansion(Command):

    def __init__(self, player):
        self.log_text = None
        self.game_status = game_status_repository.game_status
        self.player_farm = player_status_repository.player_status[player].farm
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.EXPAND.value]

    def execute(self):
        if self.is_filled:
            self.log_text = "이번 라운드에 이미 수행된 행동입니다."
            return False
        doExpansion = HouseExpansion(self.player_farm)
        if (doExpansion.execute()):
            self.log_text = f"농장 확장에 성공했습니다."
            return True
        else:
            self.log_text = f"농장을 확장하지못했습니다."
            return False

    def log(self):
        return self.log_text
