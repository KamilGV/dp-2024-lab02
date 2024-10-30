from abc import ABC, abstractmethod


class IFormatter(ABC):
    @abstractmethod
    def format(self, message: str) -> str:
        pass
