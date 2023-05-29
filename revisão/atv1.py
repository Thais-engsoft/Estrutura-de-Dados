
''' Escreva um programa em Python usando um TAD Fila que representa o cenário de uma
empresa de distribuição de mercadorias. A empresa é composta por dois balcões, onde
ambos atendem aos clientes que chegam. Todo cliente que chega retira uma senha, a
mesma pode ser do tipo 1 ou 2. Caso a senha seja do tipo 1, segue o atendimento por
ordem de chegada. Caso a senha seja do Tipo 2, segue o atendimento por ordem de
chegada entre os do Tipo 2, porém todos antecedem as do tipo 1. Ou seja, todos os clientes
do Tipo 2 são atendidos antes dos Clientes do Tipo 1. O programa inicialmente deverá
solicitar 10 entradas, onde será passado a informação do tipo da senha. E a cada 5 saídas
(remoções) um novo cliente deverá ser inserido na Fila'''


class Fila:
    #construção da classe
    def __init__(self):
        self.items = []

    #.append adicionar itens a fila - enfileira
    #recebe um parâmetro "item", que representa o elemento a ser adicionado à fila - adicionado ao final
    def enfileirar(self, item):
        self.items.append(item)

    #remove e retorna o primeiro elemento da fila. Antes de remover o elemento, é verificado se a fila não está vazia usando o método "esta_vazia". 
    #Caso a fila não esteja vazia, o método ".pop(0)" é utilizado para remover e retornar o primeiro elemento da lista "items".
    def desenfileirar(self):
        if not self.esta_vazia():
            return self.items.pop(0)

    #Retorna se a lista está ou não vazia
    def esta_vazia(self):
        return len(self.items) == 0

    #retorna a quantidade de elementos da fila
    def tamanho(self):
        return len(self.items)

    #vai mostrar todos os elementos da fila
    def imprimir_fila(self):
        print(self.items)


#fila <RECEBE> a classe Fila
fila = Fila()

#a contagem começa em 0
contador = 0

#início do loop
while True:

    # Solicita 10 entradas do usuário
    if contador < 10:
        tipo_senha = int(input("Digite o tipo da senha (1 ou 2): "))

        #vai chamar a classe+método que foi especificado na classe
        #contador vai adicionando mais um elemento na lista
        fila.enfileirar(tipo_senha)
        contador += 1

    else:
        # Realizar atendimento a cada 5 saídas (remoções)
        #realizar o atendimento de cinco clientes. 
        #A cada iteração do loop, o método "desenfileirar" da classe "Fila" é chamado para remover o primeiro elemento da fila. 
        #Se houver um cliente para atender (ou seja, o valor retornado pelo método "desenfileirar" não for "None"), 
        #é impressa a mensagem "Cliente atendido: Tipo" seguida pelo tipo de senha do cliente atendido. 
        #Após o loop, o contador é resetado para 0.
        for _ in range(5):
            atendimento = fila.desenfileirar()
            if atendimento is not None:
                print("Cliente atendido: Tipo", atendimento)
        contador = 0

    # Inserir novo cliente a cada 5 saídas (remoções)
    novo_cliente = int(input("Digite o tipo da senha do novo cliente (1 ou 2): "))
    fila.enfileirar(novo_cliente)

    # Imprimir fila a cada iteração
    print("Fila atual:")
    fila.imprimir_fila()
    print("------------------------")
