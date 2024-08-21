

def generate_report(RegisterPurchases):
    print("------------- REPORTE DE COMPRAS -------------\n")
    print( "==============================================\n")
    total_general = 0.0

    for compra in RegisterPurchases:
        print( f"CLIENTE:\nNombre: {compra.cliente.name}")
        print( f"Correo electrónico: {compra.cliente.email}")
        print( f"Nit: {compra.nit}\n")
        print( "AUTO(S) ADQUIRIDO(S)\n")
        for auto in compra.lista_productos:
            print( f"{auto.detalles()}\n")
        print( f"TOTAL: Q{compra.costo_total:.2f}\n")
        print( "==============================================\n")
        total_general += compra.costo_total

    print( f"Total General: Q{total_general:.2f}\n")
    print( "---------------------------------------------")
    return