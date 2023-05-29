'''Escreva um programa que simule o controle de uma pista de decolagem de aviões em
um aeroporto. Neste programa, o usuário deve ser capaz de realizar as seguintes tarefas:
a) Listar o número de aviões aguardando na fila de decolagem;
b) Autorizar a decolagem do primeiro avião da fila;
c) Adicionar um avião à fila de espera;
d) Listar todos os aviões na fila de espera;
e) Listar as características do primeiro avião da fila.
Considere que os aviões possuem um nome e um número inteiro como identificador.
Adicione outras características conforme achar necessário.
'''



class Aviao:
    def __init__(self, nome, identificador):
        self.nome = nome
        self.identificador = identificador
        self.caracteristicas = {}

    def adicionar_caracteristica(self, chave, valor):
        self.caracteristicas[chave] = valor


class Aeroporto:
    def __init__(self):
        self.fila_decolagem = []

    #listar todos os aviões que estão na fila 
    def listar_avioes_aguardando(self):
        quantidade = len(self.fila_decolagem)
        print("Número de aviões aguardando decolagem:", quantidade)

    #remover os aviões que decolaram
    def autorizar_decolagem(self):
        if self.fila_decolagem:
            aviao = self.fila_decolagem.pop(0)
            print("Autorizando decolagem do avião", aviao.nome)
        else:
            print("Não há aviões aguardando na fila de decolagem")

    #adiciona avião no final da fila
    def adicionar_aviao(self, aviao):
        self.fila_decolagem.append(aviao)
        print("Avião", aviao.nome, "adicionado à fila de espera")

    #aviões que estão na fila de espera para decolar
    def listar_avioes_espera(self):
        if self.fila_decolagem:
            print("Aviões na fila de espera:")
            for aviao in self.fila_decolagem:
                print("Nome:", aviao.nome, "| Identificador:", aviao.identificador)
        else:
            print("Não há aviões na fila de espera")

    def listar_caracteristicas_primeiro_aviao(self):
        if self.fila_decolagem:
            aviao = self.fila_decolagem[0]
            print("Características do primeiro avião na fila:")
            print("Nome:", aviao.nome)
            print("Identificador:", aviao.identificador)
            print("Características adicionais:")
            for chave, valor in aviao.caracteristicas.items():
                print(chave + ":", valor)
        else:
            print("Não há aviões na fila de espera")


# Criar um objeto do Aeroporto
aeroporto = Aeroporto()

while True:
    print("\n=== Controle de Decolagem ===")
    print("a) Listar aviões aguardando")
    print("b) Autorizar decolagem")
    print("c) Adicionar avião à fila de espera")
    print("d) Listar aviões na fila de espera")
    print("e) Listar características do primeiro avião na fila")
    print("s) Sair do programa")

    #opção recebe os valores do usuário
    opcao = input("Escolha uma opção: ")

    if opcao == "a":
        aeroporto.listar_avioes_aguardando()

    elif opcao == "b":
        aeroporto.autorizar_decolagem()

    elif opcao == "c":
        nome = input("Digite o nome do avião: ")
        identificador = int(input("Digite o identificador do avião: "))
        aviao = Aviao(nome, identificador)
        aeroporto.adicionar_aviao(aviao)

    elif opcao == "d":
        aeroporto.listar_avioes_espera()

    elif opcao == "e":
        aeroporto.listar_caracteristicas_primeiro_aviao()

    elif opcao == "s":
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
