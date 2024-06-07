"""
집 고친 후에 주요 설비/보조 설비 1개 놓기 라운드 행동
:param: 플레이어 번호, 선택하고자 하는 설비 카드
:return: 실행 결과.
:rtype: bool
"""
from behavior.basebehavior.house_upgrade import HouseUpgrade
from behavior.behavior_interface import BehaviorInterface
from command import Command
from repository.game_status_repository import game_status_repository
from repository.round_status_repository import round_status_repository


class UpgradeFacilities(BehaviorInterface):
    def __init__(self):
        self.log_text = ""

    def can_play(self):
        return HouseUpgrade().can_play()

    def execute(self):
        round_status_repository.round_status.remain_workers[game_status_repository.game_status.now_turn_player] -= 1

    def log(self):
        return self.log_text
