from proveedor import Proveedor
from arbolB import ArbolB
#funcion que inserta datos iniciales en el arbol
def insertar_datos(arbol):
   
    proveedor1 = Proveedor("Miku", "1", "electricista", 5)
    proveedor2 = Proveedor("Teto", "2", "plomera", 4)
    proveedor3 = Proveedor('kasane', '3', 'carpintero', 3)
    proveedor4 = Proveedor("Lucho", "4", "pintor", 2)
    proveedor5 = Proveedor("Marta", "5", "jardinera", 5)
    proveedor6 = Proveedor("Ana", "6", "soldador", 4) 
    proveedor7 = Proveedor("Lucho", "7", "dentista", 2)
    proveedor8 = Proveedor("Celia", "8", "piloto", 5)
    proveedor9 = Proveedor("Alicia", "9", "doctor", 4)
    proveedor10 = Proveedor("Goku", "10", "programador", 4)  
    proveedor11 = Proveedor("Jimbo", "3", "carpintero", 3)
    proveedor12 = Proveedor("Rita", "4", "abogada", 2)
    

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
    arbol.insertar(proveedor11)
    arbol.insertar(proveedor12)
#funcion que se encarga de validar las entradas de numeros
def pedir_numero():
    while True:
        try:
            numero = int(input(""))
            return numero  
        except ValueError:
            print("Error: debe ingresar un número válido. Inténtelo de nuevo.")
#funcion que retorna la seleccion de la profesion
def retornar_profesion(numero):

        if numero < 1 or numero > 13:
            print("Número de profesión no válido. Debe ser entre 1 y 12.")
            return None
        # Retorna la profesión según el número ingresado
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
        elif numero == 11:
            return "Abogado"
        elif numero == 12:
            return "Arquitecto"
        else:
            return None   
#prints de todas las profesiones 
def mostrar_profesiones():
    print("Profesiones disponibles:")
    print("[ 1 ] electricista")
    print("[ 2 ] plomera")
    print("[ 3 ] carpintero")
    print("[ 4 ] pintor")
    print("[ 5 ] jardinera")
    print("[ 6 ] soldador")
    print("[ 7 ] dentista")
    print("[ 8 ] piloto")
    print("[ 9 ] doctor")
    print("[ 10 ] programador")
    print("[ 11 ] abogado")
    print("[ 12 ] arquitecto")
    print("ingresa el numero de la profesión que desea agregar al proveedor:")
#print del menu principal
def menu_principal():
    print(" ---------------------------------------- ")
    print(" BIENVENIDO A SERVICIOS LOCALES S.A. ")
    print(" ---------------------------------------- ")
    print("[ 1 ] INSERTAR UN NUEVO PROVEEDOR")
    print("[ 2 ] BUSCAR PROVEEDORES POR SERVICIO")
    print("[ 3 ] VISUALIZAR PROVEEDORES")
    print("[ 4 ] recorrido con forme al orden del arbol")
    print("[ 5 ] SALIR")

def main():
    # Crear instancia del arbol B
    print("Ingrese el tamaño de orden del arbol B (debe ser mayor o igual a 2):")
    #solicitamos al usuario ingresar el tamaño del orden del arbol
    while True:
                try:
                    tamano_orden = pedir_numero()
                    if 1 <= tamano_orden > 1:
                        break
                    else:
                        print("El tamaño del orden debe ser mayor o igual a 2. Intentelo de nuevo.")
                except ValueError:
                    print("Error: debe ingresar un valor valido. Intentelo de nuevo.")
    
    arbol = ArbolB(tamano_orden)
    # Insertar datos de proveedores
    insertar_datos(arbol)#llama la funcion que ingresa los datos iniciales
    #inicio del menu principal
    while True:
        menu_principal()
        opcion = pedir_numero()
        #Opcion 1 del menu, insertar un nuevo proveedor
        if opcion == 1:
            nombre = input("Ingrese el nombre del proveedor: ")
            id = input("Ingrese el ID del proveedor: ")
            mostrar_profesiones()

            while True:
                try :
                    numero_profesion = pedir_numero()
                    servicio = retornar_profesion(numero_profesion)
                    if servicio is not None:
                        break
                except ValueError:
                    print("Error: debe ingresar un número valido. Intentelo de nuevo.")

            while True:
                try:
                    print("Ingrese la calificacion del proveedor (1 a 5):")
                    calificacion = pedir_numero()
                    if 1 <= calificacion <= 5:
                        break
                    else:
                        print("La calificacion debe estar entre 1 y 5. Intentelo de nuevo.")
                except ValueError:
                    print("Error: debe ingresar un número valido. Intentelo de nuevo.")

            nuevo_proveedor = Proveedor(nombre, id, servicio, calificacion)
            arbol.insertar(nuevo_proveedor)
            print(f"Proveedor: {nombre}, que brinda el servicio de: {servicio} ha sido insertado correctamente.")
        #opcion 2 del menu, buscar proveedores por servicio
        elif opcion == 2:
            servicio_buscar = input("Ingrese el tipo de servicio a buscar: ")
            proveedores = arbol.buscar_oficio(servicio_buscar) 
            
            if len(proveedores) > 0:
                print(f"\nProveedores que brindan el servicio de {servicio_buscar}:")
                for i in proveedores:
                    print(i)   
            else:
                print(f"No se encontraron proveedores que brinden el servicio de {servicio_buscar}.")
        #opcion 3 del menu, visualizar un listado de los proveedores en funcion a su nombre o calificacion
        elif opcion == 3:
            while True:
                print('='*50)
                print("Visualizando proveedores:")
                print('[ 1 ] Mostrar proveedores por Nombre')
                print('[ 2 ] Mostrar proveedores por Calificacion')
                print('[ 3 ] Salir')
                print('Seleccione una opcion:')
                opcion1 = pedir_numero()
                listed_nodes = arbol.enlistar() 

                if opcion1 == 1:
                    print("\n=== Mostrando proveedores por nombre ===")
                    listed_nodes.sort(key=lambda x: x.nombre)  # Ordenar por nombre
                    for proveedor in listed_nodes:
                        print(proveedor)
                    
                elif opcion1 == 2:
                    print("\n=== Mostrando proveedores por calificacion descendente ===")
                    listed_nodes.sort(key=lambda x: x.calificacion, reverse=True)  # Ordenar por calificacion descendente
                    for proveedor in listed_nodes:
                        print(proveedor)
                    
                elif opcion1 == 3:
                    print("Saliendo de la visualizacion de proveedores")
                    break
                else:
                    print("Opcion no valida. Intente nuevamente.")
        #opcion 4 del menu, recorrido con forme al ID almacenado en el arbol

        elif opcion == 4:
            print("METODO DE MOSTRAR EL ARBOL #1")
            arbol.mostrar()  # Mostrar el árbol final de forma "visual"
            break

        elif opcion == 5:
            print("SALIENDO DEL PROGRAMA")
            break

        else:
            print("Opcion no valida. Intente nuevamente.")  
    
    
    
    

if __name__ == "__main__":
    main()
