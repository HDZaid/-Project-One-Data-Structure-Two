class NodoB:
    def __init__(self, orden):
        self.orden = orden              # Grado mínimo (orden del árbol B)
        self.claves = []               # Lista de claves (valores) almacenadas en este nodo
        self.hijos = []                # Lista de hijos de este nodo
        self.hoja = True               # Por defecto, todo nuevo nodo es una hoja
class ArbolB:
    def __init__(self, orden):
        self.orden = orden             # Se define el orden del árbol (por ejemplo, 2)
        self.raiz = NodoB(orden)       # Se crea la raíz vacía inicialmente

    def insertar(self, clave):
        nodo_raiz = self.raiz

        # PASO 1: Verificamos si la raíz está llena (tiene 2*orden - 1 claves)
        if len(nodo_raiz.claves) == 2 * self.orden - 1:
            
            # Si está llena, se crea una nueva raíz
            nueva_raiz = NodoB(self.orden)
            nueva_raiz.hoja = False   # La nueva raíz no es hoja
            nueva_raiz.hijos.append(self.raiz)  # La raíz anterior se vuelve hijo

            # Se divide el hijo lleno (la raíz antigua)
            self.dividir(nueva_raiz, 0)

            # Ahora se inserta la clave en la nueva raíz
            self.insertar_en_nodo(nueva_raiz, clave)

            # Actualizamos la raíz del árbol
            self.raiz = nueva_raiz
        else:
            # Si la raíz no está llena, insertamos normalmente
            self.insertar_en_nodo(nodo_raiz, clave)

    def insertar_en_nodo(self, nodo_actual, clave):
        # PASO 2: Insertar la clave en el nodo correspondiente

        if nodo_actual.hoja:
            # Si el nodo actual es una hoja, simplemente insertamos la clave
            nodo_actual.claves.append(clave)
            nodo_actual.claves.sort()  # Ordenamos las claves (mantener orden)
        else:
            # Si no es hoja, buscamos en qué hijo debe ir la clave
            i = 0
            while i < len(nodo_actual.claves) and clave > nodo_actual.claves[i]:
                i += 1

            # PASO 3: Verificamos si el hijo donde va la clave está lleno
            if len(nodo_actual.hijos[i].claves) == 2 * self.orden - 1:
                # Si está lleno, lo dividimos
                self.dividir(nodo_actual, i)

                # Luego de dividir, puede cambiar la posición donde debemos insertar
                if clave > nodo_actual.claves[i]:
                    i += 1

            # PASO 4: Insertar recursivamente en el hijo adecuado
            self.insertar_en_nodo(nodo_actual.hijos[i], clave)

    def dividir(self, nodo_padre, i):
        t = self.orden
        nodo_hijo = nodo_padre.hijos[i]

        nuevo_nodo = NodoB(self.orden)
        nuevo_nodo.hoja = nodo_hijo.hoja

        # Clave del medio
        clave_mitad = nodo_hijo.claves[t - 1]

        # Dividir claves
        nuevo_nodo.claves = nodo_hijo.claves[t:]     # Parte derecha
        nodo_hijo.claves = nodo_hijo.claves[:t - 1]  # Parte izquierda

        # Si no es hoja, dividir hijos
        if not nodo_hijo.hoja:
            nuevo_nodo.hijos = nodo_hijo.hijos[t:]
            nodo_hijo.hijos = nodo_hijo.hijos[:t]

        # Insertar en el padre
        nodo_padre.claves.insert(i, clave_mitad)
        nodo_padre.hijos.insert(i + 1, nuevo_nodo)


    def mostrar(self, nodo_actual=None, nivel=0):
        # Imprimir recursivamente el árbol por niveles (identado)
        if nodo_actual is None:
            nodo_actual = self.raiz
        print("  " * nivel + str(nodo_actual.claves))
        for hijo in nodo_actual.hijos:
            self.mostrar(hijo, nivel + 1)

    def buscar(self, clave, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz

        # Buscar la posición donde la clave podría estar en este nodo
        i = 0
        while i < len(nodo_actual.claves) and clave > nodo_actual.claves[i]:
            i += 1

        # Si la clave se encuentra en este nodo
        if i < len(nodo_actual.claves) and nodo_actual.claves[i] == clave:
            print(f" Clave {clave} encontrada en el nodo: {nodo_actual.claves}")
            return True

        # Si es hoja y no se encontró
        if nodo_actual.hoja:
            print(f" Clave {clave} no encontrada.")
            return False

        # Si no es hoja, buscar recursivamente en el hijo correspondiente
        return self.buscar(clave, nodo_actual.hijos[i])
