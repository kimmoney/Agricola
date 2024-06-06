"""
급한 가족 늘리기 라운드 행동
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from command import Command
from entity.round_behavior_type import RoundBehaviorType
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


# Todo

class HurryFamily(Command):

    def __init__(self, player):
        self.log_text = None
        self.player_status = player_status_repository.player_status[player]
        self.is_filled = round_status_repository.round_status.put_basic[RoundBehaviorType.HURRY_FAMILY.value]

    def can_play(self):
        if self.player_status.baby + self.player_status.worker == 5:
            self.log_text = "더 이상 가족을 늘릴 수 없습니다"
            return False
        else:
            return True

    def execute(self):
        self.player_status.baby += 1
        self.log_text = "급한 가족 늘리기를 성공했습니다"
        return True

    def log(self):
        return self.log_text
