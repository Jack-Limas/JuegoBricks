import pytest
from src.banco import CuentaBancaria

@pytest.fixture
def cuenta():
    return CuentaBancaria(100)

def test_depositar(cuenta):
    cuenta.depositar(50)
    assert cuenta.obtener_saldo() == 150

def test_retirar(cuenta):
    cuenta.retirar(30)
    assert cuenta.obtener_saldo() == 70

def test_retirar_saldo_insuficiente(cuenta):
    with pytest.raises(ValueError):
        cuenta.retirar(200)

def test_saldo_inicial_negativo():
    with pytest.raises(ValueError):
        CuentaBancaria(-10)
