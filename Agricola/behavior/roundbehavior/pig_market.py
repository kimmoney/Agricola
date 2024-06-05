"""
돼지 시장 라운드 행동
:param: 플레이어 번호
:return: 획득한 동물이 담긴 큐
:rtype: deque
"""
from command import Command
from entity.round_behavior_type import RoundBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository
from entity.animal_type import AnimalType


# Todo

class PigMarket(Command):
    def __init__(self, player):
        self.log_text = None
        self.game_status = game_status_repository.game_status
        self.player_resource = player_status_repository.player_status[player].resource
        self.is_filled = round_status_repository.round_status.put_basic[RoundBehaviorType.PIG.value]

    def execute(self):
        if self.is_filled:
            self.log_text = "이번 라운드에 이미 수행된 행동입니다."
            return False
        animal_dict = {AnimalType.PIG: self.game_status.basic_resource[RoundBehaviorType.PIG.value]}
        self.log_text = f"돼지 {self.game_status.basic_resource[RoundBehaviorType.PIG.value]}마리를 획득하였습니다."
        self.game_status.set_basic_resource(RoundBehaviorType.PIG.value, 0)
        return animal_dict

    def log(self):
        return self.log_text
