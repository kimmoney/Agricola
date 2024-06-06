"""
울타리 + 우리 생성 클래스
:param: 플레이어 번호, 변경하고자 하는 필드 상태
:return: 우리 생성 성공 여부
:rtype: bool
우리 생성 및 max 값 조정
농장 상태 업데이트도 수행되어야 함
"""
from command import Command
from fence_validation import FenceValidation


# Todo

class ConstructFence(Command):

    def __init__(self, field_status):
        self.field_status = field_status
        self.log_text = None

    def execute(self):
        fenseValidation = FenceValidation(self.field_status)
        if fenseValidation.execute():
            self.log_text = "울타리 건설 검증에 성공했습니다"
            return True
        else:
            self.log_text = "울타리 건설 검증에 실패했습니다"
            return False

    def log(self):
        return self.log_text
