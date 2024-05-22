from behavior.basebehavior.animal_move_validation import AnimalMoveValidation

from entity.animal_type import AnimalType
from entity.farm.arable_land import ArableLand
from entity.farm.cage import Cage
from entity.field_type import FieldType
import pytest


def test_animal_move():
    # 필드 상태 예시 데이터
    field_status = [[Cage() for _ in range(11)] for _ in range(7)]
    # 동물의 위치 설정
    position = (2, 4)  # 3행 5열 위치
    # 동물 종류 설정
    animal_type = AnimalType.COW  # 예를 들어 소

    # AnimalMoveValidation 인스턴스 생성
    validator = AnimalMoveValidation(field_status, animal_type, position)

    # 실행 메소드 호출
    move_possible = validator.execute()

    assert move_possible == True


def test_animal_move_on_structure():
    # 필드 상태 예시 데이터
    field_status = [[Cage() for _ in range(11)] for _ in range(7)]
    # 동물의 위치 설정
    position = (2, 4)  # 3행 5열 위치

    field_status[5][9] = ArableLand()
    # 동물 종류 설정
    animal_type = AnimalType.COW  # 예를 들어 소

    # AnimalMoveValidation 인스턴스 생성
    validator = AnimalMoveValidation(field_status, animal_type, position)

    # 실행 메소드 호출
    move_possible = validator.execute()

    assert move_possible == False

def test_animal_move_diff_animal():
    # 필드 상태 예시 데이터
    field_status = [[Cage() for _ in range(11)] for _ in range(7)]
    # 동물의 위치 설정
    position = (2, 4)  # 3행 5열 위치

    # 기존 동물 : 돼지
    field_status[5][9].kind = AnimalType.PIG
    # 동물 종류 설정
    animal_type = AnimalType.COW  # 예를 들어 소

    # AnimalMoveValidation 인스턴스 생성
    validator = AnimalMoveValidation(field_status, animal_type, position)

    # 실행 메소드 호출
    move_possible = validator.execute()

    assert move_possible == False