"""
밭 일구기 기본 행동
:param: 플레이어 번호, 변하고자 하는 밭 상태 # 플레이어 번호 날림 by jy

:return: 실행 결과.
:rtype: bool
"""
from behavior.behavior_interface import BehaviorInterface
from behavior.basebehavior.arable_expansion import ArableExpansion


class Cultivate(BehaviorInterface):

    def __init__(self, field_status):
        self.log_text = ""
        self.field_status = field_status

    def execute(self):
        doArable = ArableExpansion(self.field_status)
        if doArable.execute():
            self.log_text = "밭을 일구었습니다."
            return True
        else:
            self.log_text = doArable.log()
            return False


    def log(self):
        return self.log_text
