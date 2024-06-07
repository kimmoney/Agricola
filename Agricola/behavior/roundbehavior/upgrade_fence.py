"""
집 한번 고친 후에 울타리 치기 라운드 행동
:param: 플레이어 번호, 바꾸고자 하는 농장 상태
:return: 실행 결과.
:rtype: bool
"""
from behavior.behavior_interface import BehaviorInterface
from command import Command
from repository.game_status_repository import game_status_repository
from repository.round_status_repository import round_status_repository


class UpgradeFence(BehaviorInterface):
    def execute(self):
        round_status_repository.round_status.remain_workers[game_status_repository.game_status.now_turn_player] -= 1
        pass

    def log(self):
        pass
