"""
밭 하나 일구기 그리고/또는 씨 뿌리기 라운드 행동
:param: 플레이어 번호, 변하고자 하는 농장 상태
:return: 실행 결과.
:rtype: bool
"""
from copy import copy

from behavior.basebehavior.seed_plant import SeedPlant
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from behavior.basebehavior.arable_expansion import ArableExpansion


# Todo

class CultivateSeed(Command):

    def __init__(self, player, plantDict, field_status, ifPlant):
        self.log_text = None
        self.game_status = game_status_repository.game_status
        self.player_farm = player_status_repository.player_status[player].farm
        self.plantDict = plantDict  # ex) {CropType.Grain : [[0,1],[1,2]}
        self.field_status = copy(field_status)
        self.ifPlant = ifPlant

    def can_play(self):
        # 밭을 건설할수있는 위치가 있는지 확인필요
        return True

    def execute(self):
        doArable = ArableExpansion(self.player_farm)
        if (doArable.execute()):
            self.log_text = f"밭 {self.game_status.basic_resource[BasicBehaviorType.CULTIVATE.value]}개를 일구었습니다."
        else:
            self.log_text = f"밭을 일구지 못했습니다."
        if (not self.ifPlant):
            return False
        doSeedPlant = SeedPlant(self.plantDict, self.field_status)
        if doSeedPlant.execute():
            self.log_text = "밭 심기를 성공했습니다"
            return True
        else:
            self.log_text = "밭 심기를 실패했습니다"
            return False

    def log(self):
        return self.log_text
