class SingletonMeta(type):
   
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super().__call__( *args, **kwargs)
        return self._instances[self]
    
class Configuration(metaclass=SingletonMeta):
    def __init__(self):
        self._data = {}

    def setConfig(self, key, value):
        self._data[key] = value

    def getConfig(self, key):
        if key not in self._data:
            return None
        return self._data[key]
