"""
나무 누적 1개 기본 행동 구현
"""
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository


class Wood1:
    def stack_resource(self):
        game_status_repository.game_status.basic_resource[BasicBehaviorType.WOOD1]