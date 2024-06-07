"""
게임 전체의 진행 상태를 저장하는 클래스
"""
from behavior.basicbehavior.cultivate import Cultivate
from behavior.basicbehavior.daily_labor import DailyLabor
from behavior.basicbehavior.dirt1 import Dirt1
from behavior.basicbehavior.dirt2 import Dirt2
from behavior.basicbehavior.farm_expansion import FarmExpansion
from behavior.basicbehavior.fishing import Fishing
from behavior.basicbehavior.meeting_place import MeetingPlace
from behavior.basicbehavior.reed import Reed
from behavior.basicbehavior.resource_market import ResourceMarket
from behavior.basicbehavior.seed import Seed
from behavior.basicbehavior.side_job1 import SideJob1
from behavior.basicbehavior.side_job2 import SideJob2
from behavior.basicbehavior.theater import Theater
from behavior.basicbehavior.wood1 import Wood1
from behavior.basicbehavior.wood2 import Wood2
from behavior.basicbehavior.wood3 import Wood3
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
from entity.round_behavior_type import RoundBehaviorType
from gamestate.game_context import GameContext
from repository.game_status_repository import game_status_repository


class GameStatus:
    def __init__(self):
        self.observers = []
        self.now_round = 0  # 현재 라운드
        self.now_turn_player = 0  # 현재 턴 플레이어
        self.next_turn_player = 0  # 다음 턴 플레이어
        self.round_card_order = [0 for i in range(14)]  # 라운드 카드의 순서. reverse map으로 탐색
        self.opened_round = [False for i in range(14)]  # 해당 라운드의 카드 공개 여부
        self.round_resource = [0 for i in range(14)]  # 라운드 기준 해당 라운드 칸 내부 자원 수 -> 프론트가 자원 표기하기 좋도록
        self.basic_resource = [0 for i in range(16)]  # 행동 Enum 기준 해당 행동 칸 내부 자원 수
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

    def basic_card_command_factory(self, basic_index):
        if basic_index == 0:
            return Wood1
        if basic_index == 1:
            return Wood2
        if basic_index == 2:
            return ResourceMarket
        if basic_index == 3:
            return Dirt1
        if basic_index == 4:
            return Theater
        if basic_index == 5:
            return FarmExpansion
        if basic_index == 6:
            return MeetingPlace
        if basic_index == 7:
            return Seed
        if basic_index == 8:
            return Cultivate
        if basic_index == 9:
            return SideJob1
        if basic_index == 10:
            return DailyLabor
        if basic_index == 11:
            return Wood3
        if basic_index == 12:
            return Dirt2
        if basic_index == 13:
            return Reed
        if basic_index == 14:
            return Fishing
        if basic_index == 15:
            return SideJob2


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

    def get_sheep_card_index(self):
        for i, num in enumerate(game_status_repository.game_status.round_card_order):
            if num is RoundBehaviorType.SHEEP1.value:
                return i

    def get_cow_card_index(self):
        for i, num in enumerate(game_status_repository.game_status.round_card_order):
            if num is RoundBehaviorType.COW.value:
                return i

    def get_pig_card_index(self):
        for i, num in enumerate(game_status_repository.game_status.round_card_order):
            if num is RoundBehaviorType.PIG.value:
                return i

    def get_stone2_card_index(self):
        for i, num in enumerate(game_status_repository.game_status.round_card_order):
            if num is RoundBehaviorType.STONE_2.value:
                return i

    def get_stone4_card_index(self):
        for i, num in enumerate(game_status_repository.game_status.round_card_order):
            if num is RoundBehaviorType.STONE_4.value:
                return i
