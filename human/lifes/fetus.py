from human.lifes.human import Human
from human.sensory.sensory import Sensory
from human.sensory.observe import Observation
from human.simulation.context import Context
from human.brain.knowledge import PriorKnowledge

class Fetus(Human):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
    
    def observe(self,
                sensory: Sensory,
                *args, **kwargs) -> Observation:
        pass
    
    def think(self,
              observation: Observation):
        pass
    
    def act(self):
        pass

    def learn(self):
        pass
    
    def feel(self):
        pass
    
    def experience(self):
        pass
    
    def create(self):
        pass
    
    def sense(self):
        pass
    
    def communicate(self):
        pass
    
    def decide(self):
        pass

    def adapt(self):
        pass
    
    def empathize(self, input):
        pass
    
    def understand(self):
        pass

    def love(self):
        pass

