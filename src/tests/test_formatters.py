import pytest
from src.formatters import InitialCaseFormatter, UpperCaseFormatter


def test_initial_formatter():
    formatter = InitialCaseFormatter()
    string = 'ABC_abc_123'
    formatted_string = formatter.format(string)
    assert formatted_string == string


def test_upper_formatter():
    formatter = UpperCaseFormatter()
    string = 'ABC_abc_123'
    formatted_string = formatter.format(string)
    assert formatted_string == string.upper()


