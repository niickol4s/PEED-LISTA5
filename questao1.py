## Questão 1 - Crie uma classe `No` que represente um nó em uma árvore binária. 
## A classe deve ter atributos para armazenar o valor do nó, o nó esquerdo e o nó direito.

class No:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None