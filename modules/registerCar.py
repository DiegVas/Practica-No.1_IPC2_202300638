# Importar la clase Car
from classes.Car import Car

def registerCar(ListCars):
    while True:
        placa = input("Ingrese la placa del auto: ")
        marca = input("Ingrese la marca del auto: ")
        modelo = input("Ingrese el modelo del auto: ")
        descripcion = input("Ingrese la descripción del auto: ")
       
               # Verificar que el precio unitario sea un número válido
        while True:
            precio_unitario = input("Ingrese el precio unitario del auto: ")
            try:
                precio_unitario = float(precio_unitario)
                break
            except ValueError:
                print("-----Por favor, ingrese un número válido para el precio unitario.------")
                print("")
        
        # Crear una instancia de Car
        auto = Car(placa, marca, modelo, descripcion, precio_unitario)
        
        # Agregar el auto a la lista de autos registrados
        ListCars.append(auto)
        
        print("\n//////////////////////////////////////////")
        print("Auto registrado exitosamente.")
        print("//////////////////////////////////////////\n")
        
        # Preguntar si desea registrar otro auto
        continuar = input("¿Desea registrar otro auto? (s/n): ").strip().lower()
        print("")
        if continuar != 's':
            break
        print("-----Registrando otro auto-----")
        
        