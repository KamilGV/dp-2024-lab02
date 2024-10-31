from unittest.mock import Mock, patch, mock_open
from src.writers import ConsoleWriter, FileWriter


def test_console_writer():
    with patch("builtins.print") as mock_print:
        string = "Test Message 123"
        writer = ConsoleWriter()
        writer.write(string)
        mock_print.assert_called_once_with(string)


def test_file_writer():
    with patch("builtins.open", new_callable=mock_open) as file_open:
        file_path = "test_path.txt"
        string = "Test Message 123"
        writer = FileWriter(file_path=file_path)
        writer.write(string)
        file_open.assert_called_once_with(file_path, "a")
        file_open().write.assert_called_once_with(string + "\n")
