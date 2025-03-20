# test_calculadora_pytest.py
import pytest
from calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_suma(calc):
    assert calc.suma(2, 3) == 5
    assert calc.suma(-1, 1) == 0

def test_resta(calc):
    assert calc.resta(10, 4) == 6

def test_division(calc):
    assert calc.division(10, 2) == 5

    with pytest.raises(ValueError):
        calc.division(5, 0)