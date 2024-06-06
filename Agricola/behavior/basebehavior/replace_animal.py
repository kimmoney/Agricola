"""
동물 재배치하기 모드 기초 행동
:param: 플레이어 번호, 변경하고자 하는 필드 상태
:return: 동물 재배치하기 성공 여부
:rtype: bool

프론트에서 동물 재배치하기 버튼을 클릭하고, 동물을 완전히 이동시킨 뒤 수행하는 동물 배치 확정 로직
"""
from behavior.basebehavior.place_animal import PlaceAnimal
from command import Command


class ReplaceAnimal(Command):
    def __init__(self, field_status):
        self.log_text = ""
        self.field_status = field_status

    def execute(self):
        return PlaceAnimal(self.field_status)

    def log(self):
        return self.log_text
