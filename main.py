from modules.purchase import  purchase
from modules.registerCar import registerCar
from modules.registerClient import registerClient
from modules.report import generate_report
from modules.studentData import studentData

def menu():
    
    print("----------Menú de Opciones:----------")
    print("[1]. Registrar Auto")
    print("[2]. Registrar Cliente")
    print("[3]. Realizar Compra")
    print("[4]. Reporte de compras")
    print("[5]. Datos del Estudiante")
    print("[6]. Salir")
    print("")

def main():
    
    RegisterCars = []
    RegisterClients = []
    RegisterPurchases = []
    
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        print("")
         
        if opcion == '1':   
            print("--------Registro de Auto------------")
            print("")
            registerCar(RegisterCars)
           
            
        elif opcion == '2':           
            print("--------Registro de Cliente---------")
            registerClient(RegisterClients)
           
            
        elif opcion == '3':          
            print("--------Realizar Compra-------------")
            purchase(RegisterPurchases, RegisterClients, RegisterCars)
            
            
        elif opcion == '4':
            print("--------Reporte de Compras----------")
            generate_report(RegisterPurchases)
            
        elif opcion == '5':
            print("--------Datos del Estudiante--------")
            studentData()
            
        elif opcion == '6':
            print("--------Saliendo del programa-------")
            break
        
        else:
            
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()