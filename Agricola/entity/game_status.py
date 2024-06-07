"""
게임 전체의 진행 상태를 저장하는 클래스
"""
from behavior.roundbehavior.cow_market import CowMarket
from behavior.roundbehavior.cultivate_seed import CultivateSeed
from behavior.roundbehavior.facilities import Facilities
from behavior.roundbehavior.family_facility import FamilyFacility
from behavior.roundbehavior.fence_construction_round import FenceConstructionRound
from behavior.roundbehavior.hurry_family import HurryFamily
from behavior.roundbehavior.pig_market import PigMarket
from behavior.roundbehavior.seed_bake import SeedBake
from behavior.roundbehavior.sheep_market import SheepMarket
from behavior.roundbehavior.stone_2 import Stone2
from behavior.roundbehavior.stone_4 import Stone4
from behavior.roundbehavior.upgrade_facilities import UpgradeFacilities
from behavior.roundbehavior.upgrade_fence import UpgradeFence
from behavior.roundbehavior.vegetable_seed import VegetableSeed
from entity.main_facility_status import MainFacilityStatus
from gamestate.game_context import GameContext


class GameStatus:
    def __init__(self):
        self.observers = []
        self.now_round = 0          # 현재 라운드
        self.now_turn_player = 0    # 현재 턴 플레이어
        self.next_turn_player = 0   # 다음 턴 플레이어
        self.round_card_order = [0 for i in range(14)]  # 라운드 카드의 순서. reverse map으로 탐색
        self.opened_round = [False for i in range(14)]  # 해당 라운드의 카드 공개 여부
        self.round_resource = [0 for i in range(14)] # 라운드 기준 해당 라운드 칸 내부 자원 수
        self.basic_resource = [0 for i in range(16)] # 행동 Enum 기준 해당 행동 칸 내부 자원 수
        self.main_facility_status = MainFacilityStatus()
        self.game_context = GameContext()
        self.acted = False

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

    def round_card_command_factory(self, round_index):
        if self.round_card_order[round_index] == 0:
            return SheepMarket
        if self.round_card_order[round_index] == 1:
            return FenceConstructionRound
        if self.round_card_order[round_index] == 2:
            return Facilities
        if self.round_card_order[round_index] == 3:
            return SeedBake
        if self.round_card_order[round_index] == 4:
            return FamilyFacility
        if self.round_card_order[round_index] == 5:
            return Stone2
        if self.round_card_order[round_index] == 6:
            return UpgradeFacilities
        if self.round_card_order[round_index] == 7:
            return PigMarket
        if self.round_card_order[round_index] == 8:
            return VegetableSeed
        if self.round_card_order[round_index] == 9:
            return CowMarket
        if self.round_card_order[round_index] == 10:
            return Stone4
        if self.round_card_order[round_index] == 11:
            return CultivateSeed
        if self.round_card_order[round_index] == 12:
            return HurryFamily
        if self.round_card_order[round_index] == 13:
            return UpgradeFence