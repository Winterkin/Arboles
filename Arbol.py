#Esteban Figueroa
#Jhoan Barreto

from collections import deque

class NodoLista:
    def __init__(self, dato):
        self.data = dato
        self.siguiente = None

class NodoArbol:
    def __init__(self, dato):
        self.data = dato
        self.izquierdo = None
        self.derecho = None

def convert(cabeza):
    if not cabeza:
        return None

    q = deque()

    root = NodoArbol(cabeza.data)
    q.append(root)

    cabeza = cabeza.next

    while cabeza:

        padre = q.popleft()

        hijoizquierdo = None
        hijoderecho = None

        if cabeza:
            hijoizquierdo = NodoArbol(cabeza.data)
            q.append(hijoizquierdo)
            cabeza = cabeza.next

        if cabeza:
            hijoderecho = NodoArbol(cabeza.data)
            q.append(hijoderecho)
            cabeza = cabeza.next

        padre.izquierdo = hijoizquierdo
        padre.derecho = hijoderecho

    return root

def altura(root):
    if root is None:
        return -1

    alturai = altura(root.izquierdo)
    alturad = altura(root.derecho)

    return max(alturai, alturad) + 1



if __name__ == "__main__":
  
    peso=0
    print("Inserte los datos que quiere meter al arbol, escriba fin para terminarlo")
    while entrada!="fin":
        entrada=input("inserte el siguiente dato del arbol")
        cabeza=NodoLista(entrada)
        cabeza=cabeza.siguiente
        peso=peso+1
    root = convert(cabeza)
    print("la altura del arbol es")
    altura(root)
    print("el peso del arbol es")
    print(peso)