"""
회합 장소 기본 행동
:param: 플레이어 번호, 선택하고자 하는 보조 설비
:return: 실행 결과.
:rtype: bool
"""
from behavior.behavior_interface import BehaviorInterface
from command import Command
from entity.basic_behavior_type import BasicBehaviorType
from repository.game_status_repository import game_status_repository
from repository.player_status_repository import player_status_repository
from repository.round_status_repository import round_status_repository



class MeetingPlace(BehaviorInterface):
    def __init__(self, player):
        self.log_text = ""
        self.game_status = game_status_repository.game_status
        self.player_resource = player_status_repository.player_status[player].resource
        self.is_filled = round_status_repository.round_status.put_basic[BasicBehaviorType.MEETING.value]

    def can_play(self):
        return True

    def execute(self):
        for player in player_status_repository.player_status:  # 기존 1등 선마커 뺏기
            if player.resource.first_turn:
                player.resource.set_first_turn(False)
                break
        self.player_resource.set_first_turn(True)
        self.log_text = "선 마커를 획득하였습니다."
        return True

    def log(self):
        return self.log_text
