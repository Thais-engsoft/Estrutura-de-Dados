from classes import No2
Lista_valor = No2()

# Inserindo elementos no início da lista
Lista_valor.insertAt_Beginning("ALBERTO")
Lista_valor.insertAt_Beginning("LUIZ")
Lista_valor.insertAt_Beginning("JOÃO")

# Inserindo valores no final da lista
Lista_valor.insertAt_End("ANA")
Lista_valor.insertAt_End("PALOMA")
Lista_valor.insertAt_End("MARIA")

# remove os valores da lista
Lista_valor.remove("MARIA")

#SEARCH
indice = Lista_valor.search("THAIS")
if indice != -1:
    True
else:
    False

# Imprimindo os valores da lista
algo = Lista_valor.head
while algo is not None:
    print(algo.elem)
    algo = algo.next

