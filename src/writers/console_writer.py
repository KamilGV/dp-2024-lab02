from src.interfaces import IWriter


class ConsoleWriter(IWriter):
    def __init__(self, *args, **kwargs):
        pass

    """
    Класс для запиcи логов

        Методы:
        write(message): Записывает сообщение в консоль.
    """

    def write(self, message) -> None:
        """
        Метод для записи лога в консоль.

        :param message: Сообщение.
        :return: None.
        """
        print(message)
