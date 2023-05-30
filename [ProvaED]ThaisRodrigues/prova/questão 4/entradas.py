from classes import Pilha

pilha = Pilha()

print(pilha.is_empty()) 

pilha.push(5)
pilha.push(10)
pilha.push(20)

print(pilha.top())
print(pilha.pop()) 
print(pilha.top())

# adicionando mais um
pilha.push(35)

print(pilha.pop())  
print(pilha.top())  
print(pilha.pop())  
print(pilha.pop())  
print(pilha.is_empty())

