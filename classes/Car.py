class Car:

    def __init__(self, placa, marca, modelo, descripcion, precio_unitario):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario

    def detalles(self):
        return (f"Placa: {self.placa}\n"
                f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Descripción: {self.descripcion}\n"
                f"Precio Unitario: Q{self.precio_unitario:.2f}")
