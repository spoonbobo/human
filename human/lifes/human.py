from abc import ABC, abstractmethod

from human.sensory.sensory import Sensory
from human.sensory.observe import Observation

class Human(ABC):
    """
    A human is a true intelligence.
    """
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @abstractmethod
    def observe(self, sensory: Sensory, *args, **kwargs) -> Observation:
        pass
    
    @abstractmethod
    def think(self):
        pass
    
    @abstractmethod
    def act(self):
        pass

    @abstractmethod
    def learn(self):
        pass
    
    @abstractmethod
    def feel(self):
        pass
    
    @abstractmethod
    def experience(self):
        pass
    
    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def sense(self):
        pass
    
    @abstractmethod
    def communicate(self):
        pass
    
    @abstractmethod
    def decide(self):
        pass

    @abstractmethod
    def adapt(self):
        pass
    
    @abstractmethod
    def empathize(self, input):
        pass
    
    @abstractmethod
    def understand(self):
        pass

    @abstractmethod
    def love(self):
        pass
