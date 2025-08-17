# ╔════════════════════════════════════════════════════════════════╗
# ║                       ÁRBOL B                                  ║
# ╠════════════════════════════════════════════════════════════════╣
# ║ FECHA:      29/07/2025                                         ║
# ║ CURSO:      Estructura de datos II                             ║
# ║ DOCENTE:    Ing. Luis Hernández                                ║
# ║ INSTITUCIÓN:URL                                                ║
# ╠════════════════════════════════════════════════════════════════╣
# ║ DESCRIPCIÓN:                                                   ║
# ║ Código corregido para seguir la metodología tradicional:       ║
# ║     claves máximo    u=ORDEN-1                                 ║
# ║     claves mínimas   l=(ORDEN//2)-1                            ║
# ╚════════════════════════════════════════════════════════════════╝

class NodoB:
    def __init__(self, orden, es_hoja=True):
        self.orden = orden              # Grado mínimo (orden del árbol B)
        self.claves = []               # Lista de claves (valores) almacenadas en este nodo
        self.hijos = []                # Lista de hijos de este nodo
        self.es_hoja = es_hoja         # Indica si este nodo es una hoja

class ArbolB:
    def __init__(self, orden):
        if orden < 2:
            raise ValueError("El orden del arbol B debe ser al menos 2")
        self.orden = orden             # Se define el orden del árbol
        self.raiz = NodoB(orden)       # Se crea la raíz vacía inicialmente

    def insertar(self, clave):
        raiz = self.raiz
        
        # CORREGIDO: Un nodo está lleno cuando tiene (orden - 1) claves
        if len(raiz.claves) == self.orden - 1:
            nueva_raiz = NodoB(self.orden, False)  # La nueva raíz no es hoja
            nueva_raiz.hijos.append(self.raiz)     # La raíz actual se vuelve hijo
            self._dividir_hijo(nueva_raiz, 0)      # Dividir el hijo lleno
            self.raiz = nueva_raiz                 # Actualizar la raíz
            
        self._insertar_no_lleno(self.raiz, clave)

    def _insertar_no_lleno(self, nodo, clave):
        i = len(nodo.claves) - 1
        
        if nodo.es_hoja:
            # Insertar en hoja: encontrar posición e insertar
            nodo.claves.append(0)  # Expandir la lista
            while i >= 0 and nodo.claves[i] > clave:
                nodo.claves[i + 1] = nodo.claves[i]
                i -= 1
            nodo.claves[i + 1] = clave
        else:
            # Insertar en nodo interno: encontrar el hijo correcto
            while i >= 0 and nodo.claves[i] > clave:
                i -= 1
            i += 1
            
            # CORREGIDO: Si el hijo está lleno, dividirlo
            if len(nodo.hijos[i].claves) == self.orden - 1:
                self._dividir_hijo(nodo, i)
                if nodo.claves[i] < clave:
                    i += 1
            
            self._insertar_no_lleno(nodo.hijos[i], clave)

    def _dividir_hijo(self, padre, indice):
        hijo_lleno = padre.hijos[indice]
        nuevo_hijo = NodoB(self.orden, hijo_lleno.es_hoja)
        
        # CORREGIDO: Índice del medio para metodología tradicional
        # Con orden n, tenemos n-1 claves máximo
        # El medio está en la posición (n-1)//2
        medio = (self.orden - 1) // 2
        
        # IMPORTANTE: Extraer la clave del medio ANTES de modificar las listas
        clave_medio = hijo_lleno.claves[medio]
        
        # Mover las claves de la mitad superior al nuevo nodo
        nuevo_hijo.claves = hijo_lleno.claves[medio + 1:]
        hijo_lleno.claves = hijo_lleno.claves[:medio]
        
        # Si no es hoja, mover también los hijos
        if not hijo_lleno.es_hoja:
            nuevo_hijo.hijos = hijo_lleno.hijos[medio + 1:]
            hijo_lleno.hijos = hijo_lleno.hijos[:medio + 1]
        
        # Insertar el nuevo hijo en el padre
        padre.hijos.insert(indice + 1, nuevo_hijo)
        
        # Mover la clave del medio al padre
        padre.claves.insert(indice, clave_medio)

    def buscar(self, clave, nodo=None):
        if nodo is None:
            nodo = self.raiz
            
        i = 0
        while i < len(nodo.claves) and clave > nodo.claves[i]:
            i += 1
            
        # Si encontramos la clave
        if i < len(nodo.claves) and clave == nodo.claves[i]:
            print(f" Clave {clave} encontrada en el nodo: {nodo.claves}")
            return True
            
        # Si es hoja y no se encontró
        if nodo.es_hoja:
            print(f" Clave {clave} no encontrada.")
            return False
            
        # Buscar recursivamente en el hijo apropiado
        return self.buscar(clave, nodo.hijos[i])

    def mostrar(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
            
        # Solo mostrar nodos que tienen claves
        if len(nodo.claves) > 0:
            print("  " * nivel + str(nodo.claves))
            
        # Mostrar hijos solo si no es hoja
        if not nodo.es_hoja:
            for hijo in nodo.hijos:
                self.mostrar(hijo, nivel + 1)

    '''
    def verificar_propiedades(self, nodo=None, es_raiz=True):
        """Función para verificar que el árbol cumple las propiedades del Árbol B"""
        if nodo is None:
            nodo = self.raiz
            
        claves_max = self.orden - 1
        claves_min = (self.orden // 2) - 1 if not es_raiz else 0
        
        # Verificar número de claves
        num_claves = len(nodo.claves)
        if num_claves > claves_max:
            print(f"ERROR: Nodo {nodo.claves} tiene {num_claves} claves, máximo permitido: {claves_max}")
            return False
        if num_claves < claves_min:
            print(f"ERROR: Nodo {nodo.claves} tiene {num_claves} claves, mínimo requerido: {claves_min}")
            return False
            
        print(f"✓ Nodo {nodo.claves}: {num_claves} claves (min: {claves_min}, max: {claves_max})")
        
        # Verificar hijos recursivamente
        if not nodo.es_hoja:
            for hijo in nodo.hijos:
                if not self.verificar_propiedades(hijo, False):
                    return False
                    
        return True
    '''