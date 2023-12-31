## Prática 4 - Nesta atividade prática de Programação Estruturada e Estrutura de Dados, 
# você será desafiado a desenvolver um software em Python que crie uma árvore binária 
# a partir de um conjunto de números não repetitivos inseridos em níveis. 
# Ao final, o software deverá exibir informações cruciais da árvore, 
# como a raiz, a altura, os nós internos e as folhas. Adicione também uma função de busca: ao informar um número, 
# o software deve responder se o número está ou não presente na árvore.

from random import randint

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def mostrar_root(self):
        return self.root.value
    
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
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self.buscar_value_recursive(node.left, value)
        else:
            return self.buscar_value_recursive(node.right, value)
        
    def height_tree(self):
        return self.height_tree_recursive(self.root) - 1
        
    def height_tree_recursive(self, node):
        if node is None:
            return 0
        else:
            left_tree = self.height_tree_recursive(node.left)
            right_tree = self.height_tree_recursive(node.right)
            return max(left_tree, right_tree) + 1
        
    def node_interno(self, node):
        if node is None:
            return
        if node.left or node.right:
            print(node.value, end=" ")
        self.node_interno(node.left)
        self.node_interno(node.right)
        
    def folha(self, node):
        if node is None:
            return
        if node.left is None and node.right is None:
            print(node.value, end=" ")
        self.folha(node.left)
        self.folha(node.right)
        
binarytree = BinaryTree()

value = list()
QTD_VALUE_TREE = 7

while len(value) < QTD_VALUE_TREE:
    i = randint(1, 30)
    if i not in value:
        binarytree.insert(i)
        value.append(i)

print('Árvore em pós-ordem: ')
binarytree.pos_order()
print()

print(f'Raiz: {binarytree.mostrar_root()}')
print(f'Altura: {binarytree.height_tree()}')

print('Nós internos: ')
binarytree.node_interno(binarytree.root)
print()

print('Folhas: ')
binarytree.folha(binarytree.root)
print()

value_find = int(input('Buscar valor: '))

if binarytree.buscar_value(value_find):
    print('Valor presente.')
else:
    print('Valor ausente.')
    
    