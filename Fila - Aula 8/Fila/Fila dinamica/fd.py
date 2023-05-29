class No():
    def __init__(self,value,next):
        self.data = value
        self.next = next
        
class Fd():
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def insert(self,value):
        if self.size==0:
            self.first=self.last=No(value,None)
        else:
            self.first=No(value,self.first)
        self.size+=1
        
    def remove(self):
        if self.size==1:
            self.first=self.last=None
        else:
            self.first=self.first.next
        self.size-=1
        
    def show(self):
        aux=self.first
        while aux != None:
            print(aux.data)
            aux=aux.next
            
    def be_empty(self):
        self.size==0
        
