from classes import No2

fila = No2()

print(f"A fila está vazia?:  {fila.isempty()}")

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(5)
fila.enqueue(6)
fila.enqueue(7)
fila.enqueue(8)
fila.enqueue(9)
fila.enqueue(10)
fila.enqueue(11)

print(f"\nA fila está cheia? {fila.isfull()}")

fila.dequeue()
fila.dequeue()
fila.dequeue()

print(f"\nTamanho atual da fila: {len(fila.cont)}")
