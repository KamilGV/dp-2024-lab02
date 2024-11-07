from abc import ABC, abstractmethod


class IFormatter(ABC):
    """
    Интерфейс для приведения сообщений к определенному формату

        Методы:
        format(message): Возвращает форматированное сообщение.
    """

    @abstractmethod
    def format(self, message: str) -> str:
        """
        Метод для форматирования сообщения.

        :param message: Сообщение.
        :return: Форматированное сообщение.
        """
        pass
