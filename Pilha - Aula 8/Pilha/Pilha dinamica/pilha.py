import implementation
class Pilha():
    def __init__(self):
        self.f1=implementation.Ibase()

    def insert(self,value):
            self.f1.insert_last(value)

    def show(self):
        self.f1.show()
        
    def remove(self):
        if not self.f1.be_empty():
               self.f1.remove_last()

    def be_empty(self):
        if self.f1.size==0:
            return True
        else:
            return False
    
