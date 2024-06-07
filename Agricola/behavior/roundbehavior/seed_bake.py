"""
곡식 활용 라운드 행동
빈 밭만큼 곡식 선택하고, 해당 곡식을 심는다
그리고 빵 굽기 여부를 통해 빵 굽기를 수행한다.
:param: 플레이어 번호, 빵 굽기 여부, 선택한 밭과 곡물
:return: 실행 결과.
:rtype: bool
"""
from behavior.basebehavior.do_bake import DoBake
from behavior.behavior_interface import BehaviorInterface
from command import Command
from copy import copy
from entity.crop_type import CropType
from entity.round_behavior_type import RoundBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository
from behavior.basebehavior.seed_plant import SeedPlant


# Todo

class SeedBake(BehaviorInterface):

    def __init__(self, player, ifBread, plantDict, field_status):
        self.log_text = ""
        self.player = player
        self.ifBread = ifBread
        self.player_MainCard = player_status_repository.player_status[player].card.putMainCard
        self.plantDict = plantDict  # ex) {CropType.Grain : [[0,1],[1,2]}
        self.field_status = copy(field_status)

    def can_play(self):
        if (self.ifBread and not self.player_MainCard):
            self.log_text("빵 굽기를 할 주요 설비가 존재하지 않습니다")
            return False
        else:
            return True

    def execute(self):
        doSeedPlant = SeedPlant(self.plantDict, self.field_status)
        if doSeedPlant.execute():
            self.log_text = "밭 심기를 성공했습니다"
        else:
            self.log_text = "밭 심기를 실패했습니다"
            return False
        if (not self.ifBread):  # 빵굽기x
            round_status_repository.round_status.remain_workers[game_status_repository.game_status.now_turn_player] -= 1
            return True
        else :
            doBake = DoBake()
            if (doBake.execute()):
                self.log_Text = "빵 굽기를 완료했습니다"
            else:
                self.log_text = "빵 굽기를 실패했습니다"
            round_status_repository.round_status.remain_workers[game_status_repository.game_status.now_turn_player] -= 1
            return True

    def log(self):
        return self.log_text
