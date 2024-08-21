from classes.Customer import Customer

def registerClient(ListClients):
    while True:
        print("")
        name = input("Ingrese el nombre del cliente: ")
        email = input("Ingrese el correo electrónico del cliente: ")
        nit = input("Ingrese el NIT del cliente: ")
        
        # Crear una instancia de Customer
        cliente = Customer(name, email, nit)
        
        # Agregar el cliente a la lista de clientes registrados
        ListClients.append(cliente)
        
        print("Cliente registrado exitosamente.")
        print("----------------------------------")
        print("")
        
        # Preguntar si desea registrar otro cliente
        continuar = input("¿Desea registrar otro cliente? (s/n): ").strip().lower()
        print("")
        print("-------Resgistrar otro Cliente---------")
        if continuar != 's':
            break