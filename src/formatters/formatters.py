from src.interfaces import IFormatter


class InitialCaseFormatter(IFormatter):
    """
    Класс для приведения сообщений к исходному формату

        Методы:
        format(message): Возвращает исходное сообщение.
    """

    def format(self, message: str) -> str:
        """
        Метод для форматирования сообщения.

        :param message: Сообщение.
        :return: Исходное сообщение.
        """
        return message


class UpperCaseFormatter(IFormatter):
    """
    Класс для приведения сообщений к формату в заглавном регистре

        Методы:
        format(message): Возвращает форматированное сообщение в заглавном регистре.
    """

    def format(self, message: str) -> str:
        """
        Метод для форматирования сообщения.

        :param message: Сообщение.
        :return: Сообщение в заглавном регистре.
        """
        return message.upper()
