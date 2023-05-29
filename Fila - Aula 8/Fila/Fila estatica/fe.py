class Fe():
    def __init__(self):
        self.list = [None,None,None,None,None]
        self.size = 0
        
    def insert(self, value):
        self.list[self.size] = value
        self.size+=1

    def remove(self):
        for i in range(self.size-1):
            self.list[i] = self.list[i+1]
        self.size-=1

    def be_empty(self):
        return self.size==0

    def be_full(self):
        return self.size==5

    def get_first(self):
        return self.list[0]

    def get_last(self):
        return self.list[self.size-1]

    def show(self):
        for i in range(self.size):
            print(self.list[i],end='')
        print()
