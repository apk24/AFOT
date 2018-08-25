from abc import ABC, abstractmethod, abstractstaticmethod

from WingSection import WingSection

class Wing(ABC):
    """description of class"""

    @abstractmethod
    def getChordAt(self, y: float) -> float:
        pass

    @abstractmethod
    def getOffsetAt(self, y: float) -> float:
        pass

    @property
    @abstractmethod
    def span(self) -> float:
        pass

    @property
    @abstractmethod
    def refChord(self) -> float:
        pass

    @property
    @abstractmethod
    def refArea(self) -> float:
        pass

    @abstractmethod
    def getSectionAt(self, y: float) -> WingSection:
        pass

    @abstractmethod
    def getAoIAt(self, y: float) -> float:
        pass

