## Questão 2 - Implemente um método na classe `No` para inserir um novo valor em uma árvore binária.

class No:
    def __init__(self, value):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self): ## Criação da raíz.
        self.root = None ## Raíz inicialmente vazia.
    
    def insert(self, value): ## Inserção do valor.
        if self.root is None: ## Verificar se a raíz está vazia. 
            self.root = No(value) ## A raíz recebe novo valor.
        else:
            self.insert_recursive_level(value, self.root) ## Chamada de função recursiva para inserir valor caso a raíz estiver preenchida.
    
    def insert_recursive_level(self, value, no): ## Função recursiva. 
        if value < no.value: ## Verifica se o novo valor é menor que o valor contido no nó.
            if no.left is None: ## Caso o nó da esquerda estiver vazio.
                no.left = No(value) ## Nó da esquerda recebe novo valor.
            else: 
                self.insert_recursive_level(value, no.left) ## A função recursiva é chamada novamente.
        else: ## Caso o novo valor for maior que o valor contido no nó.
            if no.right is None: ## Verifica se o valor da direita está vazio.
                no.right = No(value) ## Nó da direita recebe novo valor.
            else: 
                self.insert_recursive_level(value, no.right) ## Função recursiva é chamada novamente.
