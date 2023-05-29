'''Suponha que um dado problema requer o uso de duas pilhas, onde cada pilha suporta
no máximo 50 elementos e em nenhum momento as duas pilhas terão juntas mais do que
80 elementos. Assim, é possível implementar as duas pilhas em um único vetor usando
apenas 80 posições ao invés de 100. Implemente a estrutura de dados e as de empilhar e
desempilhar para estas duas pilhas'''

class DuasPilhas:

    #Construção da classe
    def __init__(self):
        #capacidade total das duas pilhas
        self.capacidade_total = 80
        #capacidade máxima de cada pilha individualmente
        self.capacidade_pilha = 50
        #vai armazenar os elementos das pilhas
        self.dados = [None] * self.capacidade_total
        #presenta o topo das duas pilhas
        self.topo1 = -1
        self.topo2 = self.capacidade_total

    #recebe elemento como parâmetro
    #verifica se há espaço disponível para empilhar na pilha 1
    def empilhar_pilha1(self, elemento):
        #se o 1 for menor que o 2, vai incrementar e armazenar em self.dados
        if self.topo1 < self.topo2 - 1:
            self.topo1 += 1
            self.dados[self.topo1] = elemento
        else:
            print("Pilha 1 está cheia. Não é possível empilhar o elemento.")

    def empilhar_pilha2(self, elemento):
        #Se o 1 for menor que 2, vai decrementar (diminuir valor) 
        if self.topo1 < self.topo2 - 1:
            self.topo2 -= 1
            self.dados[self.topo2] = elemento
        else:
            print("Pilha 2 está cheia. Não é possível empilhar o elemento.")

    #verifica se há elementos na pilha 1
    def desempilhar_pilha1(self):
        #(se topo1 for maior ou igual a 0). Se houver, o elemento do topo da é retornado (elemento), 
        #o valor correspondente em dados é definido como None, 
        # topo1 é decrementado e o elemento é retornado
        if self.topo1 >= 0:
            elemento = self.dados[self.topo1]
            self.dados[self.topo1] = None
            self.topo1 -= 1
            return elemento
        else:
            print("Pilha 1 está vazia.")

    def desempilhar_pilha2(self):
        #Ele verifica se há elementos na pilha 2 (se topo2 for menor que capacidade_total). 
        #Se houver, o elemento do topo da pilha é retornado (elemento), o valor correspondente 
        #em dados é definido como None, topo2 é incrementado e o elemento é retornado. Caso a 
        #pilha 2 esteja vazia, uma mensagem de erro é exibida.
        if self.topo2 < self.capacidade_total:
            elemento = self.dados[self.topo2]
            self.dados[self.topo2] = None
            self.topo2 += 1
            return elemento
        else:
            print("Pilha 2 está vazia.")

    def imprimir_pilha1(self):
        #Ele itera de topo1 até 0 (inclusivo) e imprime o elemento correspondente em dados. 
        #A cada iteração, um elemento é impresso em uma nova linha. Após imprimir todos os 
        #elementos, uma linha separadora é exibida.
        print("Pilha 1:")
        for i in range(self.topo1, -1, -1):
            print(self.dados[i])
        print("------------------------")


    def imprimir_pilha2(self):
        #Ele itera de topo2 até capacidade_total (exclusivo) e imprime o elemento correspondente
        #em dados. A cada iteração, um elemento é impresso em uma nova linha. 
        #Após imprimir todos os elementos, uma linha separadora é exibida.
        print("Pilha 2:")
        for i in range(self.topo2, self.capacidade_total):
            print(self.dados[i])
        print("------------------------")


#pilhas vai receber os métodos da classe DuasPilhas
pilhas = DuasPilhas()

#empilha o elemento x na pilha x
pilhas.empilhar_pilha1(10)
pilhas.empilhar_pilha1(20)
pilhas.empilhar_pilha1(30)
pilhas.empilhar_pilha2(40)
pilhas.empilhar_pilha2(50)
pilhas.imprimir_pilha1()
pilhas.imprimir_pilha2()

#desempilha elemento x da pilha x
elemento1 = pilhas.desempilhar_pilha1()
elemento2 = pilhas.desempilhar_pilha2()
print("Elemento desempilhado da Pilha 1:", elemento1)
print("Elemento desempilhado da Pilha 2:", elemento2)
print("------------------------")

#imprime os elemento da pilha x
pilhas.imprimir_pilha1()
pilhas.imprimir_pilha2()
