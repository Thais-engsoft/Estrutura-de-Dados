#Lista Estática Sequencial
from ast import Return


class Les():
    #init é o construtor da classe
    #self é a referência ao objeto atual que está sendo criado
    #count é a quantidade de elementos presentes na lista.
    def __init__(self):
        self.list=[None,None,None,None,None]
        self.count=0

    def insert_start(self, value):
        '''insere valor no inicio da
        lista empurrando os demais valores
        para trás '''  
        #parâmetro value que representa o valor a ser inserido no início da lista.
        #verificar se há espaço disponível na lista para a operação, verificando o atributo
        #count
        # se tiver espaço disponível, vai empurar os valores para trás
        if self.count < len(self.list):
            for i in range(self.count - 1):
                #Em cada iteração, atribua o valor da posição atual para a posição seguinte
                self.list[i+1] = self.list[i]
             
            #vai inserir o valor na primeira posição da lista (posição 0)   
            self.list[0] = value      
            #incrementa em 1, para refletir a inserção do novo valor na lista;
            self.count +=1
        else:
            print("A lista está cheia, não é possível adicionar mais elementos")
        

    def insert_end(self, value):
        '''insere valor após o último
        elelmento da lista'''
        
        
        #mesmas verificações da questão de cima
        if self.count < len(self.list):
            
            #vai inserir o valor VALUE na posição self.count da lista
            self.list[self.count] = value
            self.count += 1
            
        else:
            print("A lista está cheia, não é possível adicionar mais elementos")
            
            
            
    def remove_start(self):
        '''remove o primeiro valor da
        lista, trazendo os demais uma
        posição pra frente'''


        if self.count > 0:
            for i in range(1, self.count):
                self.list[i - 1] = self.list[i]
            self.list[self.count - 1] = None
            self.count -= 1
        
        else:
            print("A lista está cheia, não é possível adicionar mais elementos")
            
                       
                
    def remove_end(self):
        '''remove o ultimo elemento da lista'''
        if self.count > 0:
            self.list [self.count - 1] = None
            self.count -= 1
            
        else:
            print("A lista está cheia, não é possível adicionar mais elementos")
        
        

    def be_empty(self):
        '''retorna true se a lista vazia e falhe
        caso contrário'''
        
        if self.count == 0:
            return True
        else:
            return False
        

    def be_full(self):
        '''retorna true se lista cheia e false caso contrário'''
        
        if self.count == len(self.list):
            return True
        else:
            False

    def get_prim(self):
        '''retorna o primeiro elemento
        da lista (retorna nada se a lista estiver vazia)'''
        
        if self.count > 0:
            return self.list[0]

    def get_ult(self):
        '''retorna o ultimo elemento
        da lista(retorna nada se lista vazia)'''
        if self.count > 0:
            return self.list[self.count -1]
        

    def show(self):
        '''imprime todos os elementos da lista'''
        for i in range(self.count):
            print(self.lits[i])






    def insert_after_det(self, value1, value2):
        '''insere valor1 após conf ocorrencia de valor 2
        enquanto for possivel'''
        found = False
        for i in range(self.count):
            if self.list[i] == value2:
                found = True
                for j in range(self.count, i, -1):
                    self.list[j] = self.list[j-1]
                    
                self.list[i+1] = value1
                self.count += 1
                break
        if not found:
            print(f"O valor {value2} não foi encontrado na lista. Inserção não realizada")
        
        
        
        

    def insert_after_det_account(self, value1, value2):
        '''insere valor1 apos cada ocorrencia de valor2
        enquanto for possivel retornando a quantidade
        de inserçõens realizadas'''

        '''fazer tambem um programa 'inteligente" de teste'''
        
        
    #Variável que vai ser usada para contar o número de iserções realizadas
    insert_count = 0
    
    #loop para percorrer a lista a partir do índice 0
    for i in range(self.count):
        
        if self.list[i] == value2:
            # vai deslocar os elementos seguintes uma posição para a direita
            
            for j in range(self.count, i, -1):
                self.list[j+1] = self.list[j]
                
                
            # vai inserir o value1 na posição seguinte à ocorrência de value2
            self.list[i+1] = value1
            insert_count += 1
            
    self.count += insert_count  # Atualizar o atributo count
    return insert_count  # Retornar a quantidade de inserções realizadas