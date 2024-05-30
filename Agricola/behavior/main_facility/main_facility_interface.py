"""
주요 설비 인터페이스
"""
from abc import abstractmethod
from behavior.behavior import Behavior


class MainFacilityInterface(Behavior):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def log(self):
        pass

    @abstractmethod
    def purchase(self):
        pass
