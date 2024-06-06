"""
비효율 교습
:param: 플레이어 번호, 선택하고자 하는 직업 카드
:return: 실행 결과.
:rtype: bool
"""
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


# Todo

class SideJob2(Command):
    def __init__(self, player, playCard):
        self.log_text = None
        self.playCard = playCard
        self.player_resource = player_status_repository.player_status[player].resource
        self.player_ownCard = player_status_repository.player_status[player].own_card
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.SIDE_JOB2.value]

    def execute(self):
        if self.is_filled:
            self.log_text = "이번 라운드에 이미 수행된 행동입니다."
            return False
        if (self.playCard in self.player_ownCard.handJobCard) and self.playCard.putDown():
            self.log_text = "카드 내기에 성공했습니다."
            return True
        else:
            self.log_text = "해당 카드를 낼 수 없습니다."
            return False

    def log(self):
        return self.log_text
