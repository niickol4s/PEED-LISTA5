## Questão 10 - Escreva uma função que encontre o valor máximo armazenado em uma árvore binária.

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
            
    def max_value(self): ## Função para encontrar o valor máximo na árvore
        no_atual = self.root ## Nó atual recebe a raíz
        while no_atual.right: ## Percorre a árvore da direita
            no_atual = no_atual.right 
        return no_atual.value ## Retorna o valor do nó atual

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

print(binarytree.max_value())
