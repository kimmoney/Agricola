"""
집 확장(새 방 만들기) 기초 행동
:param: 플레이어 번호, 변경하고자 하는 필드 상태
:return: 집 확장 성공 여부 반환
:rtype: bool
농장 상태 업데이트도 수행되어야 함.
"""
from command import Command
from house_expand_validation import HouseExpandValidation


class HouseExpansion(Command):

    def __init__(self, filed_status):
        self.filed_status = filed_status
        self.log_text = None

    def execute(self):
        checkValidation=HouseExpandValidation(self.field_status)
        if (checkValidation.execute()):
            self.log_text = "농장 확장 검증에 성공했습니다"
            return True
        else:
            self.log_text = "농장 확장 검증에 실패했습니다"
            return False

    def log(self):
        return self.log_text
