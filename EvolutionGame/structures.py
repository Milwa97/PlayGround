from random import shuffle, random

class Player:
    def __init__(self, ID):
        self.level = 0
        self.ID = ID                
        self.opponent = 0               

    def __repr__(self):
        return repr((self.ID, self.level, self.opponent))

    def set_opponent(self, opponent):
         self.opponent = opponent
    
    def get_level(self):
         return self.level

    def upgrade(self):
        self.level = self.level + 1

    def degrade(self):
        if self.level != 0:
            self.level = self.level - 1    
             
        
class EvolutionGame:     
    def __init__(self, n, max_level, number_of_iterations):
        self.n = n
        self.max_level = max_level
        self.number_of_iterations = number_of_iterations
        self.players = []   
        for i in range(n):
            self.players.append( Player(i) )
                              
    
    def combat(self):  ##pair and combat      
        randm = list(range(self.n))
        shuffle(randm)      
        randm1 = randm[: self.n//2]
        randm2 = randm[self.n//2 :]              
        for i,j in zip(randm1, randm2):
            self.players[i].set_opponent(j)
            self.players[j].set_opponent(i)
            if random() >0.5:
                self.players[i].upgrade()
                self.players[j].degrade()
            else:
                self.players[i].degrade()
                self.players[j].upgrade()         
       
    
    def check_winner(self):
        for p in self.players:
            if p.get_level() >= self.max_level:
                return True
        return False
    
    
    def save(self, filename):
        with open(filename, 'w') as f:
            f.write("number of players: {:}\n".format(self.n))
            f.write("max level: {:}\n".format(self.max_level))
            f.write("number of iterations: {:}\n\n".format(self.number_of_iterations))   
            for p in self.players:
                f.write(p.__repr__()[1:-1])  ## maybe not the best way, but I want to save only numbers, without brackets
                f.write("\n")
        print("\n\nsaved to file {:}".format(filename))
    
    
    def run(self):
        for k in range(self.number_of_iterations):
            self.combat()
            #for p in self.players:
            #    print(p)
            if self.check_winner():
                self.number_of_iterations = k
                break
                
                
                
   