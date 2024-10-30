from src.interfaces import IWriter


class FileWriter(IWriter):
    def __init__(self, file_path):
        self._file_path = file_path

    """
    Класс для запиcи логов
        Аттрибуты:
        file_path: Путь до файла

        Методы:
        write(message): Записывает сообщение в файл.
    """

    def write(self, message) -> None:
        """
        Метод для записи лога в текстовый файл.

        :param message: Сообщение.
        :return: None.
        """
        with open(self._file_path, 'a') as f:
            f.write(f"{message}\n")
