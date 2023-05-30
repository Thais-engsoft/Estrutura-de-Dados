
class No1():
    def __init__(self, name):
        self.elem = name
        self.next = None
        self.previous = None


class No2():
    def __init__(self):
        self.head = None
        self.chao = None

    def insertAt_Beginning(self, name):
        '''inserir valor no inicio da lista'''

        new_no = No1(name)
        if self.head is None:
            self.head = self.chao = new_no
        else:
            new_no.next = self.head
            self.head.previous = new_no
            self.head = new_no
       
       
    def insertAt_End(self, name):
        '''inserir valor no final da lista'''

        new_no = No1(name)
        if self.head is None:
            self.head = self.chao = new_no
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_no
            new_no.previous = current
            self.chao = new_no

 
    def remove(self, name):
            '''Remover valor da lista'''

            if self.head is None:
                return

            if self.head.elem == name:
                if self.head.next is not None:
                    self.head.next.previous = None
                self.head = self.head.next
                if self.head is None:
                    self.chao = None
                return

            current = self.head.next
            while current is not None:
                if current.elem == name:
                    if current.next is not None:
                        current.next.previous = current.previous
                    if current.previous is not None:
                        current.previous.next = current.next
                    else:
                        self.head = current.next
                    if current == self.chao:
                        self.chao = current.previous
                    return
                current = current.next


    def search(self, name):
        current = self.head
        index = 0

        while current is not None:
            if current.elem == name:
                return index
            current = current.next
            index += 1

        return -1


