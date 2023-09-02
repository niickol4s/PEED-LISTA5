## Questão 3 - Implemente um método na classe `Arvore` que verifica se um valor está presente na árvore.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursive_level(value, self.root)
    
    def insert_recursive_level(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_recursive_level(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_recursive_level(value, node.right)
                
    def pos_order(self):
        if self.root is None:
            print('Árvore vazia.')
        else:
            self.pos_order_recursive(self.root)
            
    def pos_order_recursive(self, node):
        if node is not None:
            self.pos_order_recursive(node.left)
            self.pos_order_recursive(node.right)
            print(node.value, end=" ")
            
    def buscar_value(self, value):
        return self.buscar_value_recursive(self.root, value)
    
    def buscar_value_recursive(self, node, value):
        if value == node.value: ## Primeiro caso. O valor atual é o valor buscado.
            return True
        elif value < node.value: ## Segundo caso. O valor atual é menor que o valor armazenado no nó. Busca na esquerda.
            return self.buscar_value_recursive(node.left, value)
        else: ## Terceiro caso. O valor atual é maior que o valor armazenado. Busca na direita.
            return self.buscar_value_recursive(node.right, value)
            
binarytree = BinaryTree()

binarytree.insert(5)
binarytree.insert(3)
binarytree.insert(7)
binarytree.insert(2)
binarytree.insert(4)
binarytree.insert(6)
binarytree.insert(8)
binarytree.pos_order()
print()

value_find = 7
print(f'Buscar valor: {value_find}.')

if binarytree.buscar_value(value_find):
    print('Valor presente.')
else:
    print('Valor ausente.')