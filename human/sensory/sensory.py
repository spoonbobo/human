from abc import ABC, abstractmethod

class Sensory(ABC):
    
    @abstractmethod
    def transduce(self):
        """
        converts external stimuli into neural signals.
        """
        pass
    
    @abstractmethod
    def transmit(self):
        """
        converts neural signals into electrical signals.
        """
        pass
    
    @abstractmethod
    def perceive(self):
        """
        interpreting and making sense of these signals in the brain.
        """
        pass

    @abstractmethod
    def integrate(self):
        """
        integrates information from different sources into a single coherent whole.
        """
        pass
    
    @abstractmethod
    def attend(self):
        """
        focuses on one or more sources of information.
        """
        pass
    
    @abstractmethod
    def adapts(self):
        """
        adjusts sensitivity over time
        """
        pass
