from src.interfaces import IFormatter


class InitialCaseFormatter(IFormatter):

    def format(self, message: str) -> str:
        return message


class UpperCaseFormatter(IFormatter):

    def format(self, message: str) -> str:
        return message.upper()
