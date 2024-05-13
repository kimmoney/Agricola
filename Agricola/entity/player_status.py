"""
플레이어의 상태 저장 엔티티
"""
from entity.farm.farm import Farm
from entity.player_partial_status.own_card import OwnCard
from entity.player_partial_status.resource import Resource
from entity.round_status import RoundStatus


class PlayerStatus:
    def __init__(self):
        self.card = OwnCard()
        self.farm = Farm()
        self.resource = Resource()
        self.worker = 0
        self.round_status = RoundStatus()
