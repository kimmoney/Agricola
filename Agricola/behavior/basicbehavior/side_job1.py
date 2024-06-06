"""
효율 교습
:param: 플레이어 번호
:return: 실행 결과.
:rtype: bool
"""
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository


# Todo

class SideJob1(Command):

    def __init__(self, player, playCard):
        self.log_text = None
        self.player = player
        self.playCard = playCard
        self.player_resource = player_status_repository.player_status[player].resource
        self.player_ownCard = player_status_repository.player_status[player].own_card
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.SIDE_JOB1.value]

    def can_play(self):
        if (not self.player_ownCard.handJobCard) or self.player_resource.food >= 1:
            self.log_text = "직업을 낼 수 있습니다."
            return True
        else:
            self.log_text = "비용이 없어 행동이 불가능합니다"
            return False

    def execute(self):
        if (self.playCard not in self.player_ownCard.handJobCard):
            self.log_text = "직업을 낼 수 없습니다."
            return False
        if (self.playCard.purchase(self.player)):
            if (self.player_ownCard.handJobCard):
                self.player_resource.food -= 1
        self.log_text = "직업을 냈습니다."
        return True

    def log(self):
        return self.log_text
