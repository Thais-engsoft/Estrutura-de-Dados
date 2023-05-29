class No():
    def __init__(self,valor):
        self.inf = valor
        self.next = None

class Ldse2():
    def __init__(self):
        self.first = None
        self._size = 0

    def append(self, value):
        if self.first:
            #inserção quando a lista já possui elementos
            pointer = self.first
            while(pointer.next):
                pointer = pointer.next
            pointer.next = No(value)
        else:
            #primeira inserção
            self.first = No(value)
        self._size = self._size + 1

    def __len__(self):
        '''retorna o tamanho da lista'''
        return self._size

    def __getitem__(self, index):
        #a = lista[6]
        pointer = self.first
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        #agora o pinter esta na posição que eu quero
        if pointer:
            return pointer.inf
        raise IndexError("list index out of range")

    def __setitem__(self, index, value):
        #lista[6] = 9
        pointer = self.first
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        #agora o pinter esta na posição que eu quero
        if pointer:
            pointer.inf = value
        else:
            raise IndexError("list index out of range")
