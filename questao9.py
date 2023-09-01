## Questão 9 - Escreva uma função para contar o número total de nós em uma árvore binária.

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
                
    def pos_order(self):
        if self.root is None:
            print('Árvore vazia.')
        else:
            self.pos_order_recursive(self.root)
    
    def pos_order_recursive(self, no):
        if no is not None:
            self.pos_order_recursive(no.left)
            self.pos_order_recursive(no.right)
            print(no.value, end=" ")
    
    def qtd_no(self):
        if self.root is None:
            return 0
        else:
            return self.qtd_no_recursive(self.root)
    
    def qtd_no_recursive(self, no):
        if no is None:
            return 0
        else:
            qtd_left = self.qtd_no_recursive(no.left)
            qtd_right = self.qtd_no_recursive(no.right)
            return 1 + qtd_left + qtd_right
    
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

total_no = binarytree.qtd_no()
print(total_no)