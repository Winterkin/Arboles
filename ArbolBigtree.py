from bigtree import Node, print_tree, find_name


#Crear estructura de árbol no binario
raiz = Node("CEO", desc="Director Ejecutivo")
cto = Node("CTO", parent=raiz, desc="Director Tecnología")
cfo = Node("CFO", parent=raiz, desc="Director Financiero")
coo = Node("COO", parent=raiz, desc="Director Operaciones")


#Añadir nodos hijos (no binario - múltiples hijos)
dev1 = Node("Dev1", parent=cto, desc="Desarrollador Senior")
dev2 = Node("Dev2", parent=cto, desc="Desarrollador Junior")
qa = Node("QA", parent=cto, desc="Control Calidad")

fin1 = Node("Fin1", parent=cfo, desc="Contabilidad")
fin2 = Node("Fin2", parent=cfo, desc="Tesorería")

#Visualizar el árbol
print("Árbol organizacional completo:")
print_tree(raiz, all_attrs=True)

#Acceder a propiedades
print("\nSubárbol del CTO:")
print_tree(cto)

#Buscar nodos
nodo_encontrado = find_name(raiz, "Dev2")
print(f"\nInformación de Dev2: {nodo_encontrado.describe(excludeprefix='')}")