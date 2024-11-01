import threading


class Singleton:
    _mutex_create = threading.Lock()
    _instance = None

    def __new__(cls, *args, **kwargs):
        return cls._create_singleton()

    @classmethod
    def _create_singleton(cls):
        with cls._mutex_create:
            if not cls._instance:
                cls._instance = super().__new__(cls)

            return cls._instance
