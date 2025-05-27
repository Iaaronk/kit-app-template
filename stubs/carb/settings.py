class _Settings:
    def __init__(self):
        self._data = {}

    def get(self, path):
        return self._data.get(path)

    def get_as_bool(self, path):
        return bool(self._data.get(path))

    def get_as_string(self, path):
        value = self._data.get(path)
        return str(value) if value is not None else ""

    def set(self, path, value):
        self._data[path] = value

    def set_bool(self, path, value):
        self._data[path] = bool(value)

    def set_string(self, path, value):
        self._data[path] = str(value)

    def set_int(self, path, value):
        self._data[path] = int(value)


_settings = _Settings()


def get_settings():
    return _settings


class ChangeEventType:
    UNKNOWN = 0
