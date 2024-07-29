import pytest
from bmi_calculator import bmi_calculator

@pytest.mark.parametrize(" weight, height, result", [
    (85, 1.8, 26),
    (90, 1.6, 35),
    (8, 2, 2),
    (72, 1.65, 26)
])

def test_bmi_calculator(weight, height, result):
    assert bmi_calculator(weight, height) == result