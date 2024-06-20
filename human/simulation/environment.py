from abc import ABC, abstractmethod

from human.simulation.stimuli import Stimuli

class Environment(ABC):
    
    @abstractmethod
    def generate_stimulus(self) -> Stimuli:
        pass