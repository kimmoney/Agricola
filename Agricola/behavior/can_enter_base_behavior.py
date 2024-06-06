from command import Command
from repository.game_status_repository import game_status_repository
from repository.round_status_repository import round_status_repository


class CanEnterRoundBehavior(Command):
    def __init__(self, behavior, behavior_enum):
        self.log_text = ""
        self.behavior = behavior
        self.behavior_enum = behavior_enum

    def execute(self):
        if not round_status_repository.round_status.put_basic[self.behavior_enum] and \
                self.behavior.can_play():
            self.log_text = "행동이 수행가능합니다."
            return True
        else:
            self.log_text = "행동을 수행할 수 없습니다"
            return False

    def log(self):
        return self.log_text
