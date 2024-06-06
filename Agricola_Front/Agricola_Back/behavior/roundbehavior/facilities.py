"""
주요 설비/보조 설비 1개 놓기 라운드 행동
:param: 플레이어 번호, 선택한 카드
:return: 실행 결과.
:rtype: bool
"""
from command import Command
from repository.player_status_repository import player_status_repository


# Todo

class Facilities(Command):
    def __init__(self, player, selectedCard, isMain):
        self.log_text = None
        self.playerResource = player_status_repository.player_status[player].resource
        self.playerCard = player_status_repository.player_status[player].card
        self.selectedCard = selectedCard
        self.isMain = isMain

    def can_play(self):
        if (self.selectedCard.canPurchase(self.player)):
            self.log_text = "카드 구매가 가능합니다"
            return True
        else:
            self.log_text = "카드 구매에 실패했습니다"
            return False

    def execute(self):
        if (self.selectedCard.purchase(self.player)):
            self.log_text = "카드 구매에 성공했습니다"
            return True
        else:
            self.log_text = "카드 구매에 실패했습니다"
            return False

    def log(self):
        return self.log_text
