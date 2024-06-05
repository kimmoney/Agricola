"""
곡식 활용 라운드 행동
빈 밭만큼 곡식 선택하고, 해당 곡식을 심는다
그리고 빵 굽기 여부를 통해 빵 굽기를 수행한다.
:param: 플레이어 번호, 빵 굽기 여부, 선택한 밭과 곡물
:return: 실행 결과.
:rtype: bool
"""
from command import Command
from copy import copy
from entity.crop_type import CropType
from entity.round_behavior_type import RoundBehaviorType
from repository.round_status_repository import round_status_repository
from behavior.basebehavior.seed_plant import SeedPlant


# Todo

class SeedBake(Command):

    def __init__(self, ifBread, plantDict, field_status):
        self.log_text = None
        self.is_filled = round_status_repository.round_status.put_basic[RoundBehaviorType.SEED_BAKE.value]
        self.ifBread = ifBread
        self.plantDict = plantDict  # ex) {CropType.Grain : [[0,1],[1,2]}
        self.field_status = copy(field_status)

    def execute(self):
        if self.is_filled:
            self.log_text = "이번 라운드에 이미 수행된 행동입니다."
            return False
        doSeedPlant = SeedPlant(self.plantDict, self.field_status)
        if doSeedPlant.execute():
            self.log_text = "밭 심기를 성공했습니다"
        else:
            self.log_text = "밭 심기를 실패했습니다"
            return False
        if (not self.ifBread):  # 빵굽기x
            return True
        # 빵굽기 코드
        return True

    def log(self):
        return self.log_text
