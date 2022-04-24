

class StrKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            reture self[key]
        except KeyError:
            return default


    def __contains__(self, key):
        return key in self.key() or str(key) in self.keys()
