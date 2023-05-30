from classes import No2
Lista_valor = No2()

# Inserindo elementos no início da lista
Lista_valor.insertAt_Beginning(10)
Lista_valor.insertAt_Beginning(20)
Lista_valor.insertAt_Beginning(30)

# Inserindo valores no final da lista
Lista_valor.insertAt_End(12)
Lista_valor.insertAt_End(26)
Lista_valor.insertAt_End(45)

# remove os valores da lista
Lista_valor.remove(12)


indice = Lista_valor.search(30)
print(indice)  # Saída: 2

indice = Lista_valor.search(60)
print(indice)  # Saída: -1

# Imprimindo os valores da lista
algo = Lista_valor.head
while algo is not None:
    print(algo.elem)
    algo = algo.next
