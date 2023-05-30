class No2():
    def __init__(self):
        self.elem = 10
        self.cont = []

    def enqueue(self, item):
        if len(self.cont) <= 10:
            self.cont.append(item)
            print(f"Elemento {item} adicionado à fila! ")
        else:
            print("A fila está cheia!")

    def dequeue(self):
        if self.cont:
            item = self.cont.pop(0)
            print(f"Elemento {item} foi removido da fila!")
            return item
        else:
            print("A fila está vazia!")
            return None

    def isfull(self):
        return len(self.cont) == self.elem

    def isempty(self):
        return len(self.cont) == 0
