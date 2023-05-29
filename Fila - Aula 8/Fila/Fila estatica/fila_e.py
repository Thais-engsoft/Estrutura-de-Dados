import fe
class FilaE():
    def __init__(self):
        self.f1 = fe.Fe()
        self.f2 = fe.Fe()

    def insert(self,value, prio):
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
