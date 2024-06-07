"""
밭 하나 일구기 그리고/또는 씨 뿌리기 라운드 행동
:param:
:return: 수행해야 할 행동 리스트
:rtype: 리스트
"""
from copy import copy

from behavior.basebehavior.seed_plant import SeedPlant
from behavior.behavior_interface import BehaviorInterface
from behavior.unitbehavior.use_worker import UseWorker
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from behavior.basebehavior.arable_expansion import ArableExpansion
from repository.round_status_repository import round_status_repository


class CultivateSeed(BehaviorInterface):
    def __init__(self):
        self.log_text = ""

    def can_play(self):
        return True

    def execute(self):
        ret = [ArableExpansion, SeedPlant, UseWorker]
        return ret

    def log(self):
        return self.log_text
