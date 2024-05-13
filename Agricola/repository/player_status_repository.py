"""
플레이어 상태 저장소
"""
from entity.player_status import PlayerStatus


class PlayerStatusRepository:
    def __init__(self):
        self.player_status_repository = [PlayerStatus() for i in range(4)]
