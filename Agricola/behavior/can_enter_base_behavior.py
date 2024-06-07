from command import Command
from repository.game_status_repository import game_status_repository
from repository.round_status_repository import round_status_repository


class CanEnterBaseBehavior(Command):
    def __init__(self, behavior, behavior_index):
        self.log_text = ""
        self.behavior = behavior
        self.behavior_index = behavior_index

    def execute(self):
        if round_status_repository.round_status.put_basic[self.behavior_index] == -1 and \
                self.behavior.can_play():
            self.log_text = "행동이 수행가능합니다."
            return True
        else:
            self.log_text = "행동을 수행할 수 없습니다"
            return False

    def log(self):
        return self.log_text
