"""
울타리 검증 클래스
:param list:  7 * 11 의 울타리 배치 배열
:return: 올바른 울타리 여부.
"""
from behavior.behavior import Behavior


class FenceValidation(Behavior):
    def __init__(self, list):
        self.list = list
        self.dx = [0, 0, -1, 1]
        self.dy = [-1, 1, 0, 0]

    def execute(self):
        for i, item in enumerate(self.list):
            for j, value in enumerate(item):
                if i % 2 == 0 and j % 2 == 0:
                    adjacent = 0
                    for k in range(4):
                        p = i + self.dx[k]
                        q = j + self.dy[k]
                        if p < 0 or q < 0 or p >= 7 or q >= 11:
                            continue
                        if list[p][q]:
                            adjacent += 1
                    if adjacent == 1:
                        return False
        return True

    def log(self):
        pass
