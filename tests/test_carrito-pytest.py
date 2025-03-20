import pytest
from src.carrito import CarritoCompras

@pytest.fixture
def carrito():
    return CarritoCompras()

def test_agregar_producto(carrito):
    carrito.agregar_producto("Laptop", 1000, 2)
    assert carrito.obtener_total() == 2000

def test_eliminar_producto(carrito):
    carrito.agregar_producto("Mouse", 50, 1)
    carrito.eliminar_producto("Mouse")
    assert carrito.obtener_total() == 0

def test_total_carrito(carrito):
    carrito.agregar_producto("Teclado", 150, 1)
    carrito.agregar_producto("Monitor", 300, 2)
    assert carrito.obtener_total() == 750
