import pytest
from src.generador import GeneradorContrasena

@pytest.fixture
def generador():
    return GeneradorContrasena()

def test_generar_contrasena(generador):
    contrasena = generador.generar(10)
    assert len(contrasena) == 10

def test_contrasena_corta(generador):
    with pytest.raises(ValueError):
        generador.generar(3)
