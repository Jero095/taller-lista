class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
class linkedlist:
    def __init__(self):
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
    
    def insertar_en_posición(self, valor, index):
        i = 0
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
        return contador
        print("hay " + contador +" numeros en la lista")
    def eliminar_ultimo(self):
        nodo_actual = self.head
        nodo_anterior = None
        if self.head ==None:
            print("la lista está vacia")
            return
        elif self.head.siguiente is None:
            ultimo_valor = self.head.valor
            self.head = None
            return ultimo_valor
        else:
            while nodo_actual.siguiente != None:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
            ultimo_valor = nodo_anterior.siguiente.valor
            nodo_anterior.siguiente = None
            return ultimo_valor
    def eliminar_ubicacion(self, index):
        contador =1
        nodo_anterior = None
        nodo_actual = self.head
        if nodo_actual == None:
            print("la lista está vacia")
            return None
        elif index ==1 and nodo_actual.siguiente != None:
            self.head = nodo_actual.siguiente
            return nodo_actual.valor
        elif index ==1:
            print("se elimino el unico elemento de la lista")
        elif index >1:
            nodo_actual =self.head
            while contador < index - 1 and nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
                contador = contador +1
            if contador == index - 1 and nodo_actual.siguiente:
                valor = nodo_actual.siguiente.valor

                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return valor
            else:
                print("La posición no existe en la lista.")
                return None
    def coincidencias(self, valorr):
        coincidencias = 0
        nodo_actual = self.head
        while nodo_actual.siguiente != None:
            nodo_actual = nodo_actual.siguiente
            if nodo_actual.valor ==valorr:
                coincidencias = coincidencias +1
        return coincidencias
    def posiciones_del_numero(self, valorr):
        posiciones = []
        nodo_actual = self.head
        nodo_actual_posicion = 1
        while nodo_actual:
            if nodo_actual.valor == valorr:
                posiciones.append(nodo_actual_posicion)
            nodo_actual = nodo_actual.siguiente
            nodo_actual_posicion += 1
        return posiciones
    def imprimir(self):
        nodo_actual = self.head
        while nodo_actual:
            print(nodo_actual.valor, end=' ')
            nodo_actual = nodo_actual.siguiente
        print()
                
def mostrar_menu():
    print("1 : Añadir número a la lista, pide un número de la lista y lo añade al final de la lista.")
    print("2 : Añadir número de la lista en una posición")
    print("3 : Longitud de la lista")
    print("4 : Eliminar el último número")
    print("5 : Eliminar un número")
    print("6 : Contar números")
    print("7 : Posiciones de un número")
    print("8 : Mostrar números")
    print("9 : Salir")

my_list = linkedlist()

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion =="1":
        numero = int(input("Ingrese un número: "))
        my_list.añadir_numero(numero)
        print("Número añadido a la lista.")
    elif opcion == "2":
        valor = int(input("Ingrese un número: "))
        index = int(input("Ingrese una posición: "))
        my_list.insertar_en_posición(numero, index)
        print("Número añadido a la lista en la posición", index)
    elif opcion == "3":
        longitud = my_list.longitud()
        print("Longitud de la lista:", longitud)
    elif opcion == "4":
        ultimo_numero = my_list.eliminar_ultimo()
        if ultimo_numero is not None:
            print("el numero ", ultimo_numero, "fue eliminado")
    elif opcion == "5":
         index = int(input("ingrese la posición"))
         numero_eliminado = my_list.eliminar_ubicacion(index)
         if numero_eliminado is not None:
            print("Número", numero_eliminado, "ha sido eliminado de la lista.")
    elif opcion == "6":
        valorr = int(input("Ingrese un número: "))
        apariciones = my_list.coincidencias(valorr)
        print("El número", numero, "aparece", apariciones, "vez/veces en la lista.")
    elif opcion == "7":
        valorr = int(input("Ingrese un número: "))
        posiciones = my_list.posiciones_del_numero(valorr)
        if len(posiciones) > 0:
            print("El número", valorr, "se encuentra en las posiciones:", posiciones)
        else:
            print("El número", numero, "no se encuentra en la lista.")
    elif opcion == "8":
        print("Números de la lista:")
        my_list.imprimir()
    elif opcion == "9":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")


    

    


        
        

