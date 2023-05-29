class Word():
    def __init__(self):
        self.letters = [None]*5
        self.count = 0

    def insert_letter(self, letter):
        '''insere letra na palavra'''
    
        self.letters[self.count] = letter
        self.count += 1

    def print_word(self):
        '''imprime a palavra'''
        
        
        # list = self.letters[0:self.count]
        # word = ''.join(list)
        # print(word)
        

        i = 0 
        while i < self.count:
            print(self.letters[i], end='')
            i+=1

    def remove_letter(self):
        '''remove a ultima letra da lista e da palavra'''

        # del self.letters[self.count-1]
        # self.count -= 1 
        # self.letters.append(None)

        '''remove a ultima letra da palavra'''
        self.count -= 1 

    def insert_letter_at_beginning(self, letter):
        '''insere letra no Inicio da palavra (para isso, move
        ás demais para trás)'''

        # if self.count < 5:
        #     self.letters.insert(0, letter)
        #     self.count += 1
        # else:
        #     raise Exception("The List is Full")

        for i in range(self.count, 0, -1):
            self.letters[i]=self.letters[i-1]
        self.letters[0]=letter
        self.count += 1

    def remove_letter_at_beginning(self):
        '''remove a primeira letra da palavra, trazendo as 
        demais para frente'''

        for i in range(self.count):
            self.letters[i] = self.letters[i+1]
        self.count -= 1
    
    def full_word(self):
        '''verifica se a lista está com todos os espaços ocupados, 
        se Sim retorna True, senão retorna False'''

        if self.count == 5:
            return True
        else:
            False