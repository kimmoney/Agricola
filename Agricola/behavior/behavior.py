from abc import ABC, abstractmethod

class Behavior(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def log(self):
        pass
