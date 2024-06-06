from command import Command
from entity.crop_type import CropType
from entity.field_type import FieldType


class SeedPlantValidation(Command):

    def __init__(self, plantDict, field_status):
        self.plantDict = plantDict
        self.field_status = field_status
        self.log_text = None

    def execute(self):
        if CropType.VEGETABLE in self.plantDict:
            for selectArable in self.plantDict[CropType.VEGETABLE]:
                validationField = self.field_status[selectArable[0]][selectArable[1]]
                if validationField.fieldType != FieldType.ARABLE and validationField.kind != CropType.NONE:
                    self.log_text("심을 수 없는 위치 입니다")
                    return False
        if CropType.GRAIN in self.plantDict:
            for selectArable in self.plantDict[CropType.GRAIN]:
                validationField = self.field_status[selectArable[0]][selectArable[1]]
                if validationField.fieldType != FieldType.ARABLE and validationField.kind != CropType.NONE:
                    self.log_text("심을 수 없는 위치 입니다")
                    return False
        self.log_text("밭 심기 검증 성공")
        return True

    def log(self):
        return self.log_text
