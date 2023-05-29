import implementation
class Pilha():
    def __init__(self):
        self.f1=implementation.Ibase()
        self.f2=implementation.Ibase()

    def insert(self,value, prio):
        if prio == 1:
            self.f1.insert_last(value)
        elif prio == 2:
            self.f2.insert_last(value)
            
    def show(self):
        self.f1.show()
        self.f2.show()
        
    def remove(self):
        if not self.f1.be_empty():
               self.f1.remove_last()
        else:
               self.f2.remove_last()
