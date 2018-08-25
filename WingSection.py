from config import CONFIG
from abc import ABC, abstractmethod
from pathlib import Path

def parseLednicer(afFile, _upper, _lower, firstTuple):
    raise NotImplementedError

def parseSelig(afFile, _upper, _lower, firstTuple):
    raise NotImplementedError

def parseAFFile(afPath, _upper, _lower):
    name = ""
    with afPath.open() as f:
            name = f.readline()
            firstTuple = ()
            while(firstTuple.empty()):
                firstTuple = tuple(map(float, f.readline().split()))
            if(firstTuple[0] > 1):
                parseLednicer(f, _upper, _lower, firstTuple)
            else:
                parseSelig(f, _upper, _lower, firstTuple)
    return name

class WingSection(ABC):
    """description of class"""
    
    @property
    @abstractmethod
    def upper(self) -> list:
        pass

    @property
    @abstractmethod
    def lower(self) -> list:
        pass

    @property
    @abstractmethod
    def path(self) -> Path:
        pass

class KnownAirfoil(WingSection):
    """description"""

    _upper = []
    _lower = []
    _name = "Airfoil"
    _afPath = Path("airfoil.dat")

    def __init__(self, fileName: str):
        self._afPath = Path(CONFIG.WingSectionPath, fileName)
        if(not self._afPath.exists()):
            raise FileNotFoundError(str(self._afPath.absolute()) + " not found!")
        parseAFFile(self._afPath, _upper, _lower)
    
    def upper(self):
        return self._upper

    def lower(self):
        return self._lower

    def path(self):
        return self._afPath
