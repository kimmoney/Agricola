"""
밭 일구기 기본 행동
:param: 플레이어 번호, 변하고자 하는 밭 상태 # 플레이어 번호 날림 by jy

:return: 실행 결과.
:rtype: bool
"""
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository
from behavior.basebehavior.arable_expansion import ArableExpansion


# Todo

class Cultivate(Command):
    def __init__(self, player):
        self.log_text = ""
        self.game_status = game_status_repository.game_status
        self.player_farm = player_status_repository.player_status[player].farm

    def can_play(self):

        # 밭을 건설할수있는 위치가 있는지 확인필요
        return True

    def execute(self):
        doArable = ArableExpansion(self.player_farm)
        if doArable.execute():
            self.log_text = f"밭 {self.game_status.basic_resource[BasicBehaviorType.CULTIVATE.value]}개를 일구었습니다."
            return True
        else:
            self.log_text = f"밭을 일구지 못했습니다."
            return False

    def log(self):
        return self.log_text
