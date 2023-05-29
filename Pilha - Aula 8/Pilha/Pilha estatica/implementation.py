class Ibase():
    def __init__(self):
        self.list = [None,None,None,None,None]
        self.size = 0
        
    def insert_last(self,value):
        self.list[self.size] = value
        self.size+=1

    def remove_last(self):
        self.size-=1
        
    def be_empty(self):
        return self.size == 0

    def getUlt(self):
        return self.list[self.size-1]

    def show(self):
        for i in range(self.size):
            print(self.list[i],end='')
        print()

