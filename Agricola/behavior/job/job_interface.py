"""
직업 카드 행동 인터페이스
"""
from abc import abstractmethod

from behavior.behavior import Behavior


class JobInterface(Behavior):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def log(self):
        pass

    @abstractmethod
    def putDown(self):
        pass
