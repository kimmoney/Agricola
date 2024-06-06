"""
채석장 라운드 행동 - 4주기
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from command import Command
from entity.round_behavior_type import RoundBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


# Todo

class Stone4(Command):
    def __init__(self, player):
        self.log_text = None
        self.game_status = game_status_repository.game_status
        self.player_resource = player_status_repository.player_status[player].resource
        self.is_filled = round_status_repository.round_status.put_basic[RoundBehaviorType.STONE_4.value]

    def can_play(self):
        return True

    def execute(self):
        self.player_resource.set_stone(
            self.player_resource.stone + self.game_status.basic_resource[RoundBehaviorType.STONE_4.value])
        self.log_text = f"돌 {self.game_status.basic_resource[RoundBehaviorType.STONE_4.value]}개를 획득하였습니다."
        self.game_status.set_basic_resource(RoundBehaviorType.STONE_4.value, 0)
        return True

    def log(self):
        return self.log_text
