import pytest

@pytest.mark.parametrize("number, result", [
    ("12", 3),
    ("-32", 5),
    ()
    ("89", 17),
    ("44",8),
    ("01", 1),
    ("-76", 13)
])