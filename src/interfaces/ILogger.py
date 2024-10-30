from abc import ABC, abstractmethod

from src.enums.level_enum import Level
from src.interfaces import IWriter


class ILogger(ABC):
    """
    Интерфейс для управления логированием сообщений

        Методы:
        log(level, message): Записывает сообщение с заданным уровнем.
    """

    @abstractmethod
    def log(self, message: str, level: Level) -> None:
        """
        Метод для записи лога.

        :param message: Сообщение лога.
        :param level: Уровень Лога.
        :return: None.
        """
        pass

    @abstractmethod
    def set_writer(self, writer: IWriter):
        """
        Метод для установки метода записи.

        :param writer: Метод записи.
        :return: None.
        """
        pass
