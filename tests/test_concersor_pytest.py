import pytest
from src.conversor import ConversorTemperatura

@pytest.fixture
def conversor():
    return ConversorTemperatura()

def test_celsius_a_fahrenheit(conversor):
    assert conversor.celsius_a_fahrenheit(0) == 32
    assert conversor.celsius_a_fahrenheit(100) == 212
    assert conversor.celsius_a_fahrenheit(-40) == -40

def test_fahrenheit_a_celsius(conversor):
    assert conversor.fahrenheit_a_celsius(32) == 0
    assert conversor.fahrenheit_a_celsius(212) == 100
    assert conversor.fahrenheit_a_celsius(-40) == -40
