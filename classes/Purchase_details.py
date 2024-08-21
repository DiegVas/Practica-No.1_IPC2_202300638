from classes.Customer import Customer
from classes.Car import Car

class Purchase_details:

    lista_productos = []
    id = 0

    def __init__(self,nit, cliente: Customer):
        self.nit = nit
        self.cliente = cliente
        self.costo_total = 0.0

    def add_car(self, auto: Car):
        self.lista_productos.append(auto)
        self.costo_total += auto.precio_unitario
