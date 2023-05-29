class Pilha:
    def __init__(self):
        self.dados = []

    def empilhar(self, elemento):
        self.dados.append(elemento)

    def desempilhar(self):
        if not self.vazia():
            return self.dados.pop()

    def vazia(self):
        return len(self.dados) == 0


def remover_caracteres_especiais(texto):
    caracteres_especiais = [' ', '.']
    return ''.join(c for c in texto if c not in caracteres_especiais)


def inverter_texto(texto):
    pilha = Pilha()
    for caractere in texto:
        pilha.empilhar(caractere)

    texto_invertido = ''
    while not pilha.vazia():
        texto_invertido += pilha.desempilhar()

    return texto_invertido


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
