from proveedor import Proveedor
from arbolB import ArbolB

def insertar_datos(arbol):
   
    proveedor1 = Proveedor("Miku", "1", "Electricista", "5")
    proveedor2 = Proveedor("Teto", "2", "Plomera", "4")
    proveedor3 = Proveedor("Jimbo", "3", "Carpintero", "3")
    proveedor4 = Proveedor("Lucho", "4", "Pintor", "2")
    proveedor5 = Proveedor("Marta", "5", "Jardinera", "5")
    proveedor6 = Proveedor("Ana", "6", "Soldador", "4") 
    proveedor7 = Proveedor("Lucho", "7", "Dentista", "2")
    proveedor8 = Proveedor("Marta", "8", "Piloto", "5")
    proveedor9 = Proveedor("Ana", "9", "Doctor", "4")
    proveedor10 = Proveedor("Goku", "10", "Programador", "4")  

    arbol.insertar(proveedor1)
    arbol.insertar(proveedor2)
    arbol.insertar(proveedor3)
    arbol.insertar(proveedor4)
    arbol.insertar(proveedor5)
    arbol.insertar(proveedor6)
    arbol.insertar(proveedor7)
    arbol.insertar(proveedor8)
    arbol.insertar(proveedor9)
    arbol.insertar(proveedor10)

def retornar_profesion(numero):
    
    if numero == 1:
        return "Electricista"
    elif numero == 2:
        return "Plomera"
    elif numero == 3:
        return "Carpintero"
    elif numero == 4:
        return "Pintor"
    elif numero == 5:
        return "Jardinera"
    elif numero == 6:
        return "Soldador"
    elif numero == 7:
        return "Dentista"
    elif numero == 8:
        return "Piloto"
    elif numero == 9:
        return "Doctor"
    elif numero == 10:
        return "Programador"
    else:
        return None
    
def mostrar_profesiones():
    print("Profesiones disponibles:")
    print("[ 1 ] Electricista")
    print("[ 2 ] Plomera")
    print("[ 3 ] Carpintero")
    print("[ 4 ] Pintor")
    print("[ 5 ] Jardinera")
    print("[ 6 ] Soldador")
    print("[ 7 ] Dentista")
    print("[ 8 ] Piloto")
    print("[ 9 ] Doctor")
    print("[ 10 ] Programador")
        
def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese el número de la profesión: "))
            return numero  
        except ValueError:
            print("Error: debe ingresar un número válido. Inténtelo de nuevo.")


def menu_principal():
    print(" ---------------------------------------- ")
    print(" BIENVENIDO A SERVICIOS LOCALES S.A. ")
    print(" ---------------------------------------- ")
    print("[ 1 ] INSERTAR UN NUEVO PROVEEDOR")
    print("[ 2 ] BUSCAR PROVEEDORES POR SERVICIO")
    print("[ 3 ] VISUALIZAR PROVEEDORES")
    print("[ 4 ] SALIR")

def main():
    # Crear instancia del árbol B
    tamano_orden = int(input("Ingrese el orden del árbol B (minimo 2): "))
    arbol = ArbolB(tamano_orden)
    # Insertar datos de proveedores
    insertar_datos(arbol)

    while True:
        menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del proveedor: ")
            id = input("Ingrese el ID del proveedor: ")
            while True:
                profesion = int(input("Ingrese la profesión del proveedor: "))
            
            servicio = input("Ingrese el tipo de servicio: ") 


            calificacion = input("Ingrese la calificación del proveedor: ")






            nuevo_proveedor = Proveedor(nombre, id, servicio, calificacion)
            arbol.insertar(nuevo_proveedor)
            print(f"Proveedor: {nombre}, que brinda el servicio de: {servicio} ha sido insertado correctamente.")

        elif opcion == "2":
            servicio_buscar = input("Ingrese el tipo de servicio a buscar: ")
            arbol.buscar(servicio_buscar)

        elif opcion == "3":
            while True:
                print('='*50)
                print("Visualizando proveedores:")
                print('[ 1 ] Mostrar proveedores por Nombre')
                print('[ 2 ] Mostrar proveedores por Calificación')
                print('[ 3 ] Salir')
                opcion1 = input("Seleccione una opción: ")
                if opcion1 == "1":
                    # Aquí se podría implementar la lógica para mostrar proveedores por nombre
                    pass
                elif opcion1 == "2":
                    # Aquí se podría implementar la lógica para mostrar proveedores por calificación
                    pass
                elif opcion1 == "3":
                    print("Saliendo de la visualización de proveedores...")
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")  
    
    

if __name__ == "__main__":
    main()
