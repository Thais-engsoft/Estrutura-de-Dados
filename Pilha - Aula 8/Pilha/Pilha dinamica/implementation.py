class No():
    def __init__(self,value, next):
        self.data = value
        self.next =  next

class Ibase():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def show(self):
        aux=self.first
        while aux != None:
            print(aux.data)
            aux=aux.next
            
    def insert_last(self,value):
        if self.size==0:
            self.first=self.last=No(value,None)
        else:
            self.last.next=self.last=No(value,None)
        self.size+=1

    def remove_last(self):
        if self.size==1:
            self.first=self.last=None
        else:
            aux=self.first
            while aux.next != self.last:
                aux=aux.next
            self.last=aux
            aux.next=None
        self.size-=1

    def get_top(self):
        aux=self.first
        while aux != None:
            print(aux.data)
            break
        
    def be_empty(self):
        self.size==0
