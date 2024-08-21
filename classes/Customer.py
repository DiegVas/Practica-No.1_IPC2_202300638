class Customer:
    def __init__(self, name, email, nit):
        self.name = name
        self.email = email
        self.nit = nit

    def detalles(self):
        return (f"Nombre: {self.name}\n"
                f"Correo Electrónico: {self.email}\n"
                f"NIT: {self.nit}")

