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
    def __init__(self, field_status):
        self.log_text = ""
        self.field_status = field_status

    def can_play(self):
        return True

    def execute(self):
        doArable = ArableExpansion(self.field_status)
        if doArable.execute():
            self.log_text = "밭을 일구었습니다."
            return True
        else:
            self.log_text = doArable.log()
            return False

    def log(self):
        return self.log_text
