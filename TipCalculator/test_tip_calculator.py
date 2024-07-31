import pytest

from tip_calculator import tip_calculator

#Tip calculator test
@pytest.mark.parametrize("bill, tip, people, amount", [
    (150, 10, 5, 33.00),
    (150, 12, 5, 33.60),
    (150, 15, 5, 34.50),
    (300, 10, 4, 82.50),
    (300, 12, 4, 84.00),
    (300, 15, 4, 86.25),
    (147, 12, 3, 54.88),
    (239, 15, 6, 45.81),
    (352.99, 12, 2, 197.67)
])

class TestTipCalculator:
    def test_tip_calculator(self, bill, tip, people, amount):
        assert tip_calculator(bill, tip, people) == amount