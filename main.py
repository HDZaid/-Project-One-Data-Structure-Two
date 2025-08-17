print('my work  here was finished, but yours is started now :) ')
from proveedor import Proveedor
from arbolB import ArbolB

def main():
    # Crear instancia del árbol B
    arbol = ArbolB()

    # Crear algunos proveedores
    proveedor1 = Proveedor("Proveedor A", "Calle 123", "555-1234")
    proveedor2 = Proveedor("Proveedor B", "Avenida 456", "555-5678")
    proveedor3 = Proveedor("Proveedor C", "Boulevard 789", "555-9012")

    # Insertar proveedores en el arbol B
    arbol.insertar(proveedor1)
    arbol.insertar(proveedor2)
    arbol.insertar(proveedor3)

    # Buscar un proveedor
    resultado = arbol.buscar("Proveedor B")
    if resultado:
        print("Proveedor encontrado:", resultado)
    else:
        print("Proveedor no encontrado")
    

main()