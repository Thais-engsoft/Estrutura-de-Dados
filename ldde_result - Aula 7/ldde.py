class No():
    def __init__ (self,previous,value,after):
        self.before = previous
        self.data = value
        self.next = after

class Ldde():
    def __init__ (self):
        self.first = self.last = None
        self.size = 0

    def insert_initial(self,value):
        if self.size == 0:
            self.first = self.last = No(None,value,None)
        else:
            self.first.before = self.first = No(None,value,self.first)
        self.size+=1

    def insert_end(self,value):  
        if self.size == 0:
           self.first = self.last = No(None,value,None)
        else:
           self.last.next = self.last = No(self.last,value,None)
        self.size+=1
        
    def show(self):
        aux=self.first
        while aux != None:
            print(aux.data)
            aux=aux.next
            
    def remove_initial(self):
        if self.size == 1:
            self.first = self.last = None
        else:
            self.first = self.first.next
            self.first.before = None
        self.size-=1
        
    def remove_end(self):
        if self.size == 1:
            self.first = self.last = None
        else:
            self.last = self.last.before
            self.last.next = None
        self.size-=1
        
