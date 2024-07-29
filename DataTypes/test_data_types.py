import pytest

from data_types import add_digits
@pytest.mark.parametrize("number, result", [
    ("12", 3),
    ("-32", 5),
    ("32", 5),
    ("89", 17),
    ("44",8),
    ("01", 1),
    ("-76", 13),
    ("76", 13)
])

def test_add_digits_of_number(number, result):
    assert add_digits(number) == result