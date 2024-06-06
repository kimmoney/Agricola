"""
라운드 행동칸 및 기본 행동칸에 자원을 쌓는 커맨드
"""
from command import Command
from entity.round_behavior_type import round_behavior_reverse_map, RoundBehaviorType
from repository.game_status_repository import game_status_repository


class StackResources(Command):
    def execute(self):
        game_status = game_status_repository.game_status
        for i in range(14):
            if round_behavior_reverse_map[game_status.opened_round_card[i]] == RoundBehaviorType.SHEEP1.name:
                game_status.set_round_resource(i, game_status.round_resource[i] + 1)
            if round_behavior_reverse_map[game_status.opened_round_card[i]] == RoundBehaviorType.COW.name:
                game_status.set_round_resource(i, game_status.round_resource[i] + 1)
            if round_behavior_reverse_map[game_status.opened_round_card[i]] == RoundBehaviorType.PIG.name:
                game_status.set_round_resource(i, game_status.round_resource[i] + 1)
            if round_behavior_reverse_map[game_status.opened_round_card[i]] == RoundBehaviorType.STONE_2.name:
                game_status.set_round_resource(i, game_status.round_resource[i] + 1)
            if round_behavior_reverse_map[game_status.opened_round_card[i]] == RoundBehaviorType.STONE_4.name:
                game_status.set_round_resource(i, game_status.round_resource[i] + 1)
        game_status.set_basic_resource(0, game_status.basic_resource[0] + 1)
        game_status.set_basic_resource(1, game_status.basic_resource[1] + 2)
        game_status.set_basic_resource(2, 1)
        game_status.set_basic_resource(3, game_status.basic_resource[3] + 1)
        game_status.set_basic_resource(4, game_status.basic_resource[4] + 1)
        game_status.set_basic_resource(7, 1)
        game_status.set_basic_resource(10, 2)
        game_status.set_basic_resource(11, game_status.basic_resource[11] + 3)
        game_status.set_basic_resource(12, game_status.basic_resource[12] + 2)
        game_status.set_basic_resource(13, game_status.basic_resource[13] + 1)
        game_status.set_basic_resource(14, game_status.basic_resource[14] + 1)



    def log(self):
        pass
