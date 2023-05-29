import fd
class No():
    def __init__(self,value,proximo):
        self.inf = value
        self.prox = proximo
        
class FilaD():
    def __init__(self):
        self.f1 = fd.Fd()
        self.f2 = fd.Fd()

    def insert(self,value,prio):
        if prio == 1:
            self.f1.insert(value)
        elif prio == 2:
            self.f2.insert(value)
            
    def show(self):
        self.f1.show()
        self.f2.show()
        
    def remove(self):
        if not self.f1.be_empty():
               self.f1.remove()
        else:
               self.f2.remove()
    
    def be_empty(self):
        if self.f1.size == 0 and self.f2.size == 0:
            return True
        else:
            return False
    
