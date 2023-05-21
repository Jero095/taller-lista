class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
class linkedlist:
    def __init__(self, valor):
        self.head = None
        
    def añadir_numero(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.head == None:
            self.head = nuevo_nodo
        else:

            nodo_actual = self.head
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
    
    def insertar_en_posición(self, valor):
        i = 0
        index = int(input())
        nuevo_nodo = Nodo(valor)
        nodo_actual = self.head
        if index == 1 and self.head == None:
            self.head = nuevo_nodo
        elif index == 1:
            nodo_actual = self.head
            nuevo_nodo.siguiente = nodo_actual
            self.head = nuevo_nodo
        elif index >1:
            while  nodo_actual.siguiente != None:
                nodo_actual = nodo_actual.siguiente
                i = i+1
                if i == index:
                    nuevo_nodo.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente = nuevo_nodo
                else:
                    print("La posición no existe en la lista.")
    def longitud(self):
        nodo_actual = self.head
        if nodo_actual.siguiente == None:
            print("hay 1 numero en la lista")
        contador = 1
        while  nodo_actual.siguiente != None:
                nodo_actual = nodo_actual.siguiente
                contador = contador+1
        print("hay " + contador +" numeros en la lista")
    def eliminar_ultimo(self):
        nodo_actual = self.head
        nodo_anetrior = None
        if self.head ==None:
            print("la lista está vacia")
        while nodo_actual.siguiente != None:
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
        nodo_anterior.siguiente = None
    
        
        

