import random

from command import Command
from repository.game_status_repository import game_status_repository


class RoundCardShuffle(Command):
    def execute(self):
        week1 = random.sample(range(0, 4), 4)
        week2 = random.sample(range(4, 7), 3)
        week3 = random.sample(range(7, 9), 2)
        week4 = random.sample(range(9, 11), 2)
        week5 = random.sample(range(11, 13), 2)
        week6 = random.sample(range(13, 14), 1)
        for i, source in week1:
            game_status_repository.game_status.set_round_card_order(i, source)
        for i, source in week2:
            game_status_repository.game_status.set_round_card_order(i + 4, source)
        for i, source in week3:
            game_status_repository.game_status.set_round_card_order(i + 7, source)
        for i, source in week4:
            game_status_repository.game_status.set_round_card_order(i + 9, source)
        for i, source in week5:
            game_status_repository.game_status.set_round_card_order(i + 11, source)
        for i, source in week6:
            game_status_repository.game_status.set_round_card_order(i + 13, source)

    def log(self):
        pass
