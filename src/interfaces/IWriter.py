from abc import ABC, abstractmethod

from src.enums.level_enum import Level


class IWriter(ABC):
    """
    Интерфейс для запиcи логов

        Методы:
        write(level, message): Записывает сообщение с заданным уровнем.
    """
    @abstractmethod
    def write(self, message: str) -> None:
        """
        Метод для записи лога.

        :param time: Время записи лога.
        :param message: Сообщение лога.
        :param level: Уровень Лога.
        :return: None.
        """
        pass
