
import pytest
from behavior.basebehavior.fence_validation import FenceValidation
from entity.field_type import FieldType


def test_fence_validation_success1():
    list = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
    fence_validation = FenceValidation(list)
    list[0][1] = FieldType.FENCE
    list[0][3] = FieldType.FENCE
    list[1][4] = FieldType.FENCE
    list[3][4] = FieldType.FENCE
    list[4][3] = FieldType.FENCE
    list[4][1] = FieldType.FENCE
    list[3][0] = FieldType.FENCE
    list[1][0] = FieldType.FENCE
    assert fence_validation.execute() == True


def test_fence_validation_success2():
    list = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]


def test_fence_validation_success3():
    list = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]


def test_fence_validation_fail1():
    list = [[FieldType.NONE_FIELD for i in range(11)] for i in range(7)]
    list[0][1] = FieldType.FENCE
    list[0][3] = FieldType.FENCE
    list[1][4] = FieldType.FENCE
    list[3][4] = FieldType.FENCE
    list[4][3] = FieldType.FENCE
    list[4][1] = FieldType.FENCE
    list[3][0] = FieldType.FENCE
    list[1][0] = FieldType.FENCE
    list[1][1] = FieldType.HOUSE
    fence_validation = FenceValidation(list)
    assert fence_validation.execute() is False


def test_fence_validation_fail2():
    list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def test_fence_validation_fail3():
    list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
