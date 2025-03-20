class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("El depósito debe ser mayor a cero")
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad

    def obtener_saldo(self):
        return self.saldo
