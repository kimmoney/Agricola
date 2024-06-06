from command import Command
from seed_plant_validation import SeedPlantValidation


class SeedPlant(Command):

    def __init__(self, plantDict, field_status):
        self.plantDict = plantDict
        self.field_status = field_status
        self.log_text = None

    def execute(self):
        checkValidation = SeedPlantValidation(self.plantDict, self.field_status)
        if checkValidation.execute():
            self.log_text = "밭 심기 검증에 성공했습니다"
            return True
        else:
            self.log_text = "밭 심기 검증에 실패했습니다"
            return False

    def log(self):
        return self.log_text
