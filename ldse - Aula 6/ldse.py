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
    
    
    # Retorna o valor correspondente ao índice fornecido
    # a = instance[5] -- instance.__getitem_(index)
     def __getitem__(self, index):

        #Se o índice estiver entre 0 e self.count - 1 (onde self.count representa o número total 
        #de elementos no objeto), o método retorna o elemento correspondente ao índice usando a 
        #expressão self.list[index], onde self.list é uma lista (ou outro objeto semelhante) 
        #contendo os elementos.
        if 0 <= index < self.count:
            return self.list[index]
        

        #menor que zero ou maior ou igual a self.count, o método lança uma exceção IndexError 
        #com a mensagem "Índice fora do intervalo válido". Isso indica que o índice fornecido 
        #não está dentro dos limites permitidos e gera um erro para informar que a operação 
        #não pode ser realizada.
        else:
            raise IndexError("Índice fora do intervalo válido")

    # Atribui um valor ao índice fornecido
    # instance[6] = 7   
     def __setitem__(self, index, value):

        #value é o valor que será atribuído
        #Se o índice estiver entre 0 e self.count - 1 (onde self.count representa o número total
        #de elementos no objeto), o método atribui o valor fornecido ao elemento correspondente 
        #ao índice usando a expressão self.list[index] = value, onde self.list é uma lista (ou 
        #outro objeto semelhante) contendo os elementos.
        if 0 <= index < self.count:
            self.list[index] = value
        else:
            raise IndexError("Índice fora do intervalo válido")
