## Ayush Thakur

## A class to describe genotype | data or genetic information

import random

def newChar():
        c = random.randint(63,122)
        if(c==63):c = 32
        if(c==64):c = 46

        return(chr(c))

class DNA:
        def __init__(self, num):
                self.num = num
                self.genes = []
                self.fitness = 0

                for i in range(num):
                        self.genes.append(newChar())

        def getPhrase(self):
                return(''.join(self.genes))

        ###fitness function

        def calcFitness(self, target):
                score = 0
                for i in range(len(self.genes)):
                        if(self.genes[i] == target[i]):
                                score = score+1

                self.fitness = score/len(target)

        ###crossover
        
        def crossover(self, partner):
                child = DNA(len(self.genes))
                midpoint = random.randint(0, len(self.genes)-1)

                for i in range(len(self.genes)):
                        if(i>midpoint):
                                child.genes[i] = self.genes[i]
                        else:
                                child.genes[i] = partner.genes[i]

                return child

        ###mutate

        def mutate(self, mutationRate):
                for i in range(len(self.genes)):
                        if(random.random() < mutationRate):
                                self.genes[i] = newChar()

                                
        

        




















        
