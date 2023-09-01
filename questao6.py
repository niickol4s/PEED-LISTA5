## Questão 6 - Implemente uma função que realiza uma travessia pré-ordem (raiz-esquerda-direita) 
# em uma árvore binária e retorna os valores dos nós visitados.

class No:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = No(value)
        else:
            self.insert_recursive_level(value, self.root)
    
    def insert_recursive_level(self, value, no):
        if value < no.value:
            if no.left is None:
                no.left = No(value)
            else:
                self.insert_recursive_level(value, no.left)
        else:
            if no.right is None:
                no.right = No(value)
            else:
                self.insert_recursive_level(value, no.right)
    
    def pre_order(self):
        if self.root is None:
            print('Árvore vazia.')
        else:
            self.pre_order_recursive(self.root)
    
    def pre_order_recursive(self, no):
        print(no.value, end=" ")
        if no.left is not None:
            self.pre_order_recursive(no.left)
        if no.right is not None:
            self.pre_order_recursive(no.right)

binarytree = BinaryTree()

binarytree.insert(5)
binarytree.insert(3)
binarytree.insert(7)
binarytree.insert(2)
binarytree.insert(4)
binarytree.insert(6)
binarytree.insert(8)
binarytree.pre_order()
print()
    