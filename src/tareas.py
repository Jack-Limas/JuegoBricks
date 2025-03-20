class Tareas:
    def __init__(self):
        self.lista = []

    def agregar_tarea(self, tarea):
        if not isinstance(tarea, str) or not tarea.strip():
            raise ValueError("La tarea debe ser una cadena no vacía")
        self.lista.append(tarea)

    def eliminar_tarea(self, tarea):
        if tarea in self.lista:
            self.lista.remove(tarea)
            return True
        return False

    def listar_tareas(self):
        return self.lista
