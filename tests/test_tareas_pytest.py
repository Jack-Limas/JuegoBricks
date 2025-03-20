import pytest
from src.tareas import Tareas

@pytest.fixture
def gestor_tareas():
    return Tareas()

def test_agregar_tarea(gestor_tareas):
    gestor_tareas.agregar_tarea("Comprar pan")
    assert "Comprar pan" in gestor_tareas.listar_tareas()

def test_eliminar_tarea(gestor_tareas):
    gestor_tareas.agregar_tarea("Ir al gimnasio")
    assert gestor_tareas.eliminar_tarea("Ir al gimnasio") is True
    assert "Ir al gimnasio" not in gestor_tareas.listar_tareas()

def test_agregar_tarea_invalida(gestor_tareas):
    with pytest.raises(ValueError):
        gestor_tareas.agregar_tarea("")
