import pytest

from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator

    def test_multiply_success(self):
        assert self.calculator.multiply(self, 20, 3) ==60

    def test_division_success(self):
        assert self.calculator.division(self, 100, 50) == 2

    def test_subtraction_success(self):
        assert self.calculator.subtraction(self, 8, 42) == -34

    def test_adding_success(self):
            assert self.calculator.adding(self, 101, 1) ==102

