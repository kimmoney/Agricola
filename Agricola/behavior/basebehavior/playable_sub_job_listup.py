"""
제출 가능한 직업 카드 리스트업 함수
:param: 플레이어 번호
:return: 제출 가능한 직업 카드 리스트 반환
:rtype: list<card_name>
"""
from command import Command
from repository.player_status_repository import player_status_repository


class PlayableSubJobListup(Command):
    def __init__(self, player):
        self.log_text = ""
        self.jobList = self.player_ownCard = player_status_repository.player_status[player].own_card.handJobCard

    def execute(self):
        self.log_text = "구매 가능한 직업을 확인했습니다"
        return  self.jobList

    def log(self):
        return self.log_text
