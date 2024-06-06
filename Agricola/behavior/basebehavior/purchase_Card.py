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

    def execute(self):
        if (self.selectedCard.canPurchase(self.playerResource)):
            self.log_text = "카드 구매가 가능합니다"
            return True # 프런트에서 진짜 살지 물어보고 true false 로 base/behavior/purchaseCard 실행
        else:
            self.log_text = "카드 구매에 실패했습니다"
            return False

    def log(self):
        return self.log_text