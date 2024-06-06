"""
기본 가족 늘리기 후 보조 설비 1개 라운드 행동
:param: 플레이어 번호, 선택한 보조 설비
:return: 실행 결과.
:rtype: bool
"""
from command import Command
from entity.round_behavior_type import RoundBehaviorType
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


# Todo

class FamilyFacility(Command):

    def __init__(self, player, subFacility, field_status):
        self.log_text = None
        self.player_status = player_status_repository.player_status[player]
        self.is_filled = round_status_repository.round_status.put_basic[RoundBehaviorType.FAMILY_FACILITY.value]
        self.subFacility = subFacility
        self.field_status = field_status

    def execute(self):
        if self.is_filled:
            self.log_text = "이번 라운드에 이미 수행된 행동입니다."
            return False
        '''
        familyHouse=FamilyHouse()
        if familyHouse.execute() # field_status 순회 집갯수 조건문
        '''
        self.player_status.baby += 1
        self.log_text = "급하지않은 가족 늘리기를 성공했습니다"
        return True

    def log(self):
        return self.log_text
