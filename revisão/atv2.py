class DuasPilhas:
    def __init__(self):
        self.capacidade_total = 80
        self.capacidade_pilha = 50
        self.dados = [None] * self.capacidade_total
        self.topo1 = -1
        self.topo2 = self.capacidade_total

    def empilhar_pilha1(self, elemento):
        if self.topo1 < self.topo2 - 1:
            self.topo1 += 1
            self.dados[self.topo1] = elemento
        else:
            print("Pilha 1 está cheia. Não é possível empilhar o elemento.")

    def empilhar_pilha2(self, elemento):
        if self.topo1 < self.topo2 - 1:
            self.topo2 -= 1
            self.dados[self.topo2] = elemento
        else:
            print("Pilha 2 está cheia. Não é possível empilhar o elemento.")

    def desempilhar_pilha1(self):
        if self.topo1 >= 0:
            elemento = self.dados[self.topo1]
            self.dados[self.topo1] = None
            self.topo1 -= 1
            return elemento
        else:
            print("Pilha 1 está vazia.")

    def desempilhar_pilha2(self):
        if self.topo2 < self.capacidade_total:
            elemento = self.dados[self.topo2]
            self.dados[self.topo2] = None
            self.topo2 += 1
            return elemento
        else:
            print("Pilha 2 está vazia.")

    def imprimir_pilha1(self):
        print("Pilha 1:")
        for i in range(self.topo1, -1, -1):
            print(self.dados[i])
        print("------------------------")

    def imprimir_pilha2(self):
        print("Pilha 2:")
        for i in range(self.topo2, self.capacidade_total):
            print(self.dados[i])
        print("------------------------")


# Exemplo de uso
pilhas = DuasPilhas()

pilhas.empilhar_pilha1(10)
pilhas.empilhar_pilha1(20)
pilhas.empilhar_pilha1(30)
pilhas.empilhar_pilha2(40)
pilhas.empilhar_pilha2(50)
pilhas.imprimir_pilha1()
pilhas.imprimir_pilha2()

elemento1 = pilhas.desempilhar_pilha1()
elemento2 = pilhas.desempilhar_pilha2()
print("Elemento desempilhado da Pilha 1:", elemento1)
print("Elemento desempilhado da Pilha 2:", elemento2)

pilhas.imprimir_pilha1()
pilhas.imprimir_pilha2()
