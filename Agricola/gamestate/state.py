"""
상태 패턴 추상 클래스
"""
from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def next_state(self):
        pass
