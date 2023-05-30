
class No1():
    def __init__(self, valor):
        self.elem = valor
        self.next = None


class No2():
    def __init__(self):
        self.head = None
        self.cont = 0

    def insertAt_Beginning(self, valor):
        '''inserir valor no inicio da lista'''
        new_no = No1(valor)  
        new_no.next = self.head  
        self.head = new_no  
        self.cont += 1  
       
    def insertAt_End(self, valor):
        '''inserir valor no final da lista'''
        new_no = No1(valor)  

        if self.head is None:
            self.head = new_no 
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_no  

        self.cont += 1  
      

    def remove(self, valor):
        lista = self.head
        rastrear = None

        while lista is not None:
            if lista.elem == valor:
                if rastrear is None:
                    self.head = lista.next  
                else:
                    rastrear.next = lista.next  

                self.cont -= 1  
                return

            rastrear = lista
            lista = lista.next

    def search(self, valor):
        current = self.head
        index = 0

        while current is not None:
            if current.elem == valor:
                return index  

            current = current.next
            index += 1

        return -1 





