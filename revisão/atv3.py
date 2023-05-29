'''Escreva um programa solicite ao usuário uma sequência de caracteres sem limite de
máximo de tamanho e realize as seguintes operações usando uma pilha: a) Imprimir o texto
na ordem inversa; b) Verificar se o texto é um palíndromo, ou seja, se a string é escrita da
mesma maneira de frente para trás e de trás para frente. Ignore espaços e pontos'''

class Pilha:
    #construtores da classe
    def __init__(self):
        self.dados = []

    #adiciona algo no final da pilha
    def empilhar(self, elemento):
        self.dados.append(elemento)

    #verifica se a pilha está vazia
    #Se a pilha não estiver vazia, o último elemento da lista dados é removido
    def desempilhar(self):
        if not self.vazia():
            return self.dados.pop()

    #verifica se a lista está vazia
    def vazia(self):
        return len(self.dados) == 0


    #recebe texto como entrada e remove os caracteres especiais presentes
    #
    def remover_caracteres_especiais(texto):
        caracteres_especiais = [' ', '.']
        return ''.join(c for c in texto if c not in caracteres_especiais)

    #A função inverter_texto recebe um texto como entrada e retorna o texto invertido. 
    #pilha recebe os métodos da classe PIlha
    #A cada iteração, o caractere é empilhado na pilha usando o método empilhar. Em seguida, 
    #a função cria uma string vazia texto_invertido e, usando um loop while, desempilha os 
    #caracteres da pilha e os concatena em texto_invertido. Por fim, a string texto_invertido
    #é retornada.
    def inverter_texto(texto):
        pilha = Pilha()
        for caractere in texto:
            pilha.empilhar(caractere)

        texto_invertido = ''
        while not pilha.vazia():
            texto_invertido += pilha.desempilhar()

        return texto_invertido

    # remove os caracteres especiais chamando a função remover_caracteres_especiais, inverte o 
    # texto chamando a função inverter_texto e compara se o texto original tem letras 
    # minúsculas é igual ao texto invertido em letras minúsculas. Ela retorna True se o texto 
    # for um palíndromo (ou seja, se o texto invertido for igual ao texto original) e False 
    # caso contrário.
    def verificar_palindromo(texto):
        texto = remover_caracteres_especiais(texto)
        texto_invertido = inverter_texto(texto)

        return texto.lower() == texto_invertido.lower()


# Solicitar a sequência de caracteres ao usuário
texto = input("Digite uma sequência de caracteres: ")

# Imprimir o texto na ordem inversa
texto_invertido = inverter_texto(texto)
print("Texto invertido:", texto_invertido)

# Verificar se o texto é um palíndromo
if verificar_palindromo(texto):
    print("O texto é um palíndromo.")
else:
    print("O texto não é um palíndromo.")
