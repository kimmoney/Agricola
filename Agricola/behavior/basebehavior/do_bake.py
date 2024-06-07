"""
빵 굽기 함수
빵 굽기 가능 여부 ->
"""
from behavior.basebehavior.base_behavior_interface import BaseBehaviorInterface
from command import Command
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from behavior.main_facility.oven1 import Oven1
from behavior.main_facility.oven2 import Oven2
from behavior.main_facility.strong_oven1 import StrongOven1
from behavior.main_facility.strong_oven2 import StrongOven2


class DoBake(BaseBehaviorInterface):
    def execute(self):
        pass

    def __init__(self):
        self.log_text = ""
        self.game_status = game_status_repository.game_status
        self.player_resource = player_status_repository.player_status[game_status_repository.game_status.now_turn_player].resource
        self.player_MainCard = player_status_repository.player_status[game_status_repository.game_status.now_turn_player].card.putMainCard

    def log(self):
        return self.log_text

    def can_play(self):
        if not self.player_MainCard:
            return False
        else:
            return True
