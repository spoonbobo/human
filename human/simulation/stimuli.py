from abc import ABC, abstractmethod

class Stimuli(ABC):

    @abstractmethod
    def generate(self):
        pass