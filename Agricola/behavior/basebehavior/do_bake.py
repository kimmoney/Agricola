from command import Command
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from behavior.main_facility.oven1 import Oven1
from behavior.main_facility.oven2 import Oven2
from behavior.main_facility.strong_oven1 import StrongOven1
from behavior.main_facility.strong_oven2 import StrongOven2


class DoBake(Command):
    def __init__(self, player):
        self.log_text = None
        self.game_status = game_status_repository.game_status
        self.player_resource = player_status_repository.player_status[player].resource
        self.player_MainCard = player_status_repository.player_status[player].card.putMainCard

    def execute(self):
        for mainFacility in self.player_MainCard:
            if mainFacility.canUse():
                mainFacility.execute(self.player_resource)
        return True

    def log(self):
        return self.log_text
