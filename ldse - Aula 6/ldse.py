'''Implementação'''

class No():
    def __init__(self, value):
        self.data = value
        self.next = None

class ElementList():
     def __init__(self):
         self.first = None
         self._size = 0

     def append(self, value):
         if self.first:
            pointer = self.first
            while(pointer.next):
                pointer = pointer.next
            pointer.next = No(value)
         else:
             self.first = No(value)
         self._size = self._size + 1

     def __len__(self):
        return self._size
     
     
     
     
     '''implemente os métodos GET e SET para
        se comportarem conforme o comentario
        na descrição do método'''
     
     def __getitem__(self, index):
        # Retorna o valor correspondente ao índice fornecido
        # a = instance[5] -- instance.__getitem_(index)
        
        if 0 <= index < self.count:
            return self.list[index]
        else:
            raise IndexError("Índice fora do intervalo válido")
        
     def __setitem__(self, index, value):
        # Atribui um valor ao índice fornecido
        # instance[6] = 7 
        if 0 <= index < self.count:
            self.list[index] = value
        else:
            raise IndexError("Índice fora do intervalo válido")