"""
카드 분배 커맨드
각 player_status 의 card 객체에 6장의 카드 번호를 넣는다.
"""
import random

from command import Command
from repository.player_status_repository import player_status_repository


class CardDistribution(Command):

    def execute(self):
        card_list = random.sample(range(24), 24)
        for i in range(4):
            for j in range(3):
                player_status_repository.player_status[i].card.handSubCard.append(card_list[i * 3 + j])
        for i in range(4):
            for j in range(3):
                player_status_repository.player_status[i].card.handJobCard.append(card_list[12 + i * 3 + j])

    def log(self):
        pass
