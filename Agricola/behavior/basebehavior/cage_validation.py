"""
동물들의 배치 상태가 올바른지 검증하는 로직을 수행하는 클래스.
"""
from behavior.behavior import Behavior
from entity.field_type import FieldType


class CageValidation(Behavior):
    def __init__(self, farm_status):
        self.farm_status = farm_status

    def execute(self):
        pass

    def animal_count_validation(self):

        for items in self.farm_status:
            for item in items:
                if item.field_type == FieldType.CAGE:
        pass

    def unified_animal_validation(self):
        pass

    def inside_animal_validation(self):
        pass
1
    def log(self):
        pass


"""
1. 울타리 안 or 외양간 안에 있는가
    - 울타리 안에 있다 -> 밖부터 순회문 돌리기 -> 순수하게 cage | 외양간 과 cage가 아닌 곳으로
    - 패딩을 추가한 배열 필요
2. 최대 제한 수를 넘지 않았는가
    - 
3. 동물의 종이 전부 같은가


잘못된 입력은 어떻게 받지?
그냥 간단한 "잘못된 곳에는 배치가 안되도록 하는 메소드" 도 필요하다???
ㄴㄴㄴㄴㄴㄴㄴㄴ
잘못된 곳에도 배치가 가능해야, 동물들이 각 칸에 락이 걸렸을 때, 위치를 서로 바꿔줄 수 있다.
들판만 가능하게 두고, 다른곳엔 배치 안되게
누르면 증발할텐데? -> 일반 들판도 동물 데이터를 기본적으로 담을 수는 있게?
-> 굳이? -> NoneField 
"""