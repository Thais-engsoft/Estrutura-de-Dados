
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
    def __init__(self):
        self.items = []

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.items.pop(0)

    def esta_vazia(self):
        return len(self.items) == 0

    def tamanho(self):
        return len(self.items)

    def imprimir_fila(self):
        print(self.items)


fila = Fila()
contador = 0

while True:
    # Solicitar 10 entradas
    if contador < 10:
        tipo_senha = int(input("Digite o tipo da senha (1 ou 2): "))
        fila.enfileirar(tipo_senha)
        contador += 1
    else:
        # Realizar atendimento a cada 5 saídas (remoções)
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
