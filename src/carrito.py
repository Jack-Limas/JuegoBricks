class CarritoCompras:
    def __init__(self):
        self.items = {}

    def agregar_producto(self, producto, precio, cantidad=1):
        if producto in self.items:
            self.items[producto]["cantidad"] += cantidad
        else:
            self.items[producto] = {"precio": precio, "cantidad": cantidad}

    def eliminar_producto(self, producto):
        if producto in self.items:
            del self.items[producto]

    def obtener_total(self):
        return sum(item["precio"] * item["cantidad"] for item in self.items.values())
