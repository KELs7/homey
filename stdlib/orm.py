from db.driver.memory_driver import mem_driver
from typing import Any

# TODO: check slicing and other dict stuff
class Storage:
    def __init__(self, contract: str, storage: str, default_value=None, driver=mem_driver):
        self._driver = driver
        self._key = self._driver["make_key"](contract=contract, storage=storage) # secure to make private?
        self.default_value = default_value
        

    def __setitem__(self, keys: str, value: Any):
        assert len(keys) <= 8, "Max keys allowed is 8."
        if type(keys) == tuple:
            key = f"{self._key}." + ".".join(keys)
            self._driver["set"](key=key, value=value)
        else:
            key = f"{self._key}." + keys
            self._driver["set"](key=key, value=value)

    def __getitem__(self, key: str):
        if type(key) == tuple:
            key = f"{self._key}." + ".".join(key)
            v = self._driver["get"](key)
            if v:
                return v
            else:
                return self.default_value
        else:
            key = f"{self._key}." + key
            v = self._driver["get"](key)
            if v:
                return v
            else:
                return self.default_value

    def set(self, value: Any):
        self._driver["set"](key=self._key, value=value)

    def get(self):
        v = self._driver["get"](key=self._key) 
        if v:
            return v
        else:
            return self.default_value