from pathlib import Path

class ConfigurationData:

    _DataPath = Path()
    _WingSectionFolder = ""
    _KnownAirfoilFolder = ""

    def __init__(self):
        pass

    @property
    def WingSectionPath(self) -> Path:
        return Path(self._DataPath,Path(self._WingSectionFolder))


global CONFIG
CONFIG = ConfigurationData()

