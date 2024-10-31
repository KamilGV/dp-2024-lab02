from datetime import datetime
import threading


from src.enums.level_enum import Level
from src.interfaces import ILogger, IWriter, IFormatter


class Logger(ILogger):
    """
    Класс для управления логированием сообщений

    Атрибуты:
        _instance: Экземпляр логгера, который используется для записи сообщений.
        _mutex_create: Мьютекс для блокировки потоков при создании экземпляра
        _mutex_write: Мьютекс для блокировки потоков при записи экземпляра

    Методы:
        log(level, message): Записывает сообщение с заданным уровнем.
    """

    _instance = None
    _mutex_create = threading.Lock()
    _mutex_write = threading.Lock()

    def __new__(cls, *args, **kwargs):
        return cls._create_singleton()

    def __init__(self, writer: IWriter, formatter: IFormatter):
        self._writer = writer
        self._formatter = formatter

    def set_writer(self, writer: IWriter):
        self._writer = writer

    def set_message_format(self, formatter: IFormatter):
        self._formatter = formatter

    def log(self, message: str, level: Level) -> None:
        """
        Метод для записи лога.

        :param message: Сообщение лога.
        :param level: Уровень Лога.
        :return: None.
        """

        log = self._genetare_log_message(message=message, level=level)
        with self._mutex_write:
            self._writer.write(self._formatter.format(log))

    def _genetare_log_message(self, message: str, level: Level) -> str:
        """
        Метод для формирования строки лога.

        :param message: Сообщение лога.
        :param level: Уровень Лога.
        :return: Строка лога.
        """
        time = str(datetime.now().strftime("%y-%m-%d %H:%M:%S"))
        return f"{time} [{level.value}] {message}"

    @classmethod
    def _create_singleton(cls):
        with cls._mutex_create:
            if not cls._instance:
                cls._instance = super().__new__(cls)

            return cls._instance
