"""
곡식 종자 기본 행동
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


# Todo


class Seed(Command):
    def __init__(self, player):
        self.log_text = ""
        self.game_status = game_status_repository.game_status
        self.player_resource = player_status_repository.player_status[player].resource
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.SEED.value]

    def can_play(self):
        return True

    def execute(self):
        self.player_resource.set_grain(
            self.player_resource.grain + self.game_status.basic_resource[BasicBehaviorType.SEED.value])
        self.log_text = f"곡식 {self.game_status.basic_resource[BasicBehaviorType.SEED.value]}개를 획득하였습니다."
        self.game_status.set_basic_resource(BasicBehaviorType.SEED.value, 1)
        return True

    def log(self):
        return self.log_text
