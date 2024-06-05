"""
밭 1개 일구기 기초 행동
:param: 플레이어 번호, 필드 상태
:return: 밭 1개 일구기 성공 여부
:rtype: bool
실제 밭 정보를 업데이트한다.
"""
from command import Command
from arable_expand_validation import ArableExpandValidation

class ArableExpansion(Command):

    def __init__(self, filed_status):
        self.filed_status = filed_status
        self.log_text=None
    def execute(self):
        checkValidation=ArableExpandValidation(self.field_status)
        if(checkValidation.execute()):
            self.log_text="밭 일구기 검증에 성공했습니다"
            return True
        else :
            self.log_text = "밭 일구기 검증에 실패했습니다"
            return False

    def log(self):
        return self.log_text
