"""
기본 가족 늘리기 후 보조 설비 1개 라운드 행동
:param: 플레이어 번호, 선택한 보조 설비
:return: 실행 결과.
:rtype: bool
"""
from behavior.behavior_interface import BehaviorInterface
from command import Command
from entity.round_behavior_type import RoundBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository



class FamilyFacility(BehaviorInterface):

    def __init__(self, player, subFacility, field_status):
        self.log_text = ""
        self.player_status = player_status_repository.player_status[player]
        self.is_filled = round_status_repository.round_status.put_basic[RoundBehaviorType.FAMILY_FACILITY.value]
        self.subFacility = subFacility
        self.field_status = field_status

    def can_play(self):
        '''
        familyHouse=FamilyHouse()
        if familyHouse.execute() # field_status 순회 집갯수 조건문
        '''
        if self.player_status.baby + self.player_status.worker == 5:
            self.log_text = "더 이상 가족을 늘릴 수 없습니다"
            return False
        else:
            return True

    def execute(self):
        self.player_status.set_baby(1)
        self.log_text = "급하지않은 가족 늘리기를 성공했습니다"
        round_status_repository.round_status.remain_workers[game_status_repository.game_status.now_turn_player] -= 1
        return True

    def log(self):
        return self.log_text
