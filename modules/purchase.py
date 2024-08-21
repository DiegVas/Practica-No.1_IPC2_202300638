
from classes.Purchase_details import Purchase_details

def purchase(registerPurchases ,customers, cars):
    customers_dict = {customer.nit: customer for customer in customers}
    
    nit = input("Ingrese el NIT del cliente: ")
    customer = customers_dict.get(nit, None)
    if not customer:
        print("Cliente no encontrado.")
        return
    
    purchase = Purchase_details(nit,customer)
    
    while True:
        print("----Menu de compra----")
        print("\n1. Agregar Auto")
        print("2. Terminar Compra y Generar Factura")
        option = input("Seleccione una opción: ").strip()
        
        if option == '1':
            placa = input("Ingrese la placa del auto: ")
            car = next((c for c in cars if c.placa == placa), None)
            
            if not car:
                print("Auto no encontrado.")
            else:
                purchase.add_car(car)
                print("Auto agregado a la compra.")
        
        elif option == '2':
            add_insurance = input("¿Desea agregar seguro al auto? (s/n): ").strip().lower() == 's'
            
            if add_insurance:
                purchase.costo_total = sum(car.precio_unitario for car in purchase.lista_productos) + sum(car.precio_unitario * 0.15 for car in purchase.lista_productos)
            else:
                purchase.costo_total = sum(car.precio_unitario for car in purchase.lista_productos)
            
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
    purchase.id = len(registerPurchases) + 1       
    registerPurchases.append(purchase)