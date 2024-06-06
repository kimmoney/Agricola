"""
게임 전체의 진행 상태를 저장하는 클래스
"""
from entity.main_facility_status import MainFacilityStatus


class GameStatus:
    def __init__(self):
        self.observers = []
        self.now_round = 0          # 현재 라운드
        self.now_turn_player = 0    # 현재 턴 플레이어
        self.next_turn_player = 0   # 다음 턴 플레이어
        self.round_card_order = [0 for i in range(14)]  # 라운드 카드의 순서. reverse map으로 탐색
        self.opened_round = [False for i in range(14)]  # 카드가 공개된 라운드 여부
        self.round_resource = [0 for i in range(14)] # 라운드 기준 해당 라운드 칸 내부
        self.basic_resource = [0 for i in range(16)]
        self.main_facility_status = MainFacilityStatus()

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_now_round(self, now_round):
        self.now_round = now_round
        self.notify()

    def set_now_turn_player(self, now_turn_player):
        self.now_turn_player = now_turn_player
        self.notify()

    def set_next_turn_player(self, next_turn_player):
        self.next_turn_player = next_turn_player
        self.notify()

    def set_round_resource(self, index, value):
        self.round_resource[index] = value
        self.notify()

    def set_round_card_order(self, index, value):
        self.round_card_order[index] = value
        self.notify()

    def set_basic_resource(self, index, value):
        self.basic_resource[index] = value
        self.notify()