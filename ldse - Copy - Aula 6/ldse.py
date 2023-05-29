class No():
    def __init__(self,valor, proximo):
        self.inf = valor
        self.prox = proximo

class Ldse():
    def __init__(self):
        self.prim = None
        self.ult = None
        self.quant = 0

    def insertStart(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.prim=No(valor,self.prim)
        self.quant+=1
        
    def removeInitial(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            self.prim=self.prim.prox
        self.quant-=1
        
    def show(self):
        aux=self.prim
        while aux != None:
            print(aux.inf)
            aux=aux.prox
            
    def insertEnd(self,valor):
        if self.quant==0:
            self.prim=self.ult=No(valor,None)
        else:
            self.ult.prox=self.ult=No(valor,None)
        self.quant+=1

    def removeEnd(self):
        if self.quant==1:
            self.prim=self.ult=None
        else:
            aux=self.prim
            while aux.prox != self.ult:
                aux=aux.prox
            self.ult=aux
            aux.prox=None
        self.quant-=1

    def insertafterDet(self,valor1,valor2):
        aux=self.prim
        while aux.inf != valor2:
            aux=aux.prox
#       print(aux.inf)
        aux.prox=self.ult=No(valor1,None)
        
        self.quant+=1

